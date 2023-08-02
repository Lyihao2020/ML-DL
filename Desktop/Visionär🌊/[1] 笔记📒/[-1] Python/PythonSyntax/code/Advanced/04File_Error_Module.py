# 文件
# 文件的打开
"""
with open("文件路径"， "打开模式"， encoding = "操作文件的字符编码"）as f：
    "对文件进行的读写操作"

# 使用 with 块的好处在于，执行完毕后，自动对文件进行close操作
"""
with open("./测试文件.txt", "r", encoding="gbk") as f:
    """读取整个内容"""
    text = f.read()
    print(text)

print("-------------------------------------")
# 程序与文件在同一文件夹内，可简化为文件名
# r 只读模式，如文件不存在，报错
# w 覆写模式，如文件不存在，则创建；如文件存在，则完全覆盖原文件
# x 创建写模式，如文件不存在，则创建；如文件存在，则报错
# a 追加写模式，如文件不存在，则创建；如文件存在，则在文件后追加内容
# b 二进制文本模式，不能单独使用，需要配合"rb","wb","ab",该模式不需指定encoding
# t 文本文件模式，默认值，需配合"rt","wt","at"，一般省略，简写成"r","w","a"
# + 与"r","w","x","a"配合使用，在原功能基础上，增加读写功能
# 打开模式缺省，默认为只读模式

# 字符码
# 通用 utf-8
# 中文 gbk
# 逐行读取 f.readline()
with open("测试文件.txt", "r", encoding="gbk") as f:
    text = f.readline()
    print(text)
    """
    for i in range(x):  # x 为所有行数
        text = f.readline()
        print(text)
    """

print("-------------------------------------")

with open("测试文件.txt", "r", encoding="gbk") as f:
    while True:
        text = f.readline()
        if not text:
            break
        else:
            print(text, end="") # 保留原文的换行，使print()的换行不起作用

print("-------------------------------------")

# 读入所有行，以每行为元素形成一个列表 f.readlines()
with open("测试文件.txt", "r", encoding="gbk") as f:
    text = f.readlines()
    print(text) # 存在换行符

print("-------------------------------------")

with open("测试文件.txt", "r", encoding="gbk") as f:
    for text in f.readlines():
        print(text)

print("-------------------------------------")

# 文件读取总结：
# 文件比较大时， read() 和 readlines() 占用内存较大，不建议使用
# readline用起来又不太方便
with open("测试文件.txt", "r", encoding="gbk") as f:
    for text in f:
        print(text)

print("-------------------------------------")

# 二进制文件读取二进制图片

"""
with open("test.jpg", "rb") as f:
    print(len(f.readline()))
    
print("-------------------------------------")
"""

# 文件的写入
# 向文件写入一个字符串或字节流 f.write()
with open("测试文件.txt", "w", encoding="utf-8") as f:
    # 一定要是字符串格式哦
    f.write("With Chrome profiles you can separate all your Chrome stuff. \n")
    f.write("Create profiles for friends and family, or split between work and fun.")

with open("测试文件.txt", "r", encoding="utf-8") as f:
    for i in range(2):
        text = f.readline()
        print(text)

print("-------------------------------------")

# 将一个元素为字符串的列表整体写入文件 f.writelines()
ls = ["With Chrome profiles you can separate all your Chrome stuff.\n", "Create profiles for friends and family, or split between work and fun."]
with open("测试文件.txt", "w", encoding="utf-8") as f:
    f.writelines(ls)

with open("测试文件.txt", "r", encoding="utf-8") as f:
    for text in f:
        print(text)

print("-------------------------------------")

# 既读又写
# 使用"+"

# r+ ： 指针在开始位置，要把指针移到末尾才可以开始写，否则会覆盖前面内容
with open("测试文件.txt", "r+", encoding="utf-8") as f:
    #   for line in f:
    #       print(line)     # 全部读一遍，指针可以到达末尾
    f.seek(0, 2)    # seek(偏移字节数, 位置(0: 开始，1：当前位置，2：结尾))
    f.writelines(ls)
    f.seek(0, 0)    # 修改指针，回到开头
    print(f.read())

# w+ 如文件不存在，则创建；如文件存在，则立即清空原内容
# a+ 如文件不存在，则创建；指针在末尾，则在文件后追加内容，不会清空原内容

# 数据的存储与读取
# 数据存储结构csv和json
# csv格式: 用逗号将数据分开的字符序列，可以用excel打开
"""
Python的`strip()`函数是用于去除字符串两端指定字符（默认为空格）的方法。它返回一个新的字符串，其中不包含指定字符。

`strip()`函数有两个可选参数：
- `chars`：指定要删除的字符集合。如果不提供该参数，默认删除字符串两端的空格。
- `start`：指定要删除的起始位置字符集合。
- `end`：指定要删除的结束位置字符集合。

以下是`strip()`函数的示例用法：

```python
string = "  Hello, World!  "
new_string = string.strip()  # 去除两端的空格
print(new_string)  # 输出: "Hello, World!"

string = "###Hello, World!$$$"
new_string = string.strip("#$")  # 去除两端的"#"和"$"
print(new_string)  # 输出: "Hello, World!"

string = "###Hello, World!$$$"
new_string = string.strip("#$H!")  # 去除两端的"#", "$", "H"和"!"
print(new_string)  # 输出: "ello, World"

string = "###Hello, World!$$$"
new_string = string.strip("#$", "!")  # 去除两端的"#", "$"和"!"
print(new_string)  # 输出: "Hello, World"

string = "Hello, World!"
new_string = string.strip("Hd!")  # 去除两端的"H", "d"和"!"
print(new_string)  # 输出: "ello, Worl"
```

请注意，`strip()`函数返回的是一个新的字符串，并不会修改原始字符串。
"""
# 读取
with open("成绩.csv", "r", encoding="utf-8") as f:
    ls = []
    for line in f:
        ls.append(line.strip("\n").split(","))
