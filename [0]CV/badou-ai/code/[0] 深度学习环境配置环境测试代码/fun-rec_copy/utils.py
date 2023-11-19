from collections import namedtuple
from tensorflow.keras.layers import *
import numpy as np
from sklearn.preprocessing import LabelEncoder


class SparseFeat(namedtuple('SparseFeat', ['name', 'vocabulary_size', 'embedding_dim'])):
    __slots__ = ()

    def __new__(cls, name, vocabulary_size, embedding_dim=4):
        return super(SparseFeat, cls).__new__(cls, name, vocabulary_size, embedding_dim)


class DenseFeat(namedtuple('DenseFeat', ['name', 'dimension'])):
    __slots__ = ()

    def __new__(cls, name, dimension=1):
        return super(DenseFeat, cls).__new__(cls, name, dimension)


class VarLenSparseFeat(namedtuple('VarLenSparseFeat', ['name', 'vocabulary_size', 'embedding_dim', 'maxlen'])):
    __slots__ = ()

    def __new__(cls,  name, vocabulary_size, embedding_dim=4, maxlen=50):
        return super(VarLenSparseFeat, cls).__new__(cls,  name, vocabulary_size, embedding_dim, maxlen)


def data_process(data_df, dense_features, sparse_features):
    data_df[dense_features] = data_df[dense_features].fillna(0.0)
    for f in dense_features:
        # lambda表达式
        # apply() 沿DataFrame的轴应用功能，axis默认为0
        data_df[f] = data_df[f].apply(lambda x: np.log(x+1) if x > -1 else -1)

    data_df[sparse_features] = data_df[sparse_features].fillna("-1")
    for f in sparse_features:
        lbe = LabelEncoder()
        # 对数据先进行拟合，再进行标准化
        data_df[f] = lbe.fit_transform(data_df[f])

    return data_df[dense_features + sparse_features]


def build_input_layers(feature_columns):
    dense_input_dict, spares_input_dict = {}, {}

    for fc in feature_columns:
        if isinstance(fc, SparseFeat):
            spares_input_dict[fc.name] = Input(shape=(1, ), name=fc.name)
        elif isinstance(fc, DenseFeat):
            dense_input_dict[fc.name] = Input(shape=(fc.dimension, ), name=fc.name)

    return dense_input_dict, spares_input_dict


def build_embedding_layers(feature_columns, input_layers_dict, is_linear):
    embedding_layers_dict = dict()

    sparse_features_columns = list(filter(lambda x: isinstance(x, SparseFeat), feature_columns)) if feature_columns else []

    if is_linear:
        for fc in sparse_features_columns:
            embedding_layers_dict[fc.name] = Embedding(fc.vocabulary_size + 1, 1, name='1d_emb_' + fc.name)
    else:
        for fc in sparse_features_columns:
            embedding_layers_dict[fc.name] = Embedding(fc.vocabulary_size + 1, fc.embedding_dim, name='kd_emb_' + fc.name)

    return embedding_layers_dict


def concat_embedding_list(feature_columns, input_layer_dict, embedding_layer_dict, flatten=False):
    # 将sparse特征筛选出来
    sparse_feature_columns = list(filter(lambda x: isinstance(x, SparseFeat), feature_columns))

    embedding_list = []
    for fc in sparse_feature_columns:
        _input = input_layer_dict[fc.name]  # 获取输入层
        _embed = embedding_layer_dict[fc.name]  # B x 1 x dim  获取对应的embedding层
        embed = _embed(_input)  # B x dim  将input层输入到embedding层中

        # 是否需要flatten, 如果embedding列表最终是直接输入到Dense层中，需要进行Flatten，否则不需要
        if flatten:
            embed = Flatten()(embed)

        embedding_list.append(embed)

    return embedding_list


def get_linear_logits(dense_input_dict, sparse_input_dict, sparse_feature_columns):
    # 将所有的dense特征的Input层，然后经过一个全连接层得到dense特征的logits
    concat_dense_inputs = Concatenate(axis=1)(list(dense_input_dict.values()))
    dense_logits_output = Dense(1)(concat_dense_inputs)

    # 获取linear部分sparse特征的embedding层，这里使用embedding的原因是：
    # 对于linear部分直接将特征进行onehot然后通过一个全连接层，当维度特别大的时候，计算比较慢
    # 使用embedding层的好处就是可以通过查表的方式获取到哪些非零的元素对应的权重，然后在将这些权重相加，效率比较高
    linear_embedding_layers = build_embedding_layers(sparse_feature_columns, sparse_input_dict, is_linear=True)

    # 将一维的embedding拼接，注意这里需要使用一个Flatten层，使维度对应
    sparse_1d_embed = []
    for fc in sparse_feature_columns:
        feat_input = sparse_input_dict[fc.name]
        embed = Flatten()(linear_embedding_layers[fc.name](feat_input))
        sparse_1d_embed.append(embed)

    # embedding中查询得到的权重就是对应onehot向量中一个位置的权重，所以后面不用再接一个全连接了，本身一维的embedding就相当于全连接
    # 只不过是这里的输入特征只有0和1，所以直接向非零元素对应的权重相加就等同于进行了全连接操作(非零元素部分乘的是1)
    sparse_logits_output = Add()(sparse_1d_embed)

    # 最终将dense特征和sparse特征对应的logits相加，得到最终linear的logits
    linear_part = Add()([dense_logits_output, sparse_logits_output])
    return linear_part


# 输入层拼接成列表
def concat_input_list(input_list):
    feature_nums = len(input_list)
    if feature_nums > 1:
        return Concatenate(axis=1)(input_list)
    elif feature_nums == 1:
        return input_list[0]
    else:
        return None

# 从所有稀疏特征列中查询指定稀疏特征列的embedding矩阵，字典形式返回
def embedding_lookup(feature_columns, input_layer_dict, embedding_layer_dict):
    embedding_list = []

    for fc in feature_columns:
        _input = input_layer_dict[fc]
        _embed = embedding_layer_dict[fc]
        embed = _embed(_input)
        embedding_list.append(embed)

    return embedding_list





