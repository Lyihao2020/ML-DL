# 基于Cora数据集的GCN节点分类
# 环境准备
import itertools
import os
import os.path as osp
import pickle
import urllib
from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sp
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init
import torch.optim as optim
###################################################################################
#                                  数据准备                                       #
###################################################################################
# 用于保存处理好的数据
Data = namedtuple('Data', ['x', 'y', 'adjacency', 'train_mask', 'val_mask', 'test_mask'])


class CoraData(object):
    download_url = "http://github.com/kimiyoung/planetoid/raw/master/data"
    filenames = ["ind.cora.{}".format(name) for name in ['x', 'tx', 'allx', 'y', 'ty', 'ally', 'graph', 'test.index']]

    ####################   数据准备部分: 数据下载   #######################
    def __init__(self, data_root="cora", rebuild=False):
        """
        包括数据下载、处理、加载等功能
        当数据的缓存文件存在时，将使用缓存文件，否则将下载、处理、并缓存到磁盘中
        :param data_root: string, optional
        存放数据的目录，原始数据路径为：{data_root}/raw
        :param rebuild: boolean, optional
        是否需要重新构建数据集，当设为True时，如果缓存数据存在也会重建数据
        """
        self.data_root = data_root
        save_file = osp.join(self.data_root, "processed_cora.pkl")
        if osp.exists(save_file) and not rebuild:
            print("Using Cached File: {}".format(save_file))
            self._data = pickle.load(open(save_file, 'rb'))
        else:
            self.maybe_download()
            self._data = self.process_data()
            with open(save_file, 'wb') as f:
                pickle.dump(self.data, f)
            print("Cache File: {}".format(save_file))

    @property
    def data(self):
        """
        :return: 返回Data数据对象，包括x,y,adjacency, train_mask, val_mask, test_mask
        """
        return self._data

    def maybe_download(self):
        save_path = osp.join(self.data_root, 'raw')
        for name in self.filenames:
            if not osp.exists(osp.join(save_path, name)):
                self.download_data("{}/{}".format(self.download_url, name), save_path)

    @staticmethod
    def download_data(url, save_path):
        """
        数据下载工具，当原始数据不存在时将会进行下载
        :param url: 数据下载路径
        :param save_path: 保存位置
        :return: 返回boolean类型，成功为True
        """
        if not osp.exists(save_path):
            os.makedirs(save_path)
        data = urllib.request.urlopen(url)
        filename = osp.basename(url)

        with open(osp.join(save_path, filename), 'wb') as f:
            f.write(data.read())
        return True

    ###################    数据准备部分: 数据处理    ########################
    def process_data(self):
        """
        处理数据，得到节点特征和标签，邻接矩阵，训练集、验证集以及测试集
        :return: 返回处理后的数据，格式为Data
        """
        print("Process data ......")
        _, tx, allx, y, ty, ally, graph, test_index = [self.read_data(osp.join(self.data_root, 'raw', name)) for name in
                                                       self.filenames]
        train_index = np.arange(y.shape[0])
        val_index = np.arange(y.shape[0], y.shape[0] + 500)
        sorted_test_index = sorted(test_index)

        x = np.concatenate((allx, tx), axis=0)
        y = np.concatenate((ally, ty), axis=0).argmax(axis=1)

        x[test_index] = x[sorted_test_index]
        y[test_index] = y[sorted_test_index]
        num_nodes = x.shape[0]

        train_mask = np.zeros(num_nodes, dtype=np.bool)
        val_mask = np.zeros(num_nodes, dtype=np.bool)
        test_mask = np.zeros(num_nodes, dtype=np.bool)
        train_mask[train_index] = True
        val_mask[val_index] = True
        test_mask[test_index] = True
        adjacency = self.build_adjacency(graph)
        print("Node's feature shape: ", x.shape)
        print("Node's label shape: ", y.shape)
        print("Adjacency's shape: ", adjacency.shape)
        print("Number of training nodes: ", train_mask.sum())
        print("Number of validation nodes: ", val_mask.sum())
        print("Number of test nodes: ", test_mask.sum())

        return Data(x=x, y=y, adjacency=adjacency, train_mask=train_mask, val_mask=val_mask, test_mask=test_mask)

    @staticmethod
    def build_adjacency(adj_dict):
        """
        根据邻接表创建邻接矩阵
        :param adj_dict:  输入的邻接表
        :return:  返回邻接矩阵
        """
        edge_index = []
        num_nodes = len(adj_dict)
        for src, dst in adj_dict.items():
            edge_index.extend([src, v] for v in dst)
            edge_index.extend([v, src] for v in dst)
        # 由于上述得到的结果中存在重复的边，将去删除掉
        edge_index = list(k for k, _ in itertools.groupby(sorted(edge_index)))
        edge_index = np.asarray(edge_index)
        adjacency = sp.coo_matrix((np.ones(len(edge_index)), (edge_index[:, 0], edge_index[:, 1])),
                                  shape=(num_nodes, num_nodes), dtype='float32')
        return adjacency

    @staticmethod
    def read_data(path):
        """
        使用不同的方式读取原始数据以进一步处理
        :param path: 数据路径
        :return: 返回数据内容
        """
        name = osp.basename(path)
        if name == 'ind.cora.test.index':
            out = np.genfromtxt(path, dtype='int64')
            return out
        else:
            out = pickle.load(open(path, "rb"), encoding="latin1")
            out = out.toarray() if hasattr(out, "toarray") else out
            return out


