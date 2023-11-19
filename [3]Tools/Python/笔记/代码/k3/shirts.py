# 练习

def make_shirt(sentence='I love Python', size='big'):
    print(f'We have made a {size} T-shirt with {sentence}.')

make_shirt()
make_shirt(size='middle')
make_shirt(sentence='I love Java')

#
# Python 提供了一种类似于 C++ 中的可变参数的功能，即使用 `*args` 和 `**kwargs` 来处理可变数量的参数。
#
# 1. **`*args`（用于接收可变数量的位置参数）:**
#
#    ```python
#    def example(*args):
#        for arg in args:
#            print(arg)
#
#    # 调用函数时，可以传递任意数量的参数
#    example(1, 2, 3)  # 输出: 1 \n 2 \n 3
#    ```
#
# 2. **`**kwargs`（用于接收可变数量的关键字参数）:**
#
#    ```python
#    def example(**kwargs):
#        for key, value in kwargs.items():
#            print(key, ":", value)
#
#    # 调用函数时，可以传递任意数量的关键字参数
#    example(name="John", age=25, city="New York")
#    # 输出:
#    # name : John
#    # age : 25
#    # city : New York
#    ```
#
# 3. **同时使用 `*args` 和 `**kwargs`:**
#
#    ```python
#    def example(*args, **kwargs):
#        for arg in args:
#            print(arg)
#        for key, value in kwargs.items():
#            print(key, ":", value)
#
#    # 调用函数时，可以传递任意数量的位置参数和关键字参数
#    example(1, 2, 3, name="John", age=25)
#    # 输出:
#    # 1
#    # 2
#    # 3
#    # name : John
#    # age : 25
#    ```
#
# 这样的定义方式允许你在调用函数时传递任意数量的参数。`*args` 接收位置参数，`**kwargs` 接收关键字参数。你可以根据实际需要选择使用其中之一或两者结合使用。