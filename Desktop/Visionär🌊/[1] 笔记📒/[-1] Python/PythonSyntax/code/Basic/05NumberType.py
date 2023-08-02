# 数字类型
# 整数 - 不同进制的转换
a = bin(16) # 转二进制
b = oct(16) # 转八进制
c = hex(16) # 转十六进制
print("{0}  {1}  {2}".format(a, b, c))
print(a == b == c) # False, 因为转换后结果为字符串类型
type(a)

# 其他进制转十进制
d = int(a, 2)
e = int(b, 8)
f = int(c, 16)
print("{0}  {1}  {2}".format(d, e, f))

# 浮点数
print((0.1 + 0.2) == 0.3) # False
# 浮点数运算存在小数问题，计算机采用二进制小数来表示浮点数的小数部分
# 部分小数不能用二进制小数完全表示
# 通常情况下不会影响计算精度
print(0.1 + 0.2)
# 使用四舍五入的方法来获得精确解
a = 3 * 0.1
print(a)
b = round(a, 1) # 后面的 1 代表着保留一位小数
print(b)
print(b == 0.3)

# 复数
# 当虚部系数为 1 时，需要显示写出
print(2 + 1j)

# 运算符部分
# 乘方运算
print(2**3)
# 整数商 // 和 模运算 %
print(13//5)
print(13 % 5)
# 整数与浮点数运算结果是浮点数
# 除法运算的结果是浮点数
print(1 + 1.5)
print(2/5)
print(8/4)

# 数字运算操作函数
print(abs(-5))
print(pow(2, 5)) # 2**5
print(pow(2, 5, 3)) # 2**5 % 3
# 四舍五入函数
a = 1.618
print(round(a)) # 默认四舍五入为整数
print(round(a, 2)) # 参数 2 表示四舍五入后保留 2 位小数
print(round(a, 5)) # 位数不足，无需补齐
# 整数商和模运算 divmod(x,y) 等价返回 （x//y, x%y)
print(divmod(13, 5))
# 序列最大值最小值
a = [3, 3, 2, 4, 5, 7, 2, 1, 3]
print("max: ", max(a))
print("min: ", min(a))
# 求和sum函数
print(sum(a))

# 借助科学计算库 math/ scipy/ numpy
import math
print(math.exp(1))
print(math.log2(2))
print(math.sqrt(4))

import numpy as np
print(np.mean(a)) # 求 平均值
print(np.median(a)) # 求中位数
print(np.std(a)) # 求标准差



