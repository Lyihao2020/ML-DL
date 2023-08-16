# Pandas
"""
Numpy 在向量化的数值计算中表现优异
但是在处理更灵活、复杂的数据任务：

如为数据添加标签、处理缺失值、分组和透视表等方面

Numpy显得力不从心

而基于Numpy构建的Pandas库，提供了使得数据分析变得更快更简单的高级数据结构和操作工具

"""
print("-------------------------------------")
print("-------------------------------------")

# 对象创建
# Pandas Series对象
# Series 是带标签数据的一维数组
"""
Series对象的创建
通用结构: pd.Series(data, index=index, dtype=dtype)
  
data：数据，可以是列表，字典或Numpy数组
  
index：索引，为可选参数

dtype: 数据类型，为可选参数
"""

# 用列表创建
# index缺省，默认为整数序列
import pandas as pd

data = pd.Series([1.5, 3, 4.5, 6])
print(data)

# 增加 index
data = pd.Series([1.5, 3, 4.5, 6], index=["a", "b", "c", "d"])
print(data)

# 增加数据类型，缺省则为自动判断
data = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"], dtype="float")
print(data)

# 注意：数据支持多种类型
data = pd.Series([1, 2, "3", 4], index=["a", "b", "c", "d"])
print(data)
print(data["a"])
print(data["c"])

# 数据类型可被强制改变
data = pd.Series([1, 2, "3", 4], index=["a", "b", "c", "d"], dtype=float)
print(data)
print(data["a"])
print(data["c"])

# ValueError: could not convert string to float: 'a'
try:
    data = pd.Series([1, 2, "a", 4], index=["a", "b", "c", "d"], dtype=float)
    print(data)
except ValueError as e:
    print(e)

print("-------------------------------------")

# 用一维numpy数组创建
import numpy as np

x = np.arange(5)
data = pd.Series(x)
print(data)

print("-------------------------------------")

# 用字典创建
# 默认以键为index 值为data
population_dict = {"BeiJing": 2154,
                   "ShangHai": 2424,
                   "ShenZhen": 1303,
                   "HangZhou": 981 }
population = pd.Series(population_dict)
print(population)

# 字典创建，如果指定index，则会到字典的键中筛选，找不到的，值设为NaN
population = pd.Series(population_dict, index=["BeiJing", "HangZhou", "c", "d"])
print(population)

print("-------------------------------------")

# data为标量的情况
data = pd.Series(5, index=[100, 200, 300])
print(data)

print("-------------------------------------")

# Pandas DataFrame对象
"""
DataFrame 是带标签数据的多维数组
DataFrame对象的创建
通用结构: pd.DataFrame(data, index=index, columns=columns)
data：数据，可以是列表，字典或Numpy数组
index：索引，为可选参数
columns: 列标签，为可选参数
"""

# 通过Series对象创建
population_dict = {"BeiJing": 2154,
                   "ShangHai": 2424,
                   "ShenZhen": 1303,
                   "HangZhou": 981 }

population = pd.Series(population_dict)
population_DataFrame = pd.DataFrame(population, columns=["population"])
print(population_DataFrame)

print("-------------------------------------")

# 通过Series对象字典创建
GDP_dict = {"BeiJing": 30320,
            "ShangHai": 32680,
            "ShenZhen": 24222,
            "HangZhou": 13468 }

GDP = pd.Series(GDP_dict)
print(GDP)
Area_DataFrame = pd.DataFrame({"population": population, "GDP": GDP})
print(Area_DataFrame)

print("-------------------------------------")

# 注意：数量不够的会自动补齐
Area_DataFrame = pd.DataFrame({"population": population, "GDP": GDP, "Country": "China"})
print(Area_DataFrame)

print("-------------------------------------")

# 通过字典列表对象创建
# 字典索引作为index，字典键作为columns
import numpy as np
import pandas as pd

