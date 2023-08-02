# BOOL
# 逻辑运算的结果
a = 10
print(a > 5)
print(a == 12)
print(a < 5)
# any() all()
print(any([False, 1, 0, None]))  # False 0 None 都是无
print(all([False, 1, 0, None]))

# 指示条件：作为判断或者循环的指示条件
n = 2800
while True:
    m = eval(input("请输入一个数字: "))
    if m == n:
        print("猜对了！！！")
        break
    elif m > n:
        print("太大了")
    else:
        print("太小了")

# 作为掩码
import numpy as np
x = np.array([[1, 3, 2, 5, 7]]) # 定义numpy数组
print(x > 3)  # 将二维数组里的每一个元素与3进行对比，得到掩码
print(x[x > 3])  # 通过掩码，把大于3的数跳出来，用True

# 类型判别及类型转换
# 类型判别
age = 20
name = "Ada"
print(type(age))
print(type(name))
# isinstance(变量，预判类型) 承认继承
# 变量类型为预判类型的子类型，则为真，否则为假
# isinstance判断的是这个量是不是这个类的实例
print(isinstance(age, int))
print(isinstance(age, float))
print(isinstance(age, object))
print(isinstance(name, object))
# 字符串是不是只有数字组成
age = "30112"
name = "Ada"
print(age.isdigit())
print(name.isalpha())
age = "3123asda"
print(age.isalnum())    # 比如，可用于判断用户名是否合法
# 类型转换
# 数字类型转字符串类型
age = "20"
print("My age is " + str(age))
# 仅有数字组成的字符串转数字 int() float() eval()
s1 = "10"
s2 = "15.5"
print(int(s1))
print(float(s2))

