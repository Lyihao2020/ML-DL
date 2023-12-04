# 将函数储存在模块中
# 导入整个模块
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入特定的函数
# from module_name import function_name0, function_name1, ...

# 使用as给函数指定别名
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as给模块指定别名
import pizza as p
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
p.make_pizza(16, 'pepperoni')

# 倒入所有的函数
from pizza import *

"""
应给函数指定描述性名称，且只在其中使用小写字母和下划线。
描述性名称可帮助你和别人明白代码想要做什么。给模块命名时也应遵循上述约定。

每个函数都应包含简要地阐述其功能的注释，该注释应紫跟在两数定义后面，并采用文档字符串格式。
文档良好的描述让其他程序员只需阅读文档字符串中的描述就能够使用它：他们完全可以相信代码如描述的那样运行；
只要知道两数的名称、需要的实参以区返回值的类型，就能在自己的程序中使用它。
给形参指定默认值时，等号两边不要有空格：
def function_name(parameter_0, parameter_1='default value')

如果函数的参数很多，则按照下面的格式进行编写：
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function_body...
    
如果模块或函数包含多个函数，可使用两个空行将相邻的函数分开
所有的import都应该放在文件开头，除非，文件开头使用了注释来描述程序
"""