## 规范化邻接矩阵
def normalization(adjacency):
    """
    计算 L=D^-0.5 * (A+I) * D^-0.5
    :param adjacency: 邻接矩阵
    :return:
    """
    adjacency += sp.eye(adjacency.shape[0]) # 增加自连接
    degree = np.array(adjacency.sum(1))
    d_hat = sp.diags(np.power(degree, -0.5).flatten())
    return d_hat.dot(adjacency).dot(d_hat).tocoo()

###################################################################################
#                                  GCN层定义                                       #
###################################################################################
class GraphConvolution(nn.Module):
    def __init__(self, input_dim, output_dim, use_bias=True):
        """
        图卷积：L * X * \theta
        :param input_dim: int 节点输入特征的维度
        :param output_dim: int 输出特征维度
        :param use_bias: boolean 是否使用偏置
        """
        super(GraphConvolution, self).__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.use_bias = use_bias
        self.weight = nn.Parameter(torch.Tensor(input_dim, output_dim))
        if self.use_bias:
            self.bias = nn.Parameter(torch.Tensor(output_dim))
        else:
            self.register_parameter('bias', None)
        self.reset_parameters()

    def reset_parameters(self):
        init.kaiming_uniform_(self.weight)
        if self.use_bias:
            init.zeros_(self.bias)

    def forward(self, adjacency, input_feature):
        """
        邻接矩阵是稀疏矩阵，因此在计算时使用稀疏矩阵乘法
        :param adjacency:  邻接矩阵
        :param input_feature:  输入特征
        :return:
        """
        support = torch.mm(input_feature, self.weight)
        output = torch.sparse.mm(adjacency, support)
        if self.use_bias:
            output+=self.bias
        return output

###################################################################################
#                                  定义两层GCN模型                                  #
###################################################################################
class GcnNet(nn.Module):
    """
    定义一个包含两层GraphConvolution的模型
    """
    def __init__(self, input_dim=1433):
        super(GcnNet, self).__init__()
        self.gcn1 = GraphConvolution(input_dim,16)
        self.gcn2 = GraphConvolution(16,7)

    def forward(self, adjacency, feature):
        h = F.relu(self.gcn1(adjacency, feature))
        logits = self.gcn2(adjacency, h)
        return logits


# 超参数设置
learning_rate = 0.1
weight_decay = 5e-4
epochs = 200
# 模型定义，包括模型实例化、损失函数与优化器定义
device = "cuda" if torch.cuda.is_available() else "cpu"
model = GcnNet().to(device)
# 损失函数使用交叉熵
criterion = nn.CrossEntropyLoss().to(device)
# 优化器使用Adam
optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=weight_decay)


