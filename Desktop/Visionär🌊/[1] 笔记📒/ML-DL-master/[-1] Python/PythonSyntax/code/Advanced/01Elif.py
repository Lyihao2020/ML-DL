# 程序控制结构
# 条件测试
# 比较运算
a = 10
b = 8
print(a > b)
print(a < b)
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)
# 非空
ls = []
if ls:
    print("非空")
else:
    print("空的")
# 逻辑运算
# 与，或，非
a = 10
b = 8
c = 12
print((a > b) and (b > c))
print((a > b) or (b > c))
print(not(a > b))
# 复合逻辑运算的优先级 非 > 与 > 或
print(True or True and False)
print((True or True) and False)
# 存在运算
cars = ["BYD", "BWM", "AUDI", "TOYOTA"]
print("BYD" in cars)
print("BENZ" in cars)
print("BYD" not in cars)
print("BENZ" not in cars)

# if语句
# 单分支
age = 8
if age > 7:
    print("OK")

# 多分支
if age < 9:
    print("OK")
elif age < 13:
    print("OK!")
else:
    print("NO")

# 嵌套语句
# 题目：年满18周岁，在非公众场合可以抽烟，判断下列情形是否可以抽烟
age = eval(input("请输入你的年龄:"))
if age > 18:
    is_public_place = bool(eval(input("公共场所请输入1，非公共场所请输入0")))
    if not is_public_place:
        print("可以抽烟")
    else:
        print("不可以抽烟")
else:
    print("不可以抽烟")

# for循环
# 直接迭代-列表[], 元组(), 集合{}, 字符串""
graduates = ("李雷", "韩梅梅", "Jim")
for graduate in graduates:
    print("Congratulations, " + graduate)
# 变换迭代-字典
students = {201901: '小明', 201901: '小红', 201903: '小强'}
for k, v in students.items():
    print(k, v)
for student in students:
    print(student)
# range()对象
res = []
for i in range(200):
    res.append(i**2)
print(res[:5])
res = []
for i in range(1, 10, 2):
    res.append(i**2)
print(res)

# break 和 continue
product_scores = [89, 90, 99, 70, 67, 78, 85, 92, 77, 82]   # 1组10个产品的性能评分
# 如果低于75分的产品超过2个，则该组产品不合格
i = 0
for score in product_scores:
    if score < 75:
        i += 1
    if i == 2:
        print("产品抽检不合格")
        break
else:   # 没有被break中止，则执行else块
    print("产品抽检合格")

product_scores = [89, 90, 99, 70, 67, 78, 85, 92, 77, 82]   # 1组10个产品的性能评分
# 如果低于75分的产品超过2个，则该组产品不合格
bad_products = []
for i in range(len(product_scores)):
    if product_scores[i] > 75:
        continue
    print("第{0}个产品抽检结果不合格，分数为{1}".format(i, product_scores[i]))

# 无限循环 while
albert_age = 18
guess = eval(input("请输出猜测的数字"))
while guess != albert_age:
    if guess > albert_age:
        print("Too big")
    else:
        print("Too small")
    guess = eval(input("请输出猜测的数字"))
else:
    print("Congratulations.")

# 使用flag
albert_age = 18
flag = True
while flag:
    guess = eval(input("请输出猜测的数字"))
    if guess > albert_age:
        print("Too big")
    elif guess < albert_age:
        print("Too small")
    else:
        print("Congratulations.")
        flag = False

flag = True
while flag:
    pass
    while flag:
        pass
        while flag:
            flag = False

# while, break, continue
albert_age = 18
flag = True
while flag:
    guess = eval(input("请输出猜测的数字"))
    if guess > albert_age:
        print("Too big")
    elif guess < albert_age:
        print("Too small")
    else:
        print("Congratulations.")
        break

# 输出10以内的奇数
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# test example
pets = ["dog", "cat", "dog", "pig", "goldfish", "rabbit", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)

# 将未读书籍列表中的书名分别输出后，存入已读书籍列表
not_read = ["红楼梦", "水浒传", "三国演义", "西游记"]
have_read = []
while not_read:
    book = not_read.pop()
    have_read.append(book)
    print("我已经读过了《{0}》".format(book))
print(not_read)
print(have_read)

# 注意事项
# 尽可能减少多层嵌套
# 避免死循环
# 封装过于复杂的判断条件
# 可以考虑将条件判断封装为一个函数
numbers = (2, 1, 3, 2, False)
def judge(num):
    a, b, c, d, e = num
    x = a > b
    y = c > d
    z = not e
    return x and y and z

if judge(numbers):
    print("条件函数封装成功")