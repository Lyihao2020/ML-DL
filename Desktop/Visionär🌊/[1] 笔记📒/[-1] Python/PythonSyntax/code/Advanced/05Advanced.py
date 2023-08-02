# 数据类型的底层实现
# 从奇怪的列表说起
# 浅拷贝
list_1 = [1, [22, 33, 44], (5, 6, 7), {"name": "Sarah"}]
# list_3 = list_1   # 错误！！！相当于起了一个别名
list_2 = list_1.copy()  # 或者list_1[:] \ list(list_1) 均可实现浅拷贝
# 对浅拷贝前后两列表分别进行操作
list_2[1].append(55)

print("list_1: ", list_1)
print("list_2: ", list_2)   # 两者结果相同
print("------------------------------------")

# 列表的底层实现
# 引用数组的概念
# 列表内的元素可以分散在内存里
# 列表存储的是，实际上是这些元素的地址，地址在内存中连续
# list_1 存储的是 1， 地址列表， 地址元组，字典散列表
# 然后通过上述的三个地址找到对应的数据类型
# 添加元素
list_1.append(100)
list_2.append("n")
print("list_1: ", list_1)
print("list_2: ", list_2)
print("------------------------------------")
# 修改元素
list_1[0] = 10
list_2[0] = 20
print("list_1: ", list_1)
print("list_2: ", list_2)
print("------------------------------------")
# 对列表型元素进行操作
list_1[1].remove(44)
list_2[1] += [55, 66]
print("list_1: ", list_1)
print("list_2: ", list_2)
print("------------------------------------")
list_2[2] += (8, 9)
print("list_1: ", list_1)
print("list_2: ", list_2)
# 元组是不可变的，新增元组会指向一个新的元组地址'
print("------------------------------------")
# 对字典型元素进行操作
list_1[-2]["age"] = 18
print("list_1: ", list_1)
print("list_2: ", list_2)
print("------------------------------------")

# 引入深拷贝：将所有层级的相关元素全部复制，完全分开
import copy
list_1 = [1, [22, 33, 44], (5, 6, 7), {"name": "Sarah"}]
list_2 = copy.deepcopy(list_1)
list_1[-1]["age"] = 18
list_2[1] += [55, 66]
print("list_1: ", list_1)
print("list_2: ", list_2)
print("------------------------------------")
# 神秘的字典
# 快速的查找
import time

ls_1 = list(range(1000000))
ls_2 = list(range(500)) + [-10]*500

start = time.time()
count = 0
for n in ls_2:
    if n in ls_1:
        count += 1
end = time.time()
print("num: {}, count: {}, time: {}".format(len(ls_2), count, round(end-start, 2)))

print("------------------------------------")

d = {i:i for i in range(1000000)}
"""
这是一个Python的字典（dictionary）对象，名为`d`。
它包含了从0到999999的整数作为键，并且每个键对应的值也是相同的整数。

简单来说，这个字典将整数i映射到它自身，例如d[0]的值是0，d[1]的值是1，
以此类推，一直到d[999999]的值是999999。

这个字典的创建方式使用了字典推导式（dictionary comprehension），
通过循环遍历range(1000000)生成的整数序列，并将每个整数作为键和值插入字典中。
因此，该字典共有1000000个键值对。
"""
start = time.time()
count = 0
for n in ls_2:
    try:
        d[n]
    except:
        pass
    else:
        count += 1
end = time.time()
print("num: {}, count: {}, time: {}".format(len(ls_2), count, round(end-start, 2)))
print("------------------------------------")
# 字典的底层实现
# 通过稀疏数组来实现值的存储与访问
# 字典的创建过程
# 第一步：创建一个散列表(稀疏数组N >> n)
d = {}
# 第二步：通过hash()计算键的散列值
print(hash("Python"))
print(hash(1120))
print(hash((2, 4)))
d["age"] = 18   # 增加键值对的操作，首先会计算键的散列值
print(hash("age"))
print("------------------------------------")
# 第二步：通过计算的散列值确定其在散列表中的位置
# 极个别时，散列值会发生冲突，但内部有解决方法
# 第三步：在该位置上存入值

