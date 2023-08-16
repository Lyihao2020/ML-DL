# Numpy
# 为什么要用 Numpy
# Python for循环 低效
# 求 100万 个数的倒数
import time

def compute_reciprocals(values):
    res = []
    for value in values:
        res.append(1/value)
    return res

values = list(range(1, 1000000))
start_time = time.time()
compute_reciprocals(values)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

print("-------------------------------------")

"""
在Python中，`%timeit` 是IPython/ Jupyter Notebook等环境中的一种魔术命令，用于测量代码片段的执行时间。但是，它不是标准Python语法，因此无法在标准的Python解释器或脚本中直接使用。

如果你想在标准Python环境中测量代码的执行时间，可以使用`timeit`模块。该模块提供了一个`timeit()`函数，可用于测量给定代码片段的执行时间。以下是一个示例：

```python
import timeit

code_to_test = """
# 在这里放置要测量执行时间的代码
"""

execution_time = timeit.timeit(code_to_test, number=10000)
print(f"Execution time: {execution_time} seconds")
```

上面的示例将 `code_to_test` 中的代码执行10,000次，并打印出总共的执行时间。

请注意，`timeit`模块还提供了其他功能，例如在统计运行时间时禁用垃圾回收机制等。你可以查阅官方文档以获取更多详细信息。
"""

import timeit

def compute_reciprocals(values):
    res = []
    for value in values:
        res.append(1/value)
    return res

values = list(range(1, 100))

code_to_test = """
compute_reciprocals(values)
"""

# 将 globals 参数设置为 globals()，以便在计时期间可以访问该函数。
execution_time = timeit.timeit(code_to_test, globals=globals(), number=100)
print(f"Execution time: {execution_time} seconds")

"""
在Python中，你可以使用`%timeit`魔术命令来测量代码的执行时间，并计算多次运行的平均值。以下是如何使用`%timeit`方法来获得多次运行的平均值：

```python
import timeit

def compute_reciprocals(values):
    res = []
    for value in values:
        res.append(1/value)
    return res

values = list(range(1, 1000000))

# 定义一个函数来运行代码并返回执行时间
def run_code():
    compute_reciprocals(values)

# 使用%timeit方法运行代码并获取多次运行的平均值
result = %timeit -n 10 -r 5 -o run_code()

# 输出多次运行的平均执行时间
average_execution_time = result.best
print(f"Average execution time: {average_execution_time} seconds")
```

在上面的示例中，`%timeit`方法的参数如下：

- `-n 10`：运行代码的次数。这里设置为10次。
- `-r 5`：重复运行的次数。这里设置为5次。
- `-o`：将结果存储在一个变量中。

`%timeit`方法会运行代码多次，并返回一个`TimeitResult`对象。通过访问该对象的属性，例如`best`，你可以获得多次运行的平均时间。

注意，`%timeit`方法通常用于Jupyter Notebook或IPython交互式环境中。如果你在普通的Python脚本中运行代码，你可以使用`timeit`模块的`timeit()`函数来测量代码的执行时间。"""

print("-------------------------------------")

# 使用 Numpy 运算速度是 Python for 循环的近50倍，质的飞跃
import timeit
import numpy as np

def compute_reciprocals(values):
    return np.reciprocal(values)

code_to_test = """
compute_reciprocals(values)
"""

values = np.arange(1, 1000000)
execution_time = timeit.timeit(code_to_test, globals=globals(), number=100)
print(f"Execution time: {execution_time} seconds")

print("-------------------------------------")

# Numpy为何如此高效
# 编译型语言 VS 解释型语言
# Numpy是由C语言编写的：C语言执行时，对代码进行整体编译，速度更快

# 连续单一类型存储 VS 分散多类型存储
# 1. Numpy数组内的数据类型必须是统一的，如全部是浮点型，而Python列表支持任意类型数据的填充
# 2. Numpy数组内的数据连续存储在内存中，而Python列表的数据分散在内存中
# 这种存储方式与更加高效的底层处理方式结合

# 多线程 VS 线程锁
# Python语言执行时有线程锁，无法实现真正的多线程并行，而C语言可以

print("-------------------------------------")