for res in ls:
    print(res)

# 写入
with open("成绩.csv", "w+", encoding="utf-8") as f:
    ls = [["编号", "数学", "语文"], ['1', '100', '98'], ['2', '96', '99'], ['3', '97', '95']]
    for line in ls:
        # 写入时要使用逗号分隔
        f.write(",".join(line) + "\n")

# json格式: 常用于保存字典类型
# 写入：dump()
import json

scores = {"Peter": {"math": 96, "physics":98},
          "Paule": {"math": 100, "physics": 97},
          "Hanser": {"math":98, "physics": 95}}
with open("score.json", "w", encoding="utf-8") as f:
    # indent 表示字符串换行+缩进 ensure_ascii=False 显示中文
    json.dump(scores, f, indent=4, ensure_ascii=False)

# 读取：load()
with open("score.json", "r", encoding="utf-8") as f:
    scores = json.load(f)   # 加载整个对象
    for k, v in scores.items():
        print(k, v)

# 异常处理
# 常见异常
"""
ZeroDivisionError
FileNotFoundError
ValueError  值错误 传入一个调用者不期望的值，即使这个值的类型是正确的
IndexError  索引错误
TypeErroe   类型错误
还有一些常见的异常类型：当异常发生的时候，如果不预先设定处理方法，程序就会中断
"""
# 异常的处理
# 提高程序的稳定性和可靠性
"""
1. try_except
"""
# 单分支
x = 10
y = 0
try:
    z = x / y
except ZeroDivisionError:
    z = x / (y + 1e-7)
    print(z)
    print("ZeroDibvisionError!")

# 多分支
ls = []
d = {"name": "大杰仔"}
try:
    d["age"]
except NameError:
    print("变量名不存在")
except IndexError:
    print("索引超出界限")
except KeyError:
    print("键不存在")

# 万能异常 Exception
ls = []
d = {"name": "大杰仔"}
try:
    y = m
except Exception as e:  # 虽不能获得错误具体类型，但可以获得错误的值
    print(e)

# try_except_else
# 如果try执行，则else也执行，可以把else看作是try成功的额外奖赏
try:
    with open("测试文件.txt", "r", encoding="utf-8") as f:
        for text in f:
            print(text)
except FileNotFoundError:
    print("FileNotFoundError!")
else:
    with open("测试文件.txt", "r+", encoding="utf-8") as f:
        #   for line in f:
        #       print(line)     # 全部读一遍，指针可以到达末尾
        f.seek(0, 2)  # seek(偏移字节数, 位置(0: 开始，1：当前位置，2：结尾))
        f.writelines(ls)
        f.seek(0, 0)  # 修改指针，回到开头
        print(f.read())

# try_except_finally
# 不论try模块是否执行，finally最后都执行
ls = []
d = {"name": "大杰仔"}
try:
    y = m
except Exception as e:  # 虽不能获得错误具体类型，但可以获得错误的值
    print(e)
finally:
    print("finally execute!")

# 模块
# 模块包括第三方库，和自定义文件
# 自定义文件包括 py文件 和 包（多个py文件）
# 包（文件夹内多个py文件，再加一个__init__.py文件（内容可为空））

# 调用模块
import time

start = time.time()
time.sleep(3)
end = time.time()
print("程序运行时间：{:.2f}s".format(end-start))


# 从模块中导入类或函数 (from 模块 import 类名或函数名)
from itertools import product
ls = list(product("AB", "123"))
print(ls)

"""
注意这种用法
from function.fun1 import f1
f1()

from function import fun1, fun2
fun1.f1()
fun2.f2()
"""

# 导入模块中所有类和函数
from random import *
print(randint(1, 100))  # 产生[1, 100]之间随机整数
print(random()) # 产生[0, 1)之间随机小数

# 模块的查找路径
# 1. 优先从内存中读取，内存中已经加载的模块
# 2. 内置模块
"""
Python 启动时，会默认加载一些modules存放在sys.modules中
sys.modules 变量包含一个由当前载入（完整且成功导入）到解释器的模块组成的字典，模块名作为键，他们的位置作为值
"""
import sys
print(len(sys.modules))
print("math" in sys.modules)
print("numpy" in sys.modules)
for k, v in list(sys.modules.items())[:5]:
    print(k, ":", v)
# 3. sys.path路径中包含的模块
import sys
sys.path
# 第一个路径是当前执行文件所在文件夹
# 若需将不再该文件夹内的模块导入，需要将模块的路径添加到sys.path
"""
import sys

sys.path.append("\\路径") # 注意是双斜杠

import fun3

fun3.f3()
# 导入fun3成功
"""