# 键值对访问过程
"""
第一步：计算访问的键的散列值
第二步：根据计算结果，确定在散列表中的位置
第三步：读取在位置上存储的值
"""

# 小结：
"""
1. 字典的数据类型，通过空间换时间，实现了快速的数据查找
2. 因为散列值对应位置的顺序与键在字典中现实的顺序可能不同，因此表现出来字典是无序的
"""

# 紧凑的字符串：通过紧凑数组实现对字符的存储
# 数组在内存中连续存放，效率更高，节省空间
# 是否可变
# 不变类型：数字，字符串，元组：在生命周期内保持内容不变
# 改变了就不是自己了(id变了)
# 不可变对象的 += 实际创建了一个新的对象

x = 1
y = "Python"
print("x id: ", id(x))
print("y id: ", id(y))
x += 2
y += " Good!"
print("x id: ", id(x))
print("y id: ", id(y))

print("------------------------------------")

# 元组并不是总是不可变的
# 不可变的元组：里面的元素类型为真正的不可变时，才是不可变
# 可变类型：列表，字典，集合
ls = [1, 2, 3]
d = {"Name": "Sarah", "Age": 18}
print("ls id: ", id(ls))
print("d id: ", id(d))
ls += [4, 5]
d_2 = {"Sex": "female"}
d.update(d_2)
print("ls id: ", id(ls))
print("d id: ", id(d))
print("------------------------------------")

# 列表操作的几个小例子
# 删除列表内的特定元素

# 存在运算删除法：每次存在运算，都要对列表进行遍历，查找，效率低
alist = ["d", "d", "d", "2", "2", "d", "d", "4", "d"]
s = "d"
while True:
    if s in alist:
        alist.remove(s)
    else:
        break
print(alist)

print("------------------------------------")

# 一次性遍历元素执行删除
alist = ["d", "d", "d", "2", "2", "d", "d", "4", "d"]
for s in alist:
    if s == "d":
        alist.remove(s)
print(alist)

"""
运行该程序会出现意外结果。使用 `remove()` 函数从列表中删除元素时，会改变原始列表的长度和索引，导致迭代过程中的错误。

在这个例子中，首先会移除第一个 "d" 元素，然后将列表的长度从 9 缩短为 8，接着进入下一个迭代步骤。由于长度已经发生了变化，迭代器无法正确地访问到下一个元素，导致产生错误。

如果你想要删除列表中所有的 "d" 元素，可以使用一个辅助列表或者列表推导式来实现，以避免在迭代过程中修改原始列表。以下是一个示例代码：

```python
alist = ["d", "d", "d", "2", "2", "d", "d", "4", "d"]
alist = [s for s in alist if s != "d"]
print(alist)
```

这段代码使用列表推导式创建了一个新的列表，其中排除了所有等于 "d" 的元素。输出结果会是 `['2', '2', '4']`。
"""
print("------------------------------------")

alist = ["d", "d", "d", "2", "2", "d", "d", "4", "d"]
"""
这段代码是一个列表推导式（List comprehension），它用于过滤列表中的元素。

具体来说，`alist` 是一个列表变量，而 `s` 是迭代变量。代码的意思是，遍历 `alist` 中的每个元素，并将其赋值给 `s`。然后，检查当前的 `s` 是否不等于字符串 "d"，如果不等于，则保留该元素，并将其添加到一个新的列表中。

换句话说，这行代码将从 `alist` 列表中删除所有值为字符串 "d" 的元素，并返回一个新的列表，该列表包含了除去值为 "d" 的元素之外的其他元素。
"""
alist = [s for s in alist if s != "d"]
print(alist)

print("------------------------------------")