# 加载数据，并转换为torch.Tensor
dataset = CoraData().data
x = dataset.x/dataset.x.sum(1,keepdims=True)  # 归一化数据，使得每一行和为1
tensor_x = torch.from_numpy(x).to(device)
tensor_y = torch.from_numpy(dataset.y).to(device)
tensor_train_mask = torch.from_numpy(dataset.train_mask).to(device)
tensor_val_mask = torch.from_numpy(dataset.val_mask).to(device)
tensor_test_mask = torch.from_numpy(dataset.test_mask).to(device)

normalize_adjacency = normalization(dataset.adjacency)  # 规范化邻接矩阵
indices= torch.from_numpy(np.asarray([normalize_adjacency.row, normalize_adjacency.col]).astype('int64')).long()
values = torch.from_numpy(normalize_adjacency.data.astype(np.float32))
tensor_adjacency = torch.sparse.FloatTensor(indices,values,(2708,2708)).to(device)


###################################################################################
#                                模型训练与测试                                     #
###################################################################################
def train():
    loss_history = []
    train_acc_history = []
    val_acc_history = []

    model.train()
    train_y = tensor_y[tensor_train_mask]
    for epoch in range(epochs):
        logits = model(tensor_adjacency, tensor_x)  # 前向传播
        train_mask_logits = logits[tensor_train_mask]  # 只选择训练节点进行监督
        loss = criterion(train_mask_logits, train_y)  # 计算损失值
        optimizer.zero_grad()
        loss.backward()  # 反向传播计算参数的梯度
        optimizer.step()  # 使用优化方法进行梯度更新
        train_acc, _, _ = test(tensor_train_mask)  # 计算当前模型在训练集上的准确率
        val_acc, _, _ = test(tensor_val_mask)  # 计算当前模型在验证集上的准确率

        # 记录训练过程中损失值和准确率的变化，用于画图
        loss_history.append(loss.item())
        train_acc_history.append(train_acc.item())
        val_acc_history.append(val_acc.item())

        print("Epoch {:03d}: Loss {:.4f}, TrainAcc {:.4f}, ValAcc {:.4f}".format(epoch, loss.item(), train_acc.item(),
                                                                                 val_acc.item()))

    return loss_history, train_acc_history, val_acc_history


def test(mask):
    model.eval()
    with torch.no_grad():
        logits = model(tensor_adjacency, tensor_x)
        test_mask_logits = logits[mask]
        predict_y = test_mask_logits.max(1)[1]
        accuracy = torch.eq(predict_y, tensor_y[mask]).float().mean()
    return accuracy, test_mask_logits.cpu().numpy(), tensor_y[mask].cpu().numpy()


def plot_loss_with_acc(loss_history, val_acc_history):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(range(len(loss_history)), loss_history, c=np.array([255, 71, 90]) / 255.)
    plt.ylabel('Loss')

    ax2 = fig.add_subplot(111, sharex=ax1, frameon=False)
    ax2.plot(range(len(val_acc_history)), val_acc_history, c=np.array([79, 179, 255]) / 255.)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")
    plt.ylabel('ValAcc')

    plt.xlabel('Epoch')
    plt.title('Training Loss & Validation Accuracy')
    plt.show()

############# 开始训练 ###################
print('='*50)
print('开始训练')
loss, train_acc, val_acc = train() # 每个epoch模型在训练集上的loss，测试集上的准确率以及验证集上的准确率

# 计算最后训练好的模型在测试集上准确率
test_acc, test_logits, test_label = test(tensor_test_mask)
print('Test Accuracy: {:.4f}'.format(test_acc.item()))

# 可视化结果
plot_loss_with_acc(loss,val_acc)

# 绘制测试数据的TSNE降维图
from sklearn.manifold import TSNE
tsne = TSNE()
out = tsne.fit_transform(test_logits)
fig = plt.figure()
for i in range(7):
    indices = test_label == i
    x, y = out[indices].T
    plt.scatter(x, y, label=str(i))
plt.legend()
plt.show()