data = [{"a": i, "b": 2*i} for i in range(3)]
print(data)
data = pd.DataFrame(data)
print(data)
# 深拷贝，不会改变原来的值
data1 = data["a"].copy()
print(data1)
data1[0] = 10
print(data1)
print(data)

print("-------------------------------------")

# 不存在的键，会默认值为NaN
data = [{"a": 1, "b":1},{"b": 3, "c":4}]
print(data)
data = pd.DataFrame(data)
print(data)

print("-------------------------------------")

# 通过Numpy二维数组创建
data = np.random.randint(10, size=(3, 2))
print(data)
data = pd.DataFrame(data, columns=["foo", "bar"], index=["a", "b", "c"])
print(data)

print("-------------------------------------")

# DataFrame性质
# 属性
data = pd.DataFrame({"pop": population, "GDP": GDP})
print(data)

# df.values  返回numpy数组表示的数据
print(data.values)

# df.index 返回行索引
print(data.index)

# df.columns 返回列索引
print(data.columns)

# df.shape  形状
print(data.shape)

# pd.size 大小
print(data.size)

# pd.dtypes 返回每列数据类型
print(data.dtypes)

print("-------------------------------------")

# 索引
print(data)
# 获取列，字典式
print(data["pop"])
print(data[["GDP", "pop"]])
# 获取列，对象属性式
print(data.GDP)

print("-------------------------------------")

# 获取行，绝对索引 df.loc
print(data)
print(data.loc["BeiJing"])
print(data.loc[["BeiJing", "HangZhou"]])
# 获取行，相对索引 df.iloc
print(data.iloc[0])
print(data.iloc[[1, 3]])

print("-------------------------------------")

# 获取标量
print(data)
print(data.loc["BeiJing", "GDP"])
print(data.iloc[0, 1])
print(data.values[0][1])

print("-------------------------------------")

# Series对象的索引
print(type(data.GDP))
print(GDP)
print(GDP["BeiJing"])

print("-------------------------------------")

# 切片
dates = pd.date_range(start='2019-01-01', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=["A", "B", "C", "D"])
print(df)
"""
上述代码创建了一个日期范围，从'2019-01-01'开始，共有6个时间点。
通过使用'pd.date_range()'函数，我们可以生成一个包含指定时间间隔的日期序列。
最后，使用'print(dates)'语句将日期序列打印出来。

输出中的"freq"表示日期序列的频率。
在这个例子中，"D"代表天，表示日期序列的间隔为每天。
因此，日期序列中的日期按每天递增。"""

# 行切片
print(df["2019-01-01": "2019-01-03"])
print(df.loc["2019-01-01": "2019-01-03"])
print(df.iloc[0: 3])
# 列切片
print(df.loc[:, "A": "C"])
print(df.iloc[:, 0: 3])
# 多种多样的取值
# 行、列同时切片
print(df.loc["2019-01-02": "2019-01-03", "C":"D"])
print(df.iloc[1: 3, 2:])
# 行切片，列分散取值
print(df.loc["2019-01-04": "2019-01-06", ["A", "C"]])
print(df.iloc[3:, [0, 2]])
# 行分散取值，列切片
print(df.loc[["2019-01-02", "2019-01-06"], "C": "D"])
print(df.iloc[[1, 5], 0: 3])
# 行、列均分散取值
print(df.loc[["2019-01-04", "2019-01-06"], ["A", "D"]])
print(df.iloc[[1, 5], [0, 3]])

print("-------------------------------------")

# 布尔索引
print(df)
print(df > 0)
print(df[df > 0])
print(df.A > 0)
print(df[df.A > 0])

print("-------------------------------------")

# isin()方法
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df)

ind = df2["E"].isin(["two", "four"])
print(ind)
print(df2)
print(df2[ind])

print("-------------------------------------")

# 赋值
print(df)
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20190101', periods=6))
print(s1)
df["E"] = s1
print(df)

# 修改赋值
df.loc["2019-01-01", "A"] = 0
print(df)
df.iloc[0, 1] = 0
print(df)
df["D"] = np.array([5]*len(df))   # 可简化成df["D"] = 5
print(df)