# 针对remove()过程中发现会有迭代失误的状况
# 解决方法：使用负向索引：无论长度怎么变，从后面计数的长度不会变
alist = ["d", "d", "d", "2", "2", "d", "d", "4", "d"]
for i in range(-len(alist), 0):
    if alist[i] == "d":
        alist.remove(alist[i])
print(alist)

print("------------------------------------")

# 多维列表的创建
ls = [[0]*10]*5
print(ls)
ls = [[0]*10]
print(ls)
ls[0][0] = 1
print(ls)

print("------------------------------------")

# 创建 更加简洁的语法
# 解析语法
ls = [[0]*10 for i in range(5)]
print(ls)

print("------------------------------------")

ls[0][0] = 1
print(ls)

print("------------------------------------")

# 解析语法：
# [expression for value in iterable if condition]
# 表达式， 可迭代对象， if条件
"""
执行过程:
1. 从可迭代对象中拿出一个元素
2. 通过if元素对元素value进行筛选
3. 将value传入表达式进行处理，产生一个结果
4. 将3步产生的结果作为列表的一个元素进行储存
5. 重复，知道迭代结束，返回新创建的列表
"""
# 求20以内奇数的平方
squares = []
for i in range(1, 21):
    if i % 2 == 1:
        squares.append(i**2)
print(squares)

print("------------------------------------")

squares  = [i**2 for i in range(1, 21) if i % 2 == 1]
print(squares)

print("------------------------------------")

# 支持多变量
x = [1, 2, 3]
y = [1, 2, 3]

results = [i*j for i, j in zip(x, y)]
print(results)

print("------------------------------------")

# 支持嵌套循环
colors = ["black", "white"]
sizes = ["S", "M", "L"]
tshirts = ["{} {}".format(color, size) for color in colors for size in sizes]
print(tshirts)

print("------------------------------------")

# 解析语法构造字典
squares = {i: i**2 for i in range(10)}
for k, v in squares.items():
    print(k, ": ", v)

print("------------------------------------")

# 解析语法构造集合
squares = {i**2 for i in range(10)}
print(squares)

print("------------------------------------")

# 生成器类型
squares = (i**2 for i in range(10))
print(squares)

print("------------------------------------")

# 生成器类型迭代
colors = ["black", "white"]
sizes = ["S", "M", "L"]
tshirts = ("{} {}".format(color, size) for color in colors for size in sizes)
for tshirt in tshirts:
    print(tshirt)
print(tshirts)  # 生成器

print("------------------------------------")

# 条件表达式
# expr1 if condition else expr2
n  = -10
x = n if n >= 0 else -n
print(x)

print("------------------------------------")

# 生成器
ls = [i**2 for i in range(1, 1000001)]
for i in ls:
    pass

"""
缺点： 占用大量内存
生成器：
1. 采用惰性计算的方式
2. 无需一次性存储海量数据
3. 一边执行一边计算，只需算每次需要的值
4. 实际上一直在执行next()操作，直到无值可取
"""

# 生成器表达式
# 海量数据，无需存储
# 求 0 - 100 的和
print(sum((i for i in range(101))))

print("------------------------------------")

# 生成器函数 yiel： 生成斐波那且数列
def fib(max):
    ls = []
    n, a, b = 0, 1, 1
    while n < max:
        ls.append(a)
        a, b = b, a + b
        n += 1
    return ls

print(fib(10))

print("------------------------------------")

def fib01(max):
    n, a, b = 0, 1, 1
    while n < max:
        print(a)
        a, b = b, a + b
        n += 1

fib01(10)

print("------------------------------------")

def fib02(max):
    n, a, b = 0, 1, 1
    while n < max:
        yield(a)
        a, b = b, a + b
        n += 1
# 每次调用next()的时候执行，遇到yield()语句返回，再次执行时从上次返回的yield()语句处继续执行
# 获得生成器
print(fib02(10))
# 对生成器进行遍历
for i in fib02(10):
    print(i)

print("------------------------------------")

