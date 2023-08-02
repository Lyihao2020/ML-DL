# 标准库
# time库

# 获取现在时间
# time.localtime() 本地时间(早8个小时)
# time.gmtime() UTC世界统一时间
import time

t_local = time.localtime()
t_UTC = time.gmtime()
print("local: ", t_local)
print("UTC: ", t_UTC)

# 返回本地时间的字符串
print(time.ctime())

print("-------------------------------------")

# 时间戳与计时器
# 1. time.time()    返回自纪元以来的秒数，记录sleep()
# 2. time.perf_counter()    随意选取一个时间点，记录现在时间到该时间点的间隔秒数，记录sleep()
# 3. time.process_time()    随意选取一个时间点，记录现在时间到该时间点的间隔秒数，不记录sleep()
# perf_counter() 比 time() 精读更高一些
t_1_start = time.time()
t_2_start = time.perf_counter()
t_3_start = time.process_time()

res =  0
for i in range(1000000):
    res += i

time.sleep(5)
t_1_end = time.time()
t_2_end = time.perf_counter()
t_3_end = time.process_time()

print("time()方法: {:.3f}".format(t_1_end-t_1_start))
print("perf_counter()方法: {:.3f}".format(t_2_end-t_2_start))
print("process_time()方法: {:.3f}".format(t_3_end-t_3_start))

print("-------------------------------------")

# 格式化
# time.strftime 自定义格式化输出
lctime = time.localtime()
# %A 星期
print(time.strftime("%Y-%m-%d %A %H:%M:%S", lctime))

print("-------------------------------------")

# random库
# 随机种子 seed(a=None)
# 相同种子会产生相同的随机数
# 如果不设置随机种子，以系统当前时间为默认值
from random import *

seed(10)
print(random())
seed(10)
print(random())

# 不设置种子，会产生随机数
seed(a=None)
print(random())

print("-------------------------------------")

# 产生随机整数
# randint(a, b) 产生[a, b]之间的随机整数
numbers = [randint(1, 10) for i in range(10)]
print(numbers)

# randrange(a) 产生[0, a)之间的随机整数
numbers = [randrange(10) for i in range(10)]
print(numbers)

# randrange(a, b, step) 产生[a, b)之间以step为步长的随机整数
numbers = [randrange(0, 10, 2) for i in range(10)]
print(numbers)

print("-------------------------------------")

# 产生随机浮点数
# random() 产生[0.0, 1.0)之间的随机浮点数
numbers = [random() for i in range(10)]
print(numbers)

# uniform(a, b) 产生[a, b]之间的随机浮点数
numbers = [uniform(2.1, 3.5) for i in range(10)]
print(numbers)

print("-------------------------------------")

import random

# choice(seq) 从序列类型中随机返回一个元素
print(random.choice(["win", "lose", "draw"]))
print(random.choice("Python"))

# choice(seq, weights=None, k) 对序列类型进行k次重复采样，可设置权重
print(random.choices(["win", "lose", "draw"], k=5))
print(random.choices(["win", "lose", "draw"], [4, 4, 2], k=5))

# shuffle(seq) 将序列元素中元素随机排列，返回打乱后的序列
seq = ["win", "lose", "draw"]
random.shuffle(seq)
print(seq)

# sample(pop, k) 从pop类型中随机选取k个元素，以列表类型返回
print(sample([10, 20, 30, 40, 50], k=2))

print("-------------------------------------")

# 概率分布(高斯分布为例)
# gauss(mean, std)  生产一个符合高斯分布的随机数
number = gauss(0, 1)
print(number)

# 多生成几个
"""
当执行这段代码时，它将生成一个包含100,000个服从标准正态分布（均值为0，标准差为1）的随机数的列表。
这些随机数是使用`gauss(0, 1)`函数生成的。

`gauss()`函数是Python中`random`模块中的一个函数，用于生成服从正态分布的随机数。
它接受两个参数：均值和标准差。在这个例子中，均值为0，标准差为1，因此生成的随机数会符合标准正态分布。

生成的随机数存储在名为`res`的列表中。然后，使用`plt.hist()`函数将这些随机数进行直方图绘制。
直方图将随机数分成多个箱子（bins），每个箱子表示一个数值范围，并统计该范围内的随机数的频数。
参数`bins=1000`指定了直方图的箱子数量为1000，这意味着将整个数据范围划分为1000个小区间。

最后，通过调用`plt.show()`函数显示绘制的直方图。这将在新窗口中显示出直方图，并可视化随机数的分布情况。
"""
import matplotlib.pyplot as plt