# 修改index和columns
df.index = [i for i in range(len(df))]
print(df)
df.columns = [i for i in range(df.shape[1])]
print(df)

print("-------------------------------------")

# 数值运算和统计分析
# 数据的查看
import pandas as pd
import  numpy as np

# np.random.randn是NumPy库中的一个函数，
# 用于产生标准正态分布（均值为0，方差为1）的随机数。
# 它可以产生一个或多个符合标准正态分布的随机数，
# 这些随机数被分布在整个实数轴上。

dates = pd.date_range(start='2019-01-01', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=["A", "B", "C", "D"])
print(df)

# 查看前面的行
print(df.head())    # 默认5行
print(df.head(2))

# 查看后面的行
print(df.tail())    # 默认5行
print(df.tail(3))

# 查看总体信息
df.iloc[0, 3] = np.nan
print(df)
print(df.info())

print("-------------------------------------")

# Numpy通用函数同样适用于Pandas
# 向量化运算
x = pd.DataFrame(np.arange(4).reshape(1, 4))
print(x)
print(x+5)
print(np.exp(x))
print(x)
y = pd.DataFrame(np.arange(4,8).reshape(1, 4))
print(y)
print(x*y)

# 矩阵化运算
# 这段代码的作用是生成一个30行30列的DataFrame对象x，其中的元素值是0到9之间的随机整数。
#
# 首先，通过`np.random.seed(42)`设置了随机数生成器的种子为42，这样可以确保结果的可重复性。
#
# 然后，通过`np.random.randint(10, size=(30, 30))`生成一个30行30列的数组，其中的元素值是0到9之间的随机整数。
#
# 最后，将生成的数组作为参数传入`pd.DataFrame()`函数中，创建一个DataFrame对象x。
#
# 最后，通过`print(x)`语句将DataFrame对象x打印输出。

np.random.seed(42)
x = pd.DataFrame(np.random.randint(10, size=(30, 30)))
print(x)

# 随机数生成器的种子数是一个初始值，用于确定随机数序列的起始点。种子数的大小非常重要，因为它决定了随机数序列的周期性和可预测性。
#
# 如果使用相同的种子数，每次运行生成的随机数序列将完全相同。这在某些情况下是有用的，例如需要重现实验结果。然而，在其他情况下，预测性的随机数序列可能会导致安全问题或算法中的偏差。
#
# 要设置种子数的大小，需要考虑以下几点：
# 1. 唯一性：如果需要生成唯一的随机数序列，可以使用当前的时间戳或其他独一无二的值作为种子数。
# 2. 预测性：如果需要可预测性较强的随机数序列，可以使用相同的种子数。
# 3. 安全性：如果需要安全的随机数序列，种子数应尽量随机，并且不可被猜测。可以使用硬件随机数生成器、密码学安全伪随机数生成器等来生成随机的种子数。

# 转置
z = x.T
print(z)
np.random.seed(1)
y = pd.DataFrame(np.random.randint(10, size=(30, 30)))
print(y)

import timeit

code_to_test = """
x.dot(y)
"""

# 将 globals 参数设置为 globals()，以便在计时期间可以访问该函数。
execution_time = timeit.timeit(code_to_test, globals=globals(), number=100)
print(f"Execution time 00 : {execution_time} seconds")

code_to_test = """
np.dot(x, y)
"""

# 将 globals 参数设置为 globals()，以便在计时期间可以访问该函数。
execution_time = timeit.timeit(code_to_test, globals=globals(), number=100)
print(f"Execution time 01: {execution_time} seconds")

# 执行相同运算，Numpy与Pandas的对比
x1 = np.array(x)
print(x1)
y1 = np.array(y)
print(y)
code_to_test = """
x1.dot(y1)
"""

# 将 globals 参数设置为 globals()，以便在计时期间可以访问该函数。
execution_time = timeit.timeit(code_to_test, globals=globals(), number=100)
print(f"Execution time 00 : {execution_time} seconds")