# 什么时候用Python
# 在数据处理的过程中，遇到"Python for"循环，实现一些向量化，矩阵化的操作时，优先考虑使用 Numpy
# 如 两个向量的点乘，矩阵乘法

# Numpy数组的创建
# 从列表开始创建
import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x)
print(type(x))
print(type(x[0]))
print(x.shape)

# 设置数组的数据类型
x = np.array([1, 2, 3, 4, 5], dtype="float32")
print(x)
print(type(x[0]))

# 二维数组
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(x)
print(x.shape)

print("-------------------------------------")

# 从头创建数组
# 创建长度为5的数组，值都为0
x = np.zeros(5, dtype=int)
print(x)
# 创建一个2*4的浮点型数组，值都为1
x = np.ones((2, 4), dtype=float)
print(x)
# 创建一个3*5的数组，值都为8.8
x = np.full((3, 5), 8.8)
print(x)
# 创建一个3*3的单位矩阵
x = np.eye(3)
print(x)
# 创建一个线性序列数组，从1开始，到15结束，步长为2
x = np.arange(1, 15, 2)
print(x)
# 创建一个4个元素的数组，这四个数均匀地分配0~1
x = np.linspace(0, 1, 4)
print(x)
# 创建一个10个元素的数组，形成1~10^9的等比数列
x = np.logspace(0, 9, 10)
print(x)
# 创建一个3*3的，在0~1之间均匀分布的随机数构成的数组
x = np.random.random((3, 3))
print(x)
# 创建一个3*3的，均值为0，标准差为1的正态分布随机数构成的数组
x = np.random.normal(0, 1, (3, 3))
print(x)
# 创建一个3*3的，在[0, 10)之间随机整数构成的数组
x = np.random.randint(0, 10, (3, 3))
print(x)
# 随机重排列
x = np.array([10, 20, 30, 40])
permuted_x = np.random.permutation(x)    # 随机重排列，生成新列表
print(permuted_x)
"""可以使用 np.random.permutation(x) 来对数组x进行随机排列。该函数会返回一个新的打乱顺序的数组，而不会修改原始数组x。"""
"""每次运行代码，结果都可能不同，因为它是随机的。"""
np.random.shuffle(x)
print(x)

print("-------------------------------------")

"""
让我为您解释一下各个参数的含义：

1. `np.arange(10, 25, dtype=float)`：
   - `np.arange()` 是 NumPy 库中的一个函数，用于创建一个包含指定范围内数值序列的数组。
   - 参数 `10` 是起始值，表示序列的起始点。
   - 参数 `25` 是终止值（不包含在序列中），表示序列的结束点。
   - 参数 `dtype=float` 表示数据类型为浮点数（float）。这意味着生成的数组将包含从10到24的浮点数。

2. `np.random.choice(x, size=(4, 3))`：
   - `np.random.choice()` 是 NumPy 库中的一个函数，用于从给定数组中随机选择元素。
   - 参数 `x` 是要选择元素的数组。在这种情况下，它是上面创建的包含从10到24的浮点数的数组。
   - 参数 `size=(4, 3)` 指定了返回的数组的形状。这里它是一个4行3列的数组，即4个子数组，每个子数组包含3个元素。

总结一下，代码的作用是首先创建一个包含从10到24的浮点数的数组x，然后从x中随机选择元素创建一个4行3列的数组choice_x。
"""

# 随机采样
# 按指定形状采样
x = np.arange(10, 25, dtype=float)
print(x)
choice_x = np.random.choice(x, size=(4, 3))
print(choice_x)

# 按概率采样
probablit_x = np.random.choice(x, size=(4, 3), p=x/np.sum(x))
print(probablit_x)

print("-------------------------------------")

# Numpy数组的性质
# 数组的属性
x = np.random.randint(10, size=(3, 4))
print(x)

# 数组的形状
print(x.shape)

# 数组的维度
print(x.ndim)

y = np.arange(10)
print(y.ndim)

# 数组的大小-元素的个数
print(x.size)

# 数组的数据类型 dtype
print(x.dtype)

print("-------------------------------------")

# 数组索引
# 一维数组的索引
x = np.arange(10)
print(x[0])
print(x[-1])
print(x[5])

