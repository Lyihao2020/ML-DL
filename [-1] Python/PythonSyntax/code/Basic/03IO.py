# 输入输出
# 程序中定义
age = 18
name = "Tom"

# 动态交互输入 input
age = input("年龄: ")
name = input("姓名: ")
print(age)
print(name)
# 但从input输入得到的是字符串
x = input("请输入一个数字: ")
y = input("请输入一个数字: ")
print(x + y)    # 输出得到的是两个数字的拼接
# 所以eval()去掉引号
print(eval(x) + eval(y))

# 数据输出
# print默认换行
# print换行控制
print(123, end = '')
print(456)

# 简单的打印组合
PI = 3.1415926
E = 2.71828
print("PI = ", PI, "E = ", E)

# 格式化输出方法 format
# 基本格式："字符{0}字符{1}字符".format(v0, v1)
# 基本格式："字符{0:修饰}字符{1:修饰}字符".format(v0, v1)
# : 引导符号
# 严格按照顺序 :<填充字符><对齐><宽度><,><.精度>
# <.精度> 代表浮点数小数位数， 字符最大输出长度
print("PI = {0}, E = {1}".format(PI, E))
# 交换一下位置
print("PI = {1}, E = {0}".format(PI, E))
# 默认缺省
print("PI = {}, E = {}".format(PI, E))

# 填充输出
# _____3.1415926______ 进行填充
print("{0:_^20}".format(PI)) # 0表示数据PI，_表示填充字符，^表示居中，20代表输出宽度
print("{0:*<30}".format(PI))
print("{0:&>20}".format(PI))

# 数字千分位分隔符
# 显示 10，000，000
print("{0:,}".format(10000000))
print("{0:*<20,}".format(10000000)) # 逗号一定要在最后

# 浮点数简化输出
# 留2位小数
print("{0:.2f}".format(PI))
# 百分数输出
print("{0:.1%}".format(0.818727))
# 科学技术法输出
print("{0:.2e}".format(0.818727))

# 整数的进制转换输出
print("二进制{0:b}，Unicode码{0:c}，十进制{0:d}，八进制{0:o}，十六进制{0:x}".format(450))
