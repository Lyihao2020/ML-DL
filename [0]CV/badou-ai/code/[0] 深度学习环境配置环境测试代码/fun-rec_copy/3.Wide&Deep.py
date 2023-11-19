import tensorflow as tf
from utils import *
import pandas as pd

from tensorflow.keras.models import *
import warnings
warnings.filterwarnings("ignore")


def get_dnn_logits(dense_input_dict, sparse_input_dict, sparse_feature_columns, dnn_embedding_layers):
    concat_dense_inputs = Concatenate(axis=1)(list(dense_input_dict.values())) # B x n1 (n表示的是dense特征的维度)

    sparse_kd_embed = concat_embedding_list(sparse_feature_columns, sparse_input_dict, dnn_embedding_layers, flatten=True)

    concat_sparse_kd_embed = Concatenate(axis=1)(sparse_kd_embed) # B x n2k  (n2表示的是Sparse特征的维度)

    dnn_input = Concatenate(axis=1)([concat_dense_inputs, concat_sparse_kd_embed]) # B x (n2k + n1)

    # dnn层，这里的Dropout参数，Dense中的参数及Dense的层数都可以自己设定
    dnn_out = Dropout(0.5)(Dense(1024, activation='relu')(dnn_input))
    dnn_out = Dropout(0.3)(Dense(512, activation='relu')(dnn_out))
    dnn_out = Dropout(0.1)(Dense(256, activation='relu')(dnn_out))

    dnn_logits = Dense(1)(dnn_out)

    return dnn_logits


# Wide&Deep 模型的wide部分及Deep部分的特征选择，应该根据实际的业务场景去确定哪些特征应该放在Wide部分，哪些特征应该放在Deep部分
def WideNDeep(linear_feature_columns, dnn_feature_columns):
    # 构建输入层，即所有特征对应的Input()层，这里使用字典的形式返回，方便后续构建模型
    dense_input_dict, sparse_input_dict = build_input_layers(linear_feature_columns + dnn_feature_columns)

    # 将linear部分的特征中sparse特征筛选出来，后面用来做1维的embedding
    linear_sparse_feature_columns = list(filter(lambda x: isinstance(x, SparseFeat), linear_feature_columns))

    # 构建模型的输入层，模型的输入层不能是字典的形式，应该将字典的形式转换成列表的形式
    # 注意：这里实际的输入与Input()层的对应，是通过模型输入时候的字典数据的key与对应name的Input层
    input_layers = list(dense_input_dict.values()) + list(sparse_input_dict.values())

    # Wide&Deep模型论文中Wide部分使用的特征比较简单，并且得到的特征非常的稀疏，所以使用了FTRL优化Wide部分（这里没有实现FTRL）
    # 但是是根据他们业务进行选择的，我们这里将所有可能用到的特征都输入到Wide部分，具体的细节可以根据需求进行修改
    linear_logits = get_linear_logits(dense_input_dict, sparse_input_dict, linear_sparse_feature_columns)

    # 构建维度为k的embedding层，这里使用字典的形式返回，方便后面搭建模型
    embedding_layers = build_embedding_layers(dnn_feature_columns, sparse_input_dict, is_linear=False)

    dnn_sparse_feature_columns = list(filter(lambda x: isinstance(x, SparseFeat), dnn_feature_columns))

    # 在Wide&Deep模型中，deep部分的输入是将dense特征和embedding特征拼在一起输入到dnn中
    dnn_logits = get_dnn_logits(dense_input_dict, sparse_input_dict, dnn_sparse_feature_columns, embedding_layers)

    # 将linear,dnn的logits相加作为最终的logits
    output_logits = Add()([linear_logits, dnn_logits])

    # 这里的激活函数使用sigmoid
    output_layer = Activation("sigmoid")(output_logits)

    model = Model(input_layers, output_layer)
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
    linear_feature_columns = [SparseFeat(feat, vocabulary_size=data[feat].nunique(),embedding_dim=4)
                            for i,feat in enumerate(sparse_features)] + [DenseFeat(feat, 1,)
                            for feat in dense_features]

    dnn_feature_columns = [SparseFeat(feat, vocabulary_size=data[feat].nunique(),embedding_dim=4)
                            for i,feat in enumerate(sparse_features)] + [DenseFeat(feat, 1,)
                            for feat in dense_features]

    # 构建WideNDeep模型
    history = WideNDeep(linear_feature_columns, dnn_feature_columns)
    history.summary()
    history.compile(optimizer="adam",
                loss="binary_crossentropy",
                metrics=["binary_crossentropy", tf.keras.metrics.AUC(name='auc')])

    # 将输入数据转化成字典的形式输入
    train_model_input = {name: data[name] for name in dense_features + sparse_features}
    # 模型训练
    history.fit(train_model_input, train_data['label'].values,
            batch_size=64, epochs=5, validation_split=0.2, )