# 二维数组的索引
x2 = np.random.randint(0, 20, (2, 3))
print(x2)
print(x2[0, 0])
print(x2[1][1])

# numpy数组的整数类型是固定的，向一个整型数组中插入浮点值，浮点值会向下进行取整
x2[1, 2] = 1.618
print(x2)

print("-------------------------------------")

# 数组的切片
# 一维数组的切片跟列表一样
x1 = np.arange(20)
print(x1[:3])   # 左闭右开
print(x1[3:])
print(x1[::-1])
# 多维数组
x2 = np.random.randint(20, size=(3, 4))
print(x2)
print(x2[:2, :3])   # 前两行，前三列
print(x2[:2, 0:3:2])
print(x2[::-1, ::-1])
# 获取数组的行和列
x3 = np.random.randint(20, size=(3, 4))
print(x3)
"""
[[11 11 10  6]
 [ 2 13 14  8]
 [13  3 17  7]]
"""
print(x3[1, :]) # 第一行，从0开始计数
print(x3[1])
print(x3[:, 2]) # 得到的是一行，里面的内容是列 [10 14 17]
# 切片获取的是视图,而非副本
x4 = np.random.randint(20, size=(3, 4))
print(x4)
x5 = x4[:2, :2]
print(x5)
# 视图元素发生修改，则原数组亦发生相应的修改
# 修改切片的安全方式，copy
x6 = x4[:2, :2].copy()
x6[0, 0] = 90123
print(x4)
print(x5)
print(x6)

print("-------------------------------------")

# 数组的变形
x7 = np.random.randint(0, 10, (12,))
print(x7)
print(x7.shape)
x8 = x7.reshape(3, 4)
print(x8)
# reshape 返回的是视图，而不是副本
x8[0, 0] = 123213
print(x7)   # 但维度没有改变

print("-------------------------------------")

# 一维向量转行向量
x9 = x7.reshape(1, x7.shape[0])
print(x9)
x10 = x7[np.newaxis, :] # 转行向量
print(x10)

# 一维向量转列向量
x9 = x7.reshape(x7.shape[0], 1)
x10 = x7[:, np.newaxis]
print(x9)
print(x10)

# 多维向量转一维向量
x6 = np.random.randint(0, 10, (3, 4))
print(x6)
# flatten 返回的是副本, 一维数组
x7 = x6.flatten()
print(x7)
x7[0] = 12321
print(x6)
print(x7)
# ravel 返回的是视图
x8 = x6.ravel()
print(x8)
x8[0] = 12321
print(x6)
print(x8)

print("-------------------------------------")


# 数组的拼接
x1 = np.array([[1, 2, 3],
               [4, 5, 6]])
x2 = np.array([[7, 8, 9],
               [10, 11, 12]])
# 水平拼接---非视图
x3 = np.hstack([x1, x2])
print(x3)
x3[0, 0] = 0

x4 = np.c_[[x1, x2]]
print(x4)
x4[0, 0] = 3
print(x1)
"""
np.c_是一个索引对象，用于将切片对象转换为沿第二轴连接的数组。它不应作为函数调用。

要修复这个问题，可以使用np.concatenate()函数进行数组的拼接操作。下面是修改后的代码示例：
"""
x4 = np.concatenate([x1, x2], axis=1)
print(x4)
x4[0, 0] = 3
print(x1)

