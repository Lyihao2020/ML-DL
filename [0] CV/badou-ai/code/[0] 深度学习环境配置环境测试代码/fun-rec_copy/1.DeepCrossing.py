import tensorflow as tf
from utils import *
import pandas as pd
from tensorflow.keras.models import *
import warnings
warnings.filterwarnings("ignore")



# DNN残差块的定义
class ResidualBlock(Layer):
    def __init__(self, units):  # units表示的是DNN隐藏层神经元数量
        super(ResidualBlock, self).__init__()
        self.units = units

    def build(self, input_shape):
        out_dim = input_shape[-1]
        self.dnn1 = Dense(self.units, activation='relu')
        self.dnn2 = Dense(out_dim, activation='relu')  # 保证输入的维度和输出的维度一致才能进行残差连接

    def call(self, inputs):
        x = inputs
        x = self.dnn1(x)
        x = self.dnn2(x)
        x = Activation('relu')(x + inputs)  # 残差操作
        return x


# block_nums表示DNN残差块的数量
def get_dnn_logits(dnn_inputs, block_nums=3):
    dnn_out = dnn_inputs
    for i in range(block_nums):
        dnn_out = ResidualBlock(64)(dnn_out)

    # 将dnn的输出转化成logits
    # 利用sigmoid函数将residual层的输出转化为0 - 1之间的概率值
    dnn_logits = Dense(1, activation='sigmoid')(dnn_out)  # 相当于Scoring层

    return dnn_logits

def DeepCrossing(dnn_feature_columns):
    # 构建输入层，即所有特征对应的Input()层，这里使用字典的形式返回，方便后续构建模型
    dense_input_dict, sparse_input_dict = build_input_layers(dnn_feature_columns)
    # 构建模型的输入层，模型的输入层不能是字典的形式，应该将字典的形式转换成列表的形式
    # 注意：这里实际的输入与Input()层的对应，是通过模型输入时候的字典数据的key与对应name的Input层
    input_layers = list(dense_input_dict.values()) + list(sparse_input_dict.values())

    # 构建维度为k的embedding层，这里使用字典的形式返回，方便后面搭建模型
    embedding_layer_dict = build_embedding_layers(dnn_feature_columns, sparse_input_dict, is_linear=False)

    # 将所有的dense特征拼接到一起
    dense_dnn_list = list(dense_input_dict.values())
    dense_dnn_inputs = Concatenate(axis=1)(dense_dnn_list)  # B x n (n表示数值特征的数量)

    # 因为需要将其与dense特征拼接到一起所以需要Flatten，不进行Flatten的Embedding层输出的维度为：Bx1xdim
    sparse_dnn_list = concat_embedding_list(dnn_feature_columns, sparse_input_dict, embedding_layer_dict, flatten=True)

    sparse_dnn_inputs = Concatenate(axis=1)(sparse_dnn_list)  # B x m*dim (n表示类别特征的数量，dim表示embedding的维度)

    # 将dense特征和Sparse特征拼接到一起
    dnn_inputs = Concatenate(axis=1)([dense_dnn_inputs, sparse_dnn_inputs])  # B x (n + m*dim)

    # 输入到dnn中，需要提前定义需要几个残差块
    output_layer = get_dnn_logits(dnn_inputs, block_nums=3)

    model = Model(input_layers, output_layer)
    return model



if __name__ == "__main__":
    # 读取数据,13个数值型特征，26个类别型特征
    data = pd.read_csv('./data/criteo_sample.txt')

    columns = data.columns.values  # 拿到40个列名
    dense_features = [feat for feat in columns if 'I' in feat]  # 13
    sparse_features = [feat for feat in columns if 'C' in feat]  # 26

    # 数据处理
    train_data = data_process(data, dense_features, sparse_features)

    train_data['label'] = data['label']  # 加上label列

    dnn_feature_columns = [SparseFeat(feat, vocabulary_size=data[feat].nunique(), embedding_dim=4)
                           for feat in sparse_features] + [DenseFeat(feat, 1)
                           for feat in dense_features]

    # 开始构建DeepCrossing模型
    history = DeepCrossing(dnn_feature_columns)

    history.summary()
    history.compile(optimizer="adam",
                    loss="binary_crossentropy",
                    metrics=["binary_crossentropy", tf.keras.metrics.AUC(name='auc')])

    # 将输入数据转化成字典的形式输入
    train_model_input = {name: data[name] for name in dense_features + sparse_features}
    # 模型训练
    history.fit(train_model_input, train_data['label'].values,
            batch_size=64, epochs=20, validation_split=0.2, )