# 可迭代对象
# 可直接用于for循环的对象统称为可迭代对象:iterable
# 1. 列表，元组，字符串，字典，集合，文件
# 可以使用 isinstance() 判断
from collections.abc import Iterable
print(isinstance([1, 2, 3], Iterable))
print(isinstance({"Name": "Sarah"}, Iterable))
print(isinstance("Python", Iterable))

print("------------------------------------")

# 2. 生成器
squares = (i**2 for i in range(5))
print(isinstance(squares, Iterable))

# 生成器不但可用于for循环，还可以被 next() 对象调用
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
# 知道没有数据读取，抛出 StopIteration
try:
    print(next(squares))
except StopIteration as e:
    print(e)
# 可以被 next() 函数调用并不断返回下一个值，知道没有数据可以读取的对象称为迭代器 Iterator

print("------------------------------------")

# 迭代器
# 1. 生成器都是迭代器
# 2. 列表，元组，字符串，字典，集合不是迭代器
from collections.abc import Iterator
print(isinstance([1, 2, 3], Iterator))

# 可通过 iter(iterable) 创建迭代器
print(isinstance(iter([1, 2, 3]), Iterator))

"""
for item in Iterable等价于
先通过 iter() 函数获得可迭代对象 Iterable 的迭代器
然后对获取到的迭代器不断调用 next() 方法来获取下一个值并将其赋值给 item
当遇到 StopIteration 的异常循环后结束
"""

print("------------------------------------")

# zip enumerate 等 itertools 里的函数都是迭代器

x = [1, 2]
y = ['a', 'b']
print(zip(x, y))

for i in zip(x, y):
    print(i)

print(isinstance(zip(x, y), Iterator))

numbers = [1, 2, 3, 4, 5]
print(enumerate(numbers))

for i in enumerate(numbers):
    print(i)
print(isinstance(enumerate(numbers), Iterator))

print("------------------------------------")

# 文件是迭代器
with open("测试文件.txt", "r", encoding="utf-8") as f:
    print(isinstance(f, Iterator))

print("------------------------------------")

# 迭代器是可耗尽的
squares = (i**2 for i in  range(5))
for square in squares:
    print(square)
for square in squares:
    print(square)

print("------------------------------------")

# range() 不是迭代器
numbers = range(10)
print(isinstance(numbers, Iterator))

print(len(numbers)) # 有长度
print(numbers[0])   # 可索引
print(9 in numbers) # 可存在计算
try:
    next(numbers)   # 不可被 next() 调用
    """'range' object is not an iterator"""
except Exception as e:
    print(e)

for number in numbers:
    print(number)

# 不会被耗尽
for number in numbers:
    print(number)

"""
range() 
它是一种序列
但并不包含任何内存中的内容
而是通过计算来回答
"""

print("------------------------------------")

# 装饰器
"""
需求的提出：
1. 需要对已开发上线的程序添加某些功能
2. 不能对程序中函数的源代码进行修改
3. 不能改变程序中函数的调用
"""
# 比如说，要统计每个函数的运行时间
# 函数对象：是Python中的第一类对象
# 1. 可以把函数赋值给变量
# 2. 对该变量进行调用，可实现原函数的功能
def square01(x):
    return x**2

print(type(square01))

pow_2 = square01    # 可以理解给这个函数起了个别名
print(square01(5))
print(pow_2(5))

# 可以作为函数的参数进行传递

print("------------------------------------")

# 高阶函数
# 1. 接收函数作为参数
# 2. 或者返回一个函数
# 满足上述条件之一的函数称之为高阶函数
def pow_2(fun):
    return fun

f = pow_2(square01)
print(f(8))

print(f == square01)

print("------------------------------------")

# 嵌套函数：在函数内部定义一个函数
def outer():
    print("outer is running")

    def inner():
        print("inner is running")

    inner()

outer()

print("------------------------------------")

# 闭包
"""
def outer():
    x = 1
    z = 10

    def inner():
        y = x + 100
        return y, z

    return inner()

f = outer() # 实际上f包含了inner函数本身outer函数的环境
print(f)

print(f.__closure__)    # 包含了来自外部函数的信息
for i in f.__closure__:
    print(i.cell_contents)

res = f()
print(res)

The error you're encountering is because f is a tuple, 
not a function, and tuples do not have the __closure__ attribute. 
In your code, outer() returns the result of calling inner(), 
which is a tuple containing the values returned by inner(). 
It does not return the inner function itself.

If you want to access the closure of the inner function, 
you need to assign the inner function itself to f, like this:
"""
def outer():
    x = 1
    z = 10

    def inner():
        y = x + 100
        return y, z

    return inner

f = outer()  # Assign inner function to f

print(f.__closure__)  # Closure information of the inner function
for i in f.__closure__:
    print(i.cell_contents)

res = f()
print(res)

"""
在计算机科学中，__closure__是指存储在函数对象中的自由变量的引用。当一个函数定义在另一个函数内部时，内部函数可以访问外部函数中定义的变量。当外部函数执行完毕后，这些变量可能会被销毁，但如果内部函数仍然存在并且引用了这些变量，Python将会创建一个闭包（closure），将这些变量的引用保存在函数对象的__closure__属性中。

闭包使得内部函数可以继续访问外部函数的变量，即使外部函数已经执行完毕并且其作用域已经消失。这对于实现某些特定的编程模式非常有用，例如函数工厂、装饰器等。

在Python中，通过访问函数对象的__closure__属性，可以获取该函数的闭包。每个闭包都是一个单元素元组，其中包含了自由变量的cell对象，可以通过cell_contents属性获取实际的值。

下面是一个简单的示例代码，演示了如何使用闭包：

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)  # 输出15
```

在上述示例中，outer_function返回了inner_function，并且inner_function引用了外部函数的变量x。即使outer_function已经执行完毕，我们依然可以使用closure来调用inner_function，并且访问到x的值。这就是闭包的作用。"""

# 闭包：延伸了作用域的函数
# 如果一个函数定义在另一个函数的作用域内，并且引用了外层函数的变量，则该函数称为闭包
# 闭包是由函数及其相关的引用环境组合而成的实体

print("------------------------------------")

# 一旦在内层函数重新定义了相同名字的变量，则该变量称为局部变量
"""
def outer():
    x = 1

    def inner():
        x = x + 100
        return x    # 称为局部变量，会报错

    return inner

f = outer()
f()
"""
# nonlocal 允许内嵌的函数来修改闭包变量
def outer():
    x = 1

    def inner():
        nonlocal  x
        x = x + 100
        return x

    return inner

f = outer()
print(f.__closure__)
res = f()
print(res)

print("------------------------------------")

# 一个简单的装饰器
# 嵌套函数的实现
import time

def timer(func):

    def inner():
        print("inner run")
        start = time.time()
        func()
        end = time.time()
        print("{} 函数运行时间{:.2f}秒".format(func.__name__, (end - start)))

    return inner

def f1():
    print("f1 run")
    time.sleep(1)

f1 = timer(f1)
f1()

print("------------------------------------")

# 语法篇
@timer
def f2():   # 相当于实现了 f2 = timer(f2)
    print("f2 run")
    time.sleep(1)

f2()

print("------------------------------------")

# 装饰有参函数

def timing(func):

    def inner(*args, **kwargs): # 使内部函数也接受函数
        print("inner run")
        start = time.time()
        func(*args, **kwargs)   # 也接受函数输入
        end = time.time()
        print("{} 函数运行时间{:.2f}秒".format(func.__name__, (end - start)))

    return inner

@ timing
def f1(n):  # 存在输入参数
    print("f1 run")
    time.sleep(n)

f1(2)

print("------------------------------------")

# 被装饰函数有返回值情况
def timing01(func):

    def inner(*args, **kwargs): # 使内部函数也接受函数
        print("inner run")
        start = time.time()
        res = func(*args, **kwargs)   # 也接受函数输入
        end = time.time()
        print("{} 函数运行时间{:.2f}秒".format(func.__name__, (end - start)))
        return res

    return inner

