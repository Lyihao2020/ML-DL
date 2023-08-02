# 字符串
# 双中有单
print("I'm 18 years old")

# 单中有双
print('"Python" is good')

# 双中有双，单中有单（使用转义符 \ ）
print("\"Python\" is good")
print('\'P\' is P')

# 转义符可以用换行继续输入
s = "py" \
    "thon"
print(s)

# 字符串的性质
s = "My name is Peppa Pig."
print(s[0])
print(s[4])
print(s[-1])
# 字符串的切片
# 变量名[开始位置:结束位置:切片间隔]
# 切片范围不包含结束位置
s = "Python"
print(s[0:3:1])
# 起始位置是0，可以忽略
# 结束位置忽略，代表可以取到最后一个字符
# 可以使用反向索引
print(s[0:6])
print(s[:6])
print(s[:])
print(s[-6:])

# 反向切片
# 起始位置是-1也可以省略
# 结束位置省略，代表可以取到第一个字符
s = "123456789"
print(s[-1:-10]) # 无显示是因为默认间隔为1，导致取不到数字
print(s[-1:-10:-1])
print(s[:-10:-1])
print(s[::-1])

# 字符串操作符
a = "I love "
b = "Python"
print(a + b)
# 字符串成倍复制
c = a + b
print(3 * c)
print(c * 3)

# 成员运算
# 子集in全集：任何一个连续的切片都是原字符串的子集
folk_singers = "Peter, Paul and Mary"
print("Peter" in folk_singers)

# 遍历字符串字符 for 字符 in 字符串:
for s in "Python": # 获取每一个字符串并输出
    print(s)

# 字符串处理函数
# 字符串长度
print(len(folk_singers))
# 字符编码：将字符串转化为Unicode码（ord（字符））
# 每一个单一字符对应一个唯一的互不重复的二进制编码
# Python中使用的是Unicode编码
print(ord("1"))
print(ord("a"))
print(ord("*"))
print(ord("中"))
print(ord("国"))
# 将Unicode码转换为字符
print(chr(48))
print(chr(65))

# 字符串的处理方法：会返回一个返回值，原本的字符串不变
# 字符串的分割：1. 返回一个列表 2. 原字符串不变
languages = "Python C C++ Java PHP R"
languages_list = languages.split(" ")
print(languages)
print(languages_list)
# 字符串的聚合：1. 可迭代类型，如字符串，列表，元组等 2. 序列类型的元素必须是字符类型
s = "12345"
s_join = ",".join(s)
print(s_join)
# s = [1, 2, 3, 4, 5] 数字类型不可以聚合哦
s = ["1", "2", "3", "4", "5"]
s_join = "*".join(s)
print(s_join)
# 删除字符串两端特定字符 strip方法
s = "              I have many blanks       "
print(s.strip(" "))
print(s.lstrip(" "))
print(s.rstrip(" "))
# 字符串的替代 replace方法
s = "Python is coming."
s1 = s.replace("Python", "Py")
print(s1)
# 字符串统计 count方法
s = "Python is an excellent language"
print("an: ", s.count("an"))
print("e: ", s.count("e"))
# 字符串大小写
s = "Python"
print(s.upper()) # 全部大写
print(s.lower()) # 全部小写
print(s.title()) # 首字母大写