res = [gauss(0, 1) for i in range(100000)]

plt.hist(res, bins=1000)
plt.show()

print("-------------------------------------")

# 用random库实现简单的微信红包分配
def red_packet(total, num):
    for i in range(1, num):
        per = random.uniform(0.01, total/(num-i+1)*2)   # 保证每个人获得的红包期望是 total/num
        total -= per
        print("第{}位红包金额：{:.2f}元".format(i, per))
    else:
        print("第{}位红包金额：{:.2f}元".format(num, total))

ls = list(range(1, 5))
print(ls)

red_packet(10, 5)

print("-------------------------------------")

import numpy as np

def red_packet01(total, num):
    ls = []
    for i in range(1, num):
        per = round(random.uniform(0.01, total / (num - i + 1) * 2), 2)  # 保证每个人获得的红包期望是 total/num
        ls.append(per)
        total -= per
    else:
        ls.append(total)
    return ls

# 重复法十万次红包，统计每个位置的平均值（约等于期望）
res = []
for i in range(100000):
    ls = red_packet01(10, 5)
    res.append(ls)

res = np.array(res)
print(res[:10])
print(np.mean(res, axis=0))

"""
当你导入`numpy`库时，你可以使用其中的函数和类来处理多维数组和执行数值计算。下面是你代码中使用到的`numpy`的一些主要用法：

1. `np.array()`函数：这个函数用于创建一个`numpy`数组对象。它接受一个可迭代对象（如列表）作为输入，并返回一个包含相同元素的`numpy`数组。

   例如，在你的代码中，`res = np.array(res)`将列表`res`转换为`numpy`数组对象。

2. `np.mean()`函数：这个函数用于计算数组的平均值。它接受一个数组作为输入，并根据指定的轴计算平均值。

   在你的代码中，`np.mean(res, axis=0)`计算了二维数组`res`每列的平均值。`axis=0`表示沿着第一个维度（行）进行计算。

3. 数组索引和切片：`numpy`允许你通过索引和切片操作访问和修改数组的元素。和Python列表类似，`numpy`数组的索引从0开始。

   在你的代码中，`res[:10]`使用切片操作获取数组`res`的前十行。

总之，`numpy`提供了很多强大的功能来处理数值数据和执行科学计算。它的广泛应用包括统计分析、线性代数运算、傅里叶变换等。

"""

print("-------------------------------------")

# 生成4位由数字和英文字母构成的验证码
import random
import string

print(string.digits)
print(string.ascii_letters)

s = string.digits + string.ascii_letters
v = random.sample(s, 4)
print(v)
print(''.join(v))

print("-------------------------------------")

# collections库 容器数据类型
import collections

# 具名元组  namedtuple
p = (1, 2)
# 构建一个新的元组子类
# 定义方法如下：typename 元组名字，field_name 域名
# collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
Point = collections.namedtuple("Point", ["x", "y"])
p = Point(1, y=2)
print(p)

# 调用属性
print(p.x)
print(p.y)

# 有元组性质
print(p[0])
print(p[1])
x, y = p
print(x)
print(y)

# 确实是元组子类
print(isinstance(p, tuple))

print("-------------------------------------")

# 模拟扑克牌
from random import *

Card = collections.namedtuple("Card", ["rank", "suit"])
ranks = [str(n) for n in range(2, 11)] + list("JQKA")
suits = "spades diamonds clubs hearts".split()
print("ranks: ", ranks)
print("suits: ", suits)
cards = [Card(rank, suit) for rank in ranks for suit in suits]
print(cards)

# 洗牌
shuffle(cards)
print(cards)

# 随机抽取一张牌
choice(cards)
print(cards)

# 随机抽取多张牌
ls = sample(cards, 5)
print(ls)

print("-------------------------------------")

# Counter 计数器工具
from collections import Counter
s = "牛奶奶找刘奶奶买牛奶"
colors = ["red", "blue", "red", "green", "blue", "blue"]
cnt_str = Counter(s)
cnt_color = Counter(colors)
print(cnt_str)
print(cnt_color)

# 是字典的一个子类
print(isinstance(Counter(), dict))

# 最常见统计 most_common(n)
# 提供n个频率最高的元素和计数
print(cnt_color.most_common(2))

# 元素展开 elements()
ls = list(cnt_str.elements())
print(ls)

# 其他一些加减操作
# 字典的加减类似
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)