"""
`np.concatenate([x1, x2], axis=1)`是NumPy的函数，用于沿指定轴将两个或多个数组连接起来。

参数说明如下：
- `x1`和`x2`：要连接的数组，可以是任意维度的数组。它们的形状在除了连接轴（axis）上的其他轴应该是相等的。
- `axis`：指定连接的轴。默认为0，表示沿着第一个轴进行连接；当`axis=1`时，表示沿着第二个轴进行连接。

例如，如果`x1`和`x2`都是二维数组，形状分别为`(m, n1)`和`(m, n2)`，则使用`np.concatenate([x1, x2], axis=1)`将它们连接起来后的结果将是一个形状为`(m, n1+n2)`的二维数组。
"""
"""
在编程中，数组连接的轴通常指的是沿着某个维度将多个数组合并成一个更大的数组的操作。这个维度称为连接轴或拼接轴。

具体来说，在Python的NumPy库中，可以使用`numpy.concatenate()`函数来实现数组的连接操作。这个函数接受两个参数：`arrays`和`axis`。`arrays`是要连接的数组序列，而`axis`表示连接的轴或维度。

例如，假设有两个一维数组`a = [1, 2, 3]`和`b = [4, 5, 6]`，如果我们想沿着水平方向（轴为1）将它们连接起来，可以使用以下代码：

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b), axis=0)
print(result)
```

输出结果为：
```
[1 2 3 4 5 6]
```

在这个例子中，通过指定`axis=0`，我们沿着第一个维度将数组`a`和`b`连接起来，形成了一个新的一维数组。

除了`numpy.concatenate()`函数外，还有其他一些类似的函数可以用于数组的连接操作，如`numpy.vstack()`用于垂直连接（沿着行方向），`numpy.hstack()`用于水平连接（沿着列方向）等。这些函数的使用方式类似，在指定连接轴时需要注意维度的对应关系。
"""
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b), axis=0)
print(result)

print("-------------------------------------")

# 垂直拼接---非视图
x1 = np.array([[1, 2, 3],
               [4, 5, 6]])
x2 = np.array([[7, 8, 9],
               [10, 11, 12]])
x3 = np.vstack([x1, x2])
print(x3)
x4 = np.r_[x1, x2]
print(x4)

print("-------------------------------------")

# 数组的分裂
# split的用法
x6 = np.arange(10)
print(x6)
x1, x2, x3 = np.split(x6, [2, 7])
print(x1, x2, x3)   # 分成3段

# hsplit的用法
x7 = np.arange(1, 26).reshape(5, 5)
print(x7)
left, middle, right = np.hsplit(x7, [2, 4])
print("left:\n", left)  # 0 - 1
print("middle:\n", middle)  # 2 - 3
print("right:\n", right)  # 4

# vsplit
x7 = np.arange(1, 26).reshape(5, 5)
print(x7)
up, middle, down = np.vsplit(x7, [2, 4])
print("up:\n", up)  # 0 - 1
print("middle:\n", middle)  # 2 - 3
print("down:\n", down)  # 4

print("-------------------------------------")