code_to_test = """
np.dot(x1, y1)
"""

# 将 globals 参数设置为 globals()，以便在计时期间可以访问该函数。
execution_time = timeit.timeit(code_to_test, globals=globals(), number=100)
print(f"Execution time 01 : {execution_time} seconds")

code_to_test = """
np.dot(x.values, y.values)
"""

# 将 globals 参数设置为 globals()，以便在计时期间可以访问该函数。
execution_time = timeit.timeit(code_to_test, globals=globals(), number=100)
print(f"Execution time 02 : {execution_time} seconds")

print("-------------------------------------")

x2 = list(x1)
print(x2)
y2 = list(y1)
print(y2)
x3 = []
y3 = []
for i in x2:
    res = []
    for j in i:
        res.append(int(j))
    x3.append(res)
for i in y2:
    res = []
    for j in i:
        res.append(int(j))
    y3.append(res)
print(x3)
print(y3)

def f(x, y):
    res = []
    for i in range(len(x)):
        row = []
        for j in range(len(y[0])):
            sum_row = 0
            for k in range(len(x[0])):
                sum_row += x[i][k]*y[k][j]
            row.append(sum_row)
        res.append(row)
    return res

code_to_test = """
f(x3, y3)
"""

# 将 globals 参数设置为 globals()，以便在计时期间可以访问该函数。
execution_time = timeit.timeit(code_to_test, globals=globals(), number=100)
print(f"Execution time 03 : {execution_time} seconds")

# 一般来说，纯粹的计算在Numpy里执行的更快
# Numpy更偏重于计算，Pandas更侧重于数据处理

print("-------------------------------------")

# 广播运算
np.random.seed(42)
x = pd.DataFrame(np.random.randint(10, size=(3, 3)), columns=list("ABC"))
print(x)

# 按行广播
print(x.iloc[0])
print(x/x.iloc[0])
print(x.div(x.iloc[0], axis=1))

# 按列广播
print(x.A)
print(x.div(x.A, axis=0))

print("-------------------------------------")

# 新用法
# 索引对齐
A = pd.DataFrame(np.random.randint(0, 20, size=(2, 2)), columns=list("AB"))
print(A)
B = pd.DataFrame(np.random.randint(0, 10, size=(3, 3)), columns=list("ABC"))
print(B)

# pandas会自动对齐两个对象的索引，没有的值用np.nan表示
print(A+B)

# 缺省值也可用fill_value来填充
print(A.add(B, fill_value=0))
print(A*B)

# 统计相关
# 数据种类统计
y = np.random.randint(3, size=20)
print(y)
print(np.unique(y))

from collections import Counter
print(Counter(y))

y1 = pd.DataFrame(y, columns=["A"])
print(y1)

print(np.unique(y1))
print(y1["A"].value_counts())

print("-------------------------------------")

# 产生新的结果，并进行排序
population_dict = {"BeiJing": 2154,
                   "ShangHai": 2424,
                   "ShenZhen": 1303,
                   "HangZhou": 981 }
population = pd.Series(population_dict)

GDP_dict = {"BeiJing": 30320,
            "ShangHai": 32680,
            "ShenZhen": 24222,
            "HangZhou": 13468 }
GDP = pd.Series(GDP_dict)

city_info = pd.DataFrame({"population": population,"GDP": GDP})
print(city_info)
city_info["per_GDP"] = city_info["GDP"]/city_info["population"]
print(city_info)

# 递增排序
print(city_info.sort_values(by="per_GDP"))
print(city_info.sort_values(by="per_GDP", ascending=False))

# 按轴进行排序
data = pd.DataFrame(np.random.randint(20, size=(3, 4)), index=[2, 1, 0], columns=list("CBAD"))
print(data)

# 行排序
print(data.sort_index())

# 列排序
print(data.sort_index(axis=1))
print(data.sort_index(axis=1, ascending=False))

# 同时进行行列排序
print(data.sort_index(axis=0, ascending=False).sort_index(axis=1, ascending=False))

