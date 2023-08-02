# 组合数据类型
# 列表
# 序列类型：内部元素有位置关系，能通过位置序号访问其中的元素
# 列表是一个可以使用多种类型元素，支持元素的增删改查等操作的序列类型
ls = ["Python", 1989, True, {"version":3.7}]
print(ls)
# 另一种创建方式 list(迭代对象)
# 可迭代对象包括字符串、元祖、集合、range()等
print(list("人工智能是未来的趋势"))
print(list(("我", "们", "很", "像")))   # 元组转列表
print(list({"我", "们", "很", "像"}))   # 集合转列表
# 特殊的range():起始数字，中止数字，数字间隔
for i in range(6):  # [0, 1, 2, 3, 4, 5]
    print(i)
# 如果起始数字缺省，默认为0
# 不包含中止数字
# 数字间隔缺省，则默认为1
for i in range(1, 11, 2):
    print(i)
# range转列表
print(list(range(1, 11, 2)))

# 列表的性质
# 列表的长度
ls = [1, 2, 3, 4, 5]
print(len(ls))
# 列表的切片
cars = ["BYD", "BMW", "AUDI", "TOYOTA"]
# 正向切片
print(cars[:3])     # 获取前三个元素
print(cars[1:4:2])
print(cars[:])
print(cars[-4:-2])  # 获取前两个元素
# 反向切片
print(cars[:-4:-1])
print(cars[::-1])

# 列表的操作符
a = [1, 2]
b = [3, 4]
print(a + b)
# 使用 n * list 或 list * n 实现列表的成倍复制
# 进行初始化
print([0] * 10)

# 列表的操作符号
# 增加元素：末尾增加元素 append
language = ["Python", "C++", "R"]
language.append("PHP")
print(language)
language.append(["Ruby", "Golang"])
print(language)
# 在任意位置插入元素：insert(位置编号，元素)，在位置编号相应元素前插入待插元素
language.insert(1, "Java")
print(language)
# 在末尾整体插入一个另一列表，extend
language.extend(["Ruby", "Golang"])
print(language)

# 删除元素
# 删除列表i位置的元素 pop
language.pop(-3)
print(language)
# 不写位置信息，默认删除最后一个元素
# 删除列表中第一次出现的待删除元素 remove
while "C++" in language:
    language.remove("C++")
print(language)

# 查找元素
# 列表中第一次出现待查元素的位置 列表.inde(待查元素)
idx = -1
while "P" in language:
    idx = language.index("P")
print(idx)

# 修改元素
language[0] = "JVM"
print(language)

# 列表的复制
"""
# 错误的方法: 相当于取了一个别名，是深拷贝，在原列表上操作会影响新列表
language2 = language
print(language2)
language.pop()
print(language2)
print(language)
"""
# 正确的方式：浅拷贝
# 方式一
language2 = language.copy()
language.pop()
print(language2)
print(language)
# 方式二: 列表[:]
language2 = language[:]
language.pop()
print(language2)
print(language)

# 列表的排序
# 使用列表.sort()对列表进行永久排序
# 直接在列表上操作，无返回值
language = [2, 5, 2, 8, 19, 3, 7]
language.sort()
print(language)
# 递减排序
language.sort(reverse=True)
print(language)
# 希望原本的列表不变，返回排序后的列表
language2 = sorted(language)
print(language)
print(language2)
language2 = sorted(language, reverse=True)
print(language)
print(language2)
# 使用列表.reverse()对列表进行永久翻转
# 直接在列表上操作，无返回值
print(language[::-1])
language.reverse()
print(language)

# 使用for循环对列表进行遍历
for i in language:
    print(i)

# 元组
# 元组是一个可以使用多种数据类型元素，一旦定义，内部元素不支持增，删和修改操作的序列类型
# 可以将"元组"视作"不可变的列表"
names = ("Peter", "Paul", "Mary")
# 元组的操作
# 不支持元素的增加，删除，修改，排序操作
# 其他操作与列表一致
# 元组的常见用处
# 打包与解包
# 例1
def f1(x):
    return x**2, x**3   # 实现打包返回

print(f1(3))
print(type(f1(3)))  # 元组类型
a, b = f1(3)
print(a)
print(b)
# 例2
numbers = [201901, 201902, 201903]
names = ["小明", "小红", "小强"]
list01 = list(zip(numbers, names))
print(list01)
for number, name in zip(numbers, names):
    print(number, name)

# 字典
# 通过映射关系"键-值"来实现数据存储和查找
# 常规的字典是无序的
# 字典键的要求
# 1. 字典的键不能重复
students = {201901: '小明', 201902: '小红', 201903: '小强'}
print(students)
students = {201901: '小明', 201901: '小红', 201903: '小强'}
print(students) # 若重复，只取前面的
# 2. 字典的键必须是不可变类型，如果键可变，就找不到存储的值了
# 不可变类型: 数字，字符串，元组。一旦确定，他自己就是他自己，变了就不是他了
# 可变类型: 列表，字典，集合。一旦确定，还可以进行修改
d1 = {1: 3}
d2 = {"s": 3}
d3 = {(1, 2, 3): 3}
"""
以下这些都不合法
d = {[1, 2]: 3}
d = {{1: 2}: 3}
d = {{1, 2}: 3}
"""

# 字典的性质
# 字典的长度 = 键值对的个数
students = {201901: '小明', 201902: '小红', 201903: '小强'}
print(len(students))    # 3
# 字典的索引
print(students[201902])

# 增加新的键值对
students[201904] = '小雪'
print(students)

# 删除键值对
# del 方法
del students[201903]
print(students)
# pop方法
value = students.pop(201902)
print(value)
print(students)
# popitem() 随即删除一个键值对，并以元组返回删除键值对
key, value = students.popitem()
print(key, value)
print(students)

# 方法
# d.get():从字典中获取键值对应的值，如果没有这个键，则返回default
s = "牛奶奶找刘奶奶买牛奶"
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
    print(d)
print(d)
# d.keys() d.values()
students = {201901: '小明', 201902: '小红', 201903: '小强'}
print(list(students.keys()))
print(list(students.values()))
# d.items()
print(list(students.items()))
for key, value in students.items():
    print(key, value)

# 集合
# 一系列互不相等的无序集合,无序，无序，无序
# 元素必须是不可变类型：数字，字符串或元组，可视作字典的键
# 可以看作是没有值，或者值为None的字典
students = {'小明', '小红', '小强'}
print(students)
# 集合的运算
Chinese = {"刘德华", "张学友", "张曼玉", "钟楚红", "古天乐", "林青霞"}
Math = {"林青霞", "郭富城", "王祖贤", "刘德华", "张曼玉", "黎明"}
print(Chinese & Math)   # 返回交集
print(Chinese | Math)   # 返回并集
print(Chinese ^ Math)   # 返回两个集合中的非共有元素
print(Chinese - Math)   # 返回在集合Chinese中但不在Math中元素
# 集合增加元素
Chinese.add("赖亿豪")
print(Chinese)
# 集合移除元素
Chinese.remove("赖亿豪")
print(Chinese)
# 集合的长度
print(len(Chinese))
# 集合的遍历
for i in Chinese:
    print(i)