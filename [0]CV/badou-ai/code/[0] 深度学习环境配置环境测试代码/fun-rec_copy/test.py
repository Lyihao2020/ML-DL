import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import *

from sklearn.preprocessing import LabelEncoder

from utils import SparseFeat, DenseFeat
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('./data/criteo_sample.txt')
data = data.iloc[0:5, [0,1,2,3,4,14,15,16,17]]
print(data)

columns = data.columns.values
dense_features = [feat for feat in columns if 'I' in feat]  # 13
sparse_features = [feat for feat in columns if 'C' in feat]  # 26
# print(dense_features)
# print(sparse_features)


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

train_data = data_process(data, dense_features, sparse_features)
# print(train_data)
train_data['label'] = data['label']
print(train_data)

dnn_feature_columns = [SparseFeat(feat, vocabulary_size=data[feat].nunique(), embedding_dim=4)
                       for feat in sparse_features] + [DenseFeat(feat, 1)
                                                       for feat in dense_features]
print(dnn_feature_columns)


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

    sparse_features_columns = list(filter(lambda  x: isinstance(x, SparseFeat), feature_columns)) if feature_columns else []

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

dense_input_dict, sparse_input_dict = build_input_layers(dnn_feature_columns)
print("-----------------build_input_layers-------------------")
print(dense_input_dict)
print(sparse_input_dict)
input_layers = list(dense_input_dict.values()) + list(sparse_input_dict.values())
print(input_layers)
embedding_layer_dict = build_embedding_layers(dnn_feature_columns, sparse_input_dict, is_linear=False)
print("-----------------build_embedding_layers-------------------")
print(embedding_layer_dict)

dense_dnn_list = list(dense_input_dict.values())
dense_dnn_inputs = Concatenate(axis=1)(dense_dnn_list)  # B x n (n表示数值特征的数量)