# 向量化运算
# 与数字的加减乘除
# 整体操作
x1 = np.arange(1, 6)
print("x1+5=\n", x1+5)
print("x1-5=\n", x1-5)
print("x1*5=\n", x1*5)
print("x1/5=\n", x1/5)
print("-x1=\n", -x1)
print("x1**2=\n", x1**2)
print("x1//2=\n", x1//2)
print("x1%2=\n", x1%2)
# 绝对值，三角函数，指数，对数
# 绝对值
x2 = np.array([1, -1, 2, -2, 0])
print(x2)
print(np.abs(x2))
# 三角函数
theta = np.linspace(0, np.pi, 3)
print(theta)
print("sin(theta): ", np.sin(theta))
print("cos(theta): ", np.cos(theta))
print("tan(theta): ", np.tan(theta))
x = [-1, 0, 1]
print("arcsin(x): ", np.arcsin(x))
print("arccos(x): ", np.arccos(x))
print("arctan(x): ", np.arctan(x))
# 指数计算
x = np.arange(3)
print(np.exp(x))
# 对数运算
x = np.array([1, 2, 4, 8, 16])
print("ln(x): ", np.log(x))
print("log2(x): ", np.log2(x))
print("log10(x): ", np.log10(x))

print("-------------------------------------")

x1 = np.arange(1, 6)
x2 = np.arange(6, 11)
print(x1)
print(x2)
print("x1+x2=\n", x1+x2)
print("x1-x2=\n", x1-x2)
print("x1*x2=\n", x1*x2)
print("x1/x2=\n", x1/x2)

print("-------------------------------------")

# 矩阵运算
x = np.arange(9).reshape(3, 3)
print(x)

# 矩阵的转置
y = x.T
print(y)

print("-------------------------------------")

# 矩阵乘法
x = np.array([[1, 0],
             [1, 1]])
y = np.array([[0, 1],
             [1, 1]])
print(x.dot(y))
print(np.dot(x, y))
print(y.dot(x))
print(np.dot(y, x))
# 注意跟x*y的区别
print(x * y)

print("-------------------------------------")

# 广播运算
x = np.arange(3).reshape(1, 3)
print(x)
print(x+5)

# 如果两个数组的形状在维度上不匹配
# 那么数组的形式会沿着维度为1的维度进行扩展以匹配另一个数组的形状。
x1 = np.ones((3,3))
print(x1)
x2 = np.arange(3).reshape(1, 3)
print(x2)
print(x1+x2)
x3 = np.logspace(1, 10, 10, base=2).reshape(2, 5)
print(x3)
x4 = np.array([[1, 2, 4, 8, 16]])
print(x4)
print(x3/x4)
x5 = np.arange(3).reshape(3, 1)
print(x5)
x6 = np.arange(3).reshape(1, 3)
print(x6)
print(x5+x6)

print("-------------------------------------")

# 比较运算和掩码

# 比较运算
x1 = np.random.randint(100, size=(10,10))
print(x1)
# 每个单位都进行比较
print(x1 > 50)

print("-------------------------------------")

# 操作布尔数组
x2 = np.random.randint(10, size=(3, 4))
print(x2)
print(x2 > 5)
print(np.sum(x2 > 5))
print(np.all(x2 > 0))
print(np.any(x2 == 6))
print(np.all(x2 < 9, axis=1))   # 按行进行判断
print((x2 < 9) & (x2 >5))
print(np.sum((x2 < 9) & (x2 >5)))

print("-------------------------------------")

# 将布尔数组作为掩码
print(x2)
print(x2 > 5)
print(x2[x2 > 5]) # 几个大于 5 值为 True 的列入数组

print("-------------------------------------")

# 花哨的索引
# 一维数组
x = np.random.randint(100, size=10)
print(x)
# 注意：结果的形状与索引数组ind一致
ind = [2, 6, 9]
print(x[ind])
ind = np.array([[1, 0],
               [2, 3]])
print(x[ind])

print("-------------------------------------")

# 多维数组
x = np.arange(12).reshape(3, 4)
print(x)
row = np.array([0, 1, 2])
col = np.array([1, 3, 0])
print(x[row, col])
print(row[:, np.newaxis]) # 列向量
print(col[np.newaxis, :])   # 列向量转为行向量
print(row[np.newaxis, :], col) # 广播机制

print("-------------------------------------")

# 数值排序
x = np.random.randint(20, 50, size=10)
print(x)
x1 = np.sort(x)
print(x1)
# 不会改变原来的矩阵
print(x)

x2 = x.sort()
# 无返回值，且会改变原来的矩阵
print(x)

print("-------------------------------------")

# 获得排序索引
x = np.random.randint(20, 50, size=10)
print(x)
# 获得排序以后的位置
i = np.argsort(x)
print(i)

print("-------------------------------------")

# 最大最小值
x = np.random.randint(20, 50, size=10)
print(x)
print("max:", np.max(x))
print("min:", np.min(x))
print("max_index:", np.argmax(x))
print("min_index:", np.argmin(x))

print("-------------------------------------")

# 数值求和，求积
x = np.arange(1,6)
print(x)
print(x.sum())
print(np.sum(x))
x1 = np.arange(6).reshape(2,3)
print(x1)
# 按行求和
print(np.sum(x1, axis=1))
# 按列求和
print(np.sum(x1, axis=0))
# 全体求和
print(np.sum(x1))

print("-------------------------------------")

# 全体求积
print(x)
print(x.prod())
print(np.prod(x))

print("-------------------------------------")

# 中位数、均值、方差、标准差
x = np.random.normal(0, 1, size=10000)
print(x)
import matplotlib.pyplot as plt

plt.hist(x, bins=50)
plt.show()
"""
上述代码将绘制变量 'x' 中存储的数据的直方图，使用50个条形箱进行分组。
最终的图形将使用 'plt.show()' 命令显示出来。
"""

# 中位数
print(np.median(x))

# 均值
print(np.mean(x))
print(x.mean())

# 方差
print(x.var())
print(np.var(x))

# 标准差
print(x.std())
print(np.std(x))