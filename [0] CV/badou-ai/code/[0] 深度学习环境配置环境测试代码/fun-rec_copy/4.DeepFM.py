import tensorflow as tf
from utils import *
import pandas as pd
from tensorflow.keras.models import *
import warnings
warnings.filterwarnings("ignore")


class FM_Layer(Layer):
    def __init__(self):
        super(FM_Layer, self).__init__()

    def call(self, inputs):
        # 优化后的公式为： 0.5 * 求和（和的平方-平方的和）  =>> B x 1
        concated_embeds_value = inputs # B x n x k

        square_of_sum = tf.square(tf.reduce_sum(concated_embeds_value, axis=1, keepdims=True)) # B x 1 x k
        sum_of_square = tf.reduce_sum(concated_embeds_value * concated_embeds_value, axis=1, keepdims=True) # B x1 xk
        cross_term = square_of_sum - sum_of_square # B x 1 x k
        cross_term = 0.5 * tf.reduce_sum(cross_term, axis=2, keepdims=False) # B x 1

        return cross_term

    def compute_output_shape(self, input_shape):
        return (None, 1)


def get_fm_logits(sparse_input_dict, sparse_feature_columns, dnn_embedding_layers):
    # 将特征中的sparse特征筛选出来
    sparse_feature_columns = list(filter(lambda x: isinstance(x, SparseFeat), sparse_feature_columns))

    # 只考虑sparse的二阶交叉，将所有的embedding拼接到一起进行FM计算
    # 因为类别型数据输入的只有0和1所以不需要考虑将隐向量与x相乘，直接对隐向量进行操作即可
    sparse_kd_embed = []
    for fc in sparse_feature_columns:
        feat_input = sparse_input_dict[fc.name]
        _embed = dnn_embedding_layers[fc.name](feat_input) # B x 1 x k
        sparse_kd_embed.append(_embed)

    # 将所有sparse的embedding拼接起来，得到 (n, k)的矩阵，其中n为特征数，k为embedding大小
    concat_sparse_kd_embed = Concatenate(axis=1)(sparse_kd_embed) # B x n x k
    fm_cross_out = FM_Layer()(concat_sparse_kd_embed)

    return fm_cross_out


def get_dnn_logits(sparse_input_dict, sparse_feature_columns, dnn_embedding_layers):
    # 将特征中的sparse特征筛选出来
    sparse_feature_columns = list(filter(lambda x: isinstance(x, SparseFeat), sparse_feature_columns))

    # 将所有非零的sparse特征对应的embedding拼接到一起
    sparse_kd_embed = []
    for fc in sparse_feature_columns:
        feat_input = sparse_input_dict[fc.name]
        _embed = dnn_embedding_layers[fc.name](feat_input) # B x 1 x k
        _embed = Flatten()(_embed) # B x k
        sparse_kd_embed.append(_embed)

    concat_sparse_kd_embed = Concatenate(axis=1)(sparse_kd_embed) # B x nk

    # dnn层，这里的Dropout参数，Dense中的参数都可以自己设定，以及Dense的层数都可以自行设定
    mlp_out = Dropout(0.5)(Dense(256, activation='relu')(concat_sparse_kd_embed))
    mlp_out = Dropout(0.3)(Dense(256, activation='relu')(mlp_out))
    mlp_out = Dropout(0.1)(Dense(256, activation='relu')(mlp_out))

    dnn_out = Dense(1)(mlp_out)

    return dnn_out


def DeepFM(linear_feature_columns, dnn_feature_columns):
    # 构建输入层，即所有特征对应的Input()层，这里使用字典的形式返回，方便后续构建模型
    dense_input_dict, sparse_input_dict = build_input_layers(linear_feature_columns + dnn_feature_columns)

    # 将linear部分的特征中sparse特征筛选出来，后面用来做1维的embedding
    linear_sparse_feature_columns = list(filter(lambda x: isinstance(x, SparseFeat), linear_feature_columns))

    # 构建模型的输入层，模型的输入层不能是字典的形式，应该将字典的形式转换成列表的形式
    # 注意：这里实际的输入与Input()层的对应，是通过模型输入时候的字典数据的key与对应name的Input层
    input_layers = list(dense_input_dict.values()) + list(sparse_input_dict.values())

    # linear_logits由两部分组成，分别是dense特征的logits和sparse特征的logits
    linear_logits = get_linear_logits(dense_input_dict, sparse_input_dict, linear_sparse_feature_columns)

    # 构建维度为k的embedding层，这里使用字典的形式返回，方便后面搭建模型
    # embedding层用户构建FM交叉部分和DNN的输入部分
    embedding_layers = build_embedding_layers(dnn_feature_columns, sparse_input_dict, is_linear=False)

    # 将输入到dnn中的所有sparse特征筛选出来
    dnn_sparse_feature_columns = list(filter(lambda x: isinstance(x, SparseFeat), dnn_feature_columns))

    fm_logits = get_fm_logits(sparse_input_dict, dnn_sparse_feature_columns, embedding_layers)  # 只考虑二阶项

    # 将所有的Embedding都拼起来，一起输入到dnn中
    dnn_logits = get_dnn_logits(sparse_input_dict, dnn_sparse_feature_columns, embedding_layers)

    # 将linear,FM,dnn的logits相加作为最终的logits
    output_logits = Add()([linear_logits, fm_logits, dnn_logits])

    # 这里的激活函数使用sigmoid
    output_layers = Activation("sigmoid")(output_logits)

    model = Model(input_layers, output_layers)
    return model


if __name__ == "__main__":
    # 读取数据
    data = pd.read_csv('./data/criteo_sample.txt')

    # 划分dense和sparse特征
    columns = data.columns.values
    dense_features = [feat for feat in columns if 'I' in feat]
    sparse_features = [feat for feat in columns if 'C' in feat]

    # 简单的数据预处理
    train_data = data_process(data, dense_features, sparse_features)
    train_data['label'] = data['label']

    # 将特征分组，分成linear部分和dnn部分(根据实际场景进行选择)，并将分组之后的特征做标记（使用DenseFeat, SparseFeat）
    linear_feature_columns = [SparseFeat(feat, vocabulary_size=data[feat].nunique(), embedding_dim=4)
                              for i, feat in enumerate(sparse_features)] + [DenseFeat(feat, 1, )
                                                                            for feat in dense_features]

    dnn_feature_columns = [SparseFeat(feat, vocabulary_size=data[feat].nunique(), embedding_dim=4)
                           for i, feat in enumerate(sparse_features)] + [DenseFeat(feat, 1, )
                                                                         for feat in dense_features]

    # 构建DeepFM模型
    history = DeepFM(linear_feature_columns, dnn_feature_columns)
    history.summary()
    history.compile(optimizer="adam",
                    loss="binary_crossentropy",
                    metrics=["binary_crossentropy", tf.keras.metrics.AUC(name='auc')])

    # 将输入数据转化成字典的形式输入
    train_model_input = {name: data[name] for name in dense_features + sparse_features}
    # 模型训练
    history.fit(train_model_input, train_data['label'].values,
                batch_size=64, epochs=5, validation_split=0.2, )