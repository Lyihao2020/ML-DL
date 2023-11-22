# 骰子练习
from random import randint
"""
`randint(a, b)` 函数用于生成一个介于 `a` 和 `b` 之间的随机整数，包括 `a` 和 `b`。

具体而言，`randint(a, b)` 生成的随机整数的范围是 `[a, b]`，即包括 `a` 和 `b`。左右区间都是闭合的。

例如，`randint(1, 10)` 可以生成 1、2、3、4、5、6、7、8、9、10 中的任意一个整数。

`random` 模块中的 `random()` 函数用于生成一个位于 `[0.0, 1.0)` 范围内的随机浮点数。这个范围是左闭右开的，也就是说，包括 0.0，但不包括 1.0。

```python
import random

# 生成一个随机浮点数，范围在 [0.0, 1.0)
random_number = random.random()

print(random_number)
```

这样的生成方式意味着生成的随机数可能是 0.0，但永远不会是 1.0。如果你希望包括右边界，你可以使用 `uniform(a, b)` 函数，它生成一个在 `[a, b]` 范围内的随机浮点数，包括 `a` 和 `b`。

```python
import random

# 生成一个在 [1.0, 10.0] 范围内的随机浮点数
random_number = random.uniform(1.0, 10.0)

print(random_number)
```

这样的情况下，生成的随机数可能是 1.0，也可能是 10.0。

"""

class Die():    # 类名采用驼峰命名法，即将类名中每个单词的首字母都大写，而不使用下划线
    """创建随机数"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, times=10):
        print(f'\nTimes: {times}')
        for i in range(times):
            print(f'\t{randint(1, self.sides)}')

if __name__ == '__main__':
    new_die1 = Die(10)  # 实例名和模块名都采用小写格式，并在单词之间加入下划线
    new_die1.roll_die(10)
    new_die2 = Die(20)
    new_die2.roll_die(10)

"""
对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，
并遵储编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。

可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。

需要同时导入标准库中的模块和你编写的模块时，先编写导人标准库模块的import语句，
再添加一个空行，然后编写导人你自己编写的模块的import语句。
在包含多条import语向的程序中，这种做法让人更容易明白程序使用的各个模块都来自何方。
"""