@ timing01
def f1(n):  # 存在输入参数
    print("f1 run")
    time.sleep(n)
    return "wake up"

res = f1(2)
print(res)

print("------------------------------------")

# 带参数的装饰器
# 装饰器本身需要传递一些额外参数
# 需求： 有时需要统计绝对时间，有时需要统计绝对时间的2倍

def timing(method):

    def outer(func):
        def inner(*args, **kwargs): # 使内部函数也接受函数
            print("inner run")
            if method == "origin":
                print("origin_inner run")
                start = time.time()
                res = func(*args, **kwargs)  # 也接受函数输入
                end = time.time()
                print("{} 函数运行时间{:.2f}秒".format(func.__name__, (end - start)))
            elif method == "double":
                print("double_inner run")
                start = time.time()
                res = func(*args, **kwargs)  # 也接受函数输入
                end = time.time()
                print("{} 函数运行时间{:.2f}秒".format(func.__name__, 2*(end - start)))
            return res
        return inner
    return outer

@ timing(method="origin")
def f1(n):  # 存在输入参数
    print("f1 run")
    time.sleep(n)
    return "wake up"

@ timing(method="double")   # 相当于执行了 timing = timing(method="origin") f1 = timing(f1)
def f2(n):  # 存在输入参数
    print("f1 run")
    time.sleep(n)
    return "wake up"

res = f1(2)
print(res)
res = f2(2)
print(res)

print("------------------------------------")

# 何时执行装饰器
# 一装饰就执行，不必等调用
func_name = []
def find_function(func):
    print("run")
    func_name.append(func)
    return func

@find_function
def f1():
    print("f1 run")

@find_function
def f2():
    print("f2 run")

@find_function
def f3():
    print("f3 run")

for func in func_name:
    print(func)
    func()

print("------------------------------------")

def timing(func):

    def inner():
        print("inner run")
        start = time.time()
        func()
        end = time.time()
        print("{} 函数运行时间{:.2f}秒".format(func.__name__, (end - start)))

    return inner

@ timing
def f1(n):  # 存在输入参数
    print("f1 run")
    time.sleep(n)

print(f1.__name__)  # inner， 不是源源本本的 f1

print("------------------------------------")

from functools import wraps

"""
`@wraps(func)` 是一个装饰器，它用于将被装饰函数的元信息（比如函数名、文档字符串等）复制到装饰器函数中。它的作用是确保被装饰后的函数在使用时不会丢失原始函数的信息。

当你使用装饰器来包装一个函数时，通常会改变原始函数的一些属性，比如函数名、文档字符串、参数签名等。这可能会导致一些问题，例如在调试或者文档生成时无法正确识别被装饰函数的信息。

通过使用`@wraps(func)` 装饰器，可以解决这个问题。它会将原始函数的元信息复制给装饰器函数，从而使得装饰后的函数与原始函数具有相同的属性。这样，在调试或者文档生成时，就能够正确地识别被装饰函数的信息了。

示例：
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 在这里执行一些装饰器的操作
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    ""这是我的函数""
    pass

print(my_function.__name__)  # 输出 "my_function"
print(my_function.__doc__)   # 输出 "这是我的函数"
```

可以看到，通过使用`@wraps(func)` 装饰器，被装饰函数 `my_function` 的元信息被正确地复制到了装饰器函数 `wrapper` 上。
"""

def timing(func):
    @wraps(func)    # 装饰后函数的属性仍然是原来的函数
    def inner():
        print("inner run")
        start = time.time()
        func()
        end = time.time()
        print("{} 函数运行时间{:.2f}秒".format(func.__name__, (end - start)))

    return inner

@ timing
def f1(n):  # 存在输入参数
    print("f1 run")
    time.sleep(n)

print(f1.__name__)  # f1

print("------------------------------------")