print("-------------------------------------")

# 从一副牌中抽取10张，大于10的比例有多少
cards = collections.Counter(tens=16, low_cards=36)
seen = sample(list(cards.elements()), k=10)
print(seen)

print(seen.count("tens")/10)

print("-------------------------------------")

# deque 双向队列
# 列表访问数据非常快速
# 插入和删除操作非常慢，通过移动元素位置来实现
# 特别是 insert(0, v) 和 pop(0), 在列表开始进行的插入和删除操作
# 双向队列可以方便的在队列两边高效，快速的增加和删除元素

from collections import deque

d = deque("cde")
print(d)

d.append("f")
d.append("g")
d.appendleft("b")
d.appendleft("a")
print(d)

d.pop()
d.popleft()
print(d)

print("-------------------------------------")

# itertools 库 迭代器
# 排列组合迭代器
# product 笛卡尔积
import itertools
for i in itertools.product("ABC", "01"):
    print(i)

for i in itertools.product("ABC", repeat=3):
    print(i)

print("-------------------------------------")

# permutations 排列
for i in itertools.permutations("ABC", 3):  # 3为排列长度
    print(i)

for i in itertools.permutations(range(3)):
    print(i)

print("-------------------------------------")

# combinations 组合
for i in itertools.combinations("ABCD", 2):  # 2是组合的长度
    print(i)

for i in itertools.combinations(range(4), 3):
    print(i)

print("-------------------------------------")

# combinations_with_replacement 元素可重复组合
for i in itertools.combinations_with_replacement("ABC", 2):
    print(i)

for i in itertools.combinations_with_replacement("ABC", 2):
    print(i)

"""
import itertools

# 使用combinations_with_replacement函数生成元素可重复组合
for i in itertools.combinations_with_replacement("ABC", 2):
    print(i)

# 使用repeat参数指定重复次数来生成元素可重复组合
for i in itertools.combinations_with_replacement("ABC", 2):
    print(i)

"""

print("-------------------------------------")

# 拉链
# zip 短拉链
for i in zip("ABC", "012", "xyz"):
    print(i)

# 长短不一时，执行到最短对象处，就停止
for i in zip("ABC", "012345"):
    print(i)

print("-------------------------------------")

# 长拉链 zip_longest
# 长度不一时，执行到最长的对象处，就停止，缺省元素用None或指定字符串来替代
for i in itertools.zip_longest("ABC", "012345"):
    print(i)

for i in itertools.zip_longest("ABC", "012345", fillvalue="?"):
    print(i)

print("-------------------------------------")

# 无穷迭代器
# count(start=0, step=1)    计数
print(itertools.count(10))

# cycle(iterable)   # 循环
# 创建一个迭代器，返回 iterable 所有元素，无限重复
"""无限循环
for i in itertools.cycle("ABC"):
    print(i)
"""
# repeat(object, [times]) # 重复
# 创建一个迭代器，不断重复object，除非设定参数times，否则将无限重复

for i in itertools.repeat("ABC", 3):
    print(i)

print("-------------------------------------")

# 其他
# chain(iterables)  锁链
# 把一组迭代对象串联起来,形成一个更大的迭代器
for i in itertools.chain("ABC", [1, 2, 3]):
    print(i)

# enumerate(iterable, start=0) 枚举(Python内置)
# 产出由两个元素构成的元组，结构是(index, item)，其中 index 从 start 开始，item 从 iterable 中取
for i in enumerate("Python", start=1):
    print(i)

# groupby(iterable, key=None)   分组
# 创建一个迭代器，按照 key 的方式，返回 iterable 中连续的键和组
# key为None默认把连续重复元素分组
for key, group in itertools.groupby("AAAABBBCCDDDAABBB"):
    print(key, list(group))

animals = ["cat", "eagle", "dog", "lion", "bear", "bird", "fish"]
animals.sort(key=len)
print(animals)
for key, group in itertools.groupby(animals, key=len):
    print(key, list(group))

animals = ["cat", "eagle", "dog", "lion", "bear", "bird", "fish"]
animals.sort(key = lambda x:len(x))
print(animals)
for key, group in itertools.groupby(animals, key = lambda x:len(x)):
    print(key, list(group))

animals = ["cat", "eagle", "dog", "lion", "bear", "bird", "fish"]
animals.sort(key = lambda x:x[0])
print(animals)
for key, group in itertools.groupby(animals, key = lambda x:x[0]):
    print(key, list(group))