# 统计方法
df = pd.DataFrame(np.random.normal(2, 4, size=(6, 4)),columns=list("ABCD"))
print(df)

# 非空个数
print(df.count())

# 求和
print(df.sum())
print(df.sum(axis=1))

# 最大值，最小值
print(df.min())
print(df.max(axis=1))
print(df)
print(df.idxmax())

# 均值
print(df.mean())

# 方差
print(df.var())

# 标准差
print(df.std())

# 中位数
print(df.median())

# 众数
data = pd.DataFrame(np.random.randint(5, size=(10, 2)), columns=list("AB"))
print(data)
print(data.mode())

# 75%分位数
print(df.quantile(0.75))

# 一网打尽
print(df.describe())
data_2 = pd.DataFrame([["a", "a", "c", "d"],
                       ["c", "a", "c", "b"],
                       ["a", "a", "d", "c"]], columns=list("ABCD"))
print(data_2.describe())

# 相关系数和协方差
print(df.corr())
print(df.corrwith(df["A"]))

print("-------------------------------------")

# 自定义输出
# apply（method）的用法：使用method方法默认对每一列进行相应的操作
print(df)
# 这行代码是在对DataFrame中的每一列进行累加求和操作。
# np.cumsum是NumPy库中的函数，用于计算数组元素的累加和。
# df.apply(np.cumsum)将该函数应用到DataFrame的每一列上。
# 输出的结果是每一列都进行了累加求和的新的DataFrame。
print(df.apply(np.cumsum))
print(df.apply(np.cumsum, axis=1))
print(df.apply(sum))
print(df.sum())
print(df.apply(lambda x: x.max()-x.min()))
def my_describe(x):
    return pd.Series([x.count(), x.mean(), x.max(), x.idxmin(), x.std()], \
                     index=["Count", "mean", "max", "idxmin", "std"])
print(df.apply(my_describe))

print("-------------------------------------")

# 缺失值处理
# 发现缺失值
import pandas as pd
import numpy as np

data = pd.DataFrame(np.array([[1, np.nan, 2],
                              [np.nan, 3, 4],
                              [5, 6, None]]), columns=["A", "B", "C"])
print(data)

# 注意：有None、字符串等，数据类型全部变为object，它比int和float更消耗资源
print(data.dtypes)
print(data.isnull())
print(data.notnull())

# 删除缺失值
data = pd.DataFrame(np.array([[1, np.nan, 2, 3],
                              [np.nan, 4, 5, 6],
                              [7, 8, np.nan, 9],
                              [10, 11 , 12, 13]]), columns=["A", "B", "C", "D"])
print(data)
# 注意：np.nan是一种特殊的浮点数
print(data.dtypes)

# 删除整行(存在NAN):不改变原有的矩阵
print(data.dropna())

# 删除整列(存在NAN)：不改变原有的矩阵
print(data.dropna(axis="columns"))
print(data)

data["D"] = np.nan  # 改变
print(data)

print(data.dropna(axis="columns", how="all"))
print(data.dropna(axis="columns", how="any"))
print("-------------------------------------")

data.loc[3] = np.nan
print(data)
print(data.dropna(how="all"))

print("-------------------------------------")

# 填充缺失值
data = pd.DataFrame(np.array([[1, np.nan, 2, 3],
                              [np.nan, 4, 5, 6],
                              [7, 8, np.nan, 9],
                              [10, 11 , 12, 13]]), columns=["A", "B", "C", "D"])
print(data)
print(data.fillna(value=5)) # 不改变原有的
print(data)

print("-------------------------------------")

# 用均值进行替换
fill = data.mean()
print(fill)
print(data.fillna(value=fill))

# 下面这段代码的意思是，首先计算一个“fill”值，该值是给定数据集（data）的所有数值的平均值。
# 然后使用该“fill”值来填充数据集中的缺失值，并打印出填充后的数据集。
# stack()：这个方法用于将 DataFrame 中的列转换成行，同时创建一个层次化索引。
# 如果 data 是 Series 对象，该步骤会被忽略。
fill = data.stack().mean()
print(fill)
print(data.fillna(value=fill))

print("-------------------------------------")

# 合并数据
# 构造一个生产DataFrame的函数
import pandas as pd
import numpy as np

def make_df(cols, ind):
    "一个简单的DataFrame"
    data = {c: [str(c)+str(i) for i in ind]  for c in cols}
    return pd.DataFrame(data, ind)

print(make_df("ABC", range(3)))

# 垂直合并
df_1 = make_df("AB", [1, 2])
df_2 = make_df("AB", [3, 4])
print(df_1)
print(df_2)
print(pd.concat([df_1, df_2]))

# 水平合并
df_3 = make_df("AB", [0, 1])
df_4 = make_df("CD", [0, 1])
print(df_3)
print(df_4)
print(pd.concat([df_3, df_4], axis=1))

print("-------------------------------------")

# 索引重叠
# 行重叠
df_5 = make_df("AB", [1, 2])
df_6 = make_df("AB", [1, 2])
print(df_5)
print(df_6)
print(pd.concat([df_5, df_6]))
# ignore_index=True参数表示忽略原始索引，并在合并后的DataFrame中重新生成新的索引。
print(pd.concat([df_5, df_6],ignore_index=True))

# 列重叠
df_7 = make_df("ABC", [1, 2])
df_8 = make_df("BCD", [1, 2])
print(df_7)
print(df_8)
pd.concat([df_7, df_8], axis=1)
pd.concat([df_7, df_8],axis=1, ignore_index=True)

print("-------------------------------------")

# 对齐合并merge()
df_9 = make_df("AB", [1, 2])
df_10 = make_df("BC", [1, 2])
print(df_9)
print(df_10)
print(pd.merge(df_9, df_10))
df_9 = make_df("AB", [1, 2])
df_10 = make_df("CB", [2, 1])
print(df_9)
print(df_10)
print(pd.merge(df_9, df_10))

print("-------------------------------------")

# 合并城市信息
population_dict = {"city": ("BeiJing", "HangZhou", "ShenZhen"),
                   "pop": (2154, 981, 1303)}
population = pd.DataFrame(population_dict)
print(population)

GDP_dict = {"city": ("BeiJing", "ShangHai", "HangZhou"),
            "GDP": (30320, 32680, 13468)}
GDP = pd.DataFrame(GDP_dict)
print(GDP)

city_info = pd.merge(population, GDP)
print(city_info)

# 这段代码是将两个数据框（population和GDP）按照城市名称进行合并，并指定了合并方式为外连接（outer）
city_info = pd.merge(population, GDP, how="outer")
print(city_info)

print("-------------------------------------")

# 分组和数据透视表
df = pd.DataFrame({"key":["A", "B", "C", "C", "B", "A"],
                  "data1": range(6),
                  "data2": np.random.randint(0, 10, size=6)})
print(df)

# 分组
# 延迟计算
print(df.groupby("key"))
print(df.groupby("key").sum())
print(df.groupby("key").mean())
for i in df.groupby("key"):
    print(str(i))

# 按列取值
print(df.groupby("key")["data2"].sum())

# 按组迭代
for data, group in df.groupby("key"):
    print("{0:5} shape={1}".format(data, group.shape))

# 调用方法
print(df.groupby("key")["data1"].describe())

# 支持更复杂的操作
# 这是对DataFrame进行分组操作后进行聚合计算的方法。
print(df.groupby("key").aggregate(["min", "median", "max"]))

# 过滤
def filter_func(x):
    return x["data2"].std() > 3
print(df.groupby("key")["data2"].std())
print(df.groupby("key").filter(filter_func))

# 转换
"""
/Users/labixiaoxin/Desktop/Visionär🌊/[1] 笔记📒/ML-DL/[-1] Python/PythonSyntax/code/Advanced/08Pandas.py:820: 
FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; 
in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
  print(df.groupby("key").apply(lambda x: x-x.mean()))
print(df)
print(df.groupby("key").transform(lambda x: x-x.mean()))
# 这个报错是因为在将DataFrame分组后进行聚合操作之前，'key'列被自动排除在外。
# 可以通过只选择有效列来解决这个问题。具体来说，在调用apply之前，可以先选择除'key'列之外的所有列。
print(df)
print(df.groupby("key").apply(lambda x: x-x.mean()))
"""
print(df)
print(df.groupby("key").transform(lambda x: x-x.mean()))
print(df)
try:
    print(df.groupby("key").apply(lambda x: x-x.mean()))
except TypeError as e:
    print(e)
print(df)
# 正确的做法
print(df.groupby("key").apply(lambda x: x[x.columns.difference(["key"])] - x[x.columns.difference(["key"])].mean()))

# apply（）方法
print(df)
def norm_by_data2(x):
    x["data1"] /= x["data2"].sum()
    return x
print(df.groupby("key").apply(norm_by_data2))

# 将列表、数组设为分组键
L = [0, 1, 0, 1, 2, 0]
print(df)
print(df.groupby(L).sum())

# 用字典将索引映射到分组
df2 = df.set_index("key")
print(df2)
mapping = {"A": "first", "B": "constant", "C": "constant"}
print(df2.groupby(mapping).sum())

# 任意Python函数
print(df2.groupby(str.lower).mean())

# 多个有效值组成的列表
print(df2.groupby([str.lower, mapping]).mean())

print("-------------------------------------")

# 其他
# 1）向量化字符串操作
# 2） 处理时间序列
# 3） 多级索引：用于多维数据
base_data = np.array([[1771, 11115 ],
                      [2154, 30320],
                      [2141, 14070],
                      [2424, 32680],
                      [1077, 7806],
                      [1303, 24222],
                      [798, 4789],
                      [981, 13468]])
data = pd.DataFrame(base_data, index=[["BeiJing","BeiJing","ShangHai","ShangHai","ShenZhen","ShenZhen","HangZhou","HangZhou"]\
                                     , [2008, 2018]*4], columns=["population", "GDP"])
print(data)
data.index.names = ["city", "year"]
print(data)
print(data["GDP"])
print(data.loc["ShangHai", "GDP"])
print(data.loc["ShangHai", 2018]["GDP"])
# 4） 高性能的Pandas：eval（）
df1, df2, df3, df4 = (pd.DataFrame(np.random.random((10000,100))) for i in range(4))
# %timeit (df1+df2)/(df3+df4)
# 减少了复合代数式计算中间过程的内存分配
# %timeit pd.eval("(df1+df2)/(df3+df4)")
print(np.allclose((df1+df2)/(df3+df4), pd.eval("(df1+df2)/(df3+df4)")))
# 实现列间运算
df = pd.DataFrame(np.random.random((1000, 3)), columns=list("ABC"))
df.head()
res_1 = pd.eval("(df.A+df.B)/(df.C-1)")
res_2 = df.eval("(A+B)/(C-1)")
np.allclose(res_1, res_2)
df["D"] = pd.eval("(df.A+df.B)/(df.C-1)")
print(df.head())
df.eval("D=(A+B)/(C-1)", inplace=True)
df.head()
# 使用局部变量
column_mean = df.mean(axis=1)
res = df.eval("A+@column_mean")
res.head()
# 4） 高性能的Pandas：query（）
df.head()
# %timeit df[(df.A < 0.5) & (df.B > 0.5)]
# %timeit df.query("(A < 0.5)&(B > 0.5)")
df.query("(A < 0.5)&(B > 0.5)").head()
np.allclose(df[(df.A < 0.5) & (df.B > 0.5)], df.query("(A < 0.5)&(B > 0.5)"))
# 5）eval（）和query（）的使用时机**
# 小数组时，普通方法反而更快
print(df.values.nbytes)
print(df1.values.nbytes)
print("-------------------------------------")
print("-------------------------------------")
