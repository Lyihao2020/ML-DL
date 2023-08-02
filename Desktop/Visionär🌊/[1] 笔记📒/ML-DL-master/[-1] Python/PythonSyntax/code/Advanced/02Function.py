# 函数
# 阶乘的函数表现形式
def factor(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(factor(5))
print(factor(20))

# 函数的定义及调用
# 三要素：参数，函数体，返回值
# 求正方形体积
def area_of_square(length_of_side):
    square_area = pow(length_of_side, 3)
    return square_area
print(area_of_square(3))

def function(x,y,z):
    return x * y * z
print(function(1,2,3))

# 关键字参数
# 打破位置限制，直接对参数进行赋值（形参 = 实参）
print(function(y=1, x=2, z=3))
# 不可以对一个形参重复传值
# function(1, z=3, x=2)

# 默认参数
# 在定义阶段就给形参赋予默认值
def register(name, age, sex = "male"):
    print(name, age, sex)

register("杰哥", 18)
# 默认参数应该设置为不可变类型
def function01(ls=[]):
    print(id(ls))
    ls.append(1)
    print(id(ls))
    print(ls)

function01()
function01()
function01()

def function02(ls="Python"):    # 每次程序进入使用的地址入口
    print(id(ls))
    ls += "3.7"
    print(id(ls))   # 地址更改了
    print(ls)

function02()
function02()    # 因为两个地址更改了，还是引用原来的地址，所以并没有重复叠加 3.7

# 让参数变成可选的
def name(first_name, last_name, middle_name=None):
    if middle_name:
        return first_name+middle_name+last_name
    else:
        return first_name+last_name
print(name("大", "仔"))
print(name("大", "蛋", "仔"))

# 可变长参数
# 不知道会传过来多少参数，该参数必须放在参数列表的后面
def foo(x, y, z, *args):
    print(x, y, z)
    print(args)

foo(1, 2, 3, 4, 5, 6)

# 实参打散
foo(1, 2, 3, [4, 5, 6])     # 列表赋值给元组
foo(1, 2, 3, *[4, 5, 6])    # 打散的是列表，字符串，元组或集合

# 可变长参数 **kwargs
def foo01(x, y, z, **kwargs):
    print(x, y, z)
    print(kwargs)

# 转换为字典的形式进行赋值
foo01(1, 2, 3, a=4, b=5, c=6)   # 在这里参数的传递要以赋值的方式进行传递
foo01(1, 2, 3, **{"a": 4, "b": 5, "c": 6})  # **打散以后又被组合成一个字典

# 可变长参数的组合使用：可以接受任意长度的参数
def foo02(*args, **kwargs):
    print(args)
    print(kwargs)

foo02(1, 2, 3, a=4, b=5, c=6)

# 函数体与变量作用域
# 局部变量-仅在函数体内部定义和发挥作用
def mutiply(x, y):
    z = x*y
    return z    # 函数执行完毕，局部变量z就被释放掉了
z = mutiply(2,9)    # 全部z不会被释放掉
print(z)
# 全局变量（可以在函数体内部直接使用，但如果重名，内部会将外部变量覆盖）
n = 3
ls = [0]
def mutiply01(x, y):
    global  z   # 使用global在函数体内部定义全局变量
    z = n * x * y
    ls.append(z)
    return z
print(mutiply(2, 9))
print(ls)
print(z)

# 返回值
# 多个返回值
def foo03(x = 1):
    return 1, x, x**2, x**3
a, b, c, d = foo03(3)
print(foo03(3))
print(a)
print(b)
print(c)
print(d)

# 可以有多个return语句，一旦执行其中一个，代表了函数运行的结束
# 没有return语句，返回值为None
def foo04():
    print("我是孙悟空")
res = foo04()
print(res)

# 几点建议
# 函数及其参数的命名参照变量的命名：字母小写及下划线组合，有实际意义
# 应包含简要函数定义概述
# 函数定义前后各空两行
def f1():
    # 这个函数的作用是...
    pass

# 函数式编程实例
# 自顶向下，分而治之
# 问题描述
# 小丹和小伟羽毛球都打得不错，基本上，打100个球，小丹能赢55次，小伟能赢45次
# 但每次到大型比赛（1局定胜负，谁先到21分就获胜），小丹赢的概率远远大于小伟
# 用模拟实验来解释原因
# 问题抽象
# 1. 小丹每球获胜概率55%，小伟每球获胜概率45%
# 2. 每局比赛，先赢21球者获胜
# 3. 假设进行n = 10000局独立比赛，小丹会获胜多少局？（n较大，实验期望=真实期望）
# 问题分解
import random
def main():
    #主要逻辑
    prob_A, prob_B, numbers_of_games = get_inputs() #获取真实数据
    win_A, win_B = sim_n_games(prob_A, prob_B, numbers_of_games)    #获取模拟结果
    print_summary(win_A, win_B, numbers_of_games)

# 输入原始数据
def get_inputs():
    prob_A = eval(input("请输入运动员A的每球获胜概率(0~1):"))
    prob_B = round(1-prob_A, 2) # 四舍五入，保留两位小数
    numbers_of_games = eval(input("请输入模拟的场次(正整数):"))
    print("模拟比赛总次数:", numbers_of_games)
    print("A选手每球获胜概率：", prob_A)
    print("B选手每球获胜概率：", prob_B)
    return prob_A, prob_B, numbers_of_games

# 多场比赛模拟
def sim_n_games(pro_A, pro_B, numbers_of_games):
    win_A, win_B = 0, 0
    for i in range(numbers_of_games):
        score_A, score_B = sim_one_game(pro_A, pro_B)
        if score_A > score_B:
            win_A += 1
        else:
            win_B += 1
    return win_A, win_B

def sim_one_game(prob_A, prob_B):
    # 模拟一场比赛的结果
    score_A, score_B = 0, 0
    while not gameover(score_A, score_B):
        if random.random() < prob_A:
            score_A += 1
        else:
            score_B += 1
    return score_A, score_B

def gameover(score_A, score_B):
    # 单场比赛模拟结束，一方先到达21分，比赛结束
    return score_A == 21 or score_B == 21

# 单元测试，用assert 断言进行
# 表达式结果为false时触发异常
assert gameover(21, 8) == True
assert gameover(9, 21) == True
assert gameover(11, 8) == False
# assert gameover(21, 8) == False # 会报错
print(sim_one_game(0.55, 0.45))
print(sim_one_game(0.7, 0.3))
print(sim_one_game(0.2, 0.8))

# 结果汇总输出
def print_summary(win_A, win_B, numbers_of_games):
    print("共模拟了{}场比赛".format(numbers_of_games))
    print("选手A获胜了{0}场，占比{1:.1%}".format(win_A, win_A / numbers_of_games))
    print("选手B获胜了{0}场，占比{1:.1%}".format(win_B, win_B / numbers_of_games))

if __name__ == "__main__":
    main()

# 匿名函数
# 基本形式: lambda 变量：函数体
# 常用用法
# 在参数列表中最适合使用匿名函数，尤其是与key = 搭配
# 排序 sort() sorted()
ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
ls.sort()
print(ls)

# 按照key设置的参数进行排序
ls.sort(key=lambda x: x[0])
print(ls)

ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
temp = sorted(ls, key=lambda x: x[0]+x[1])
print(temp)

# max() min()
n = max(ls, key=lambda x: x[1])
print(n)

n = min(ls, key=lambda x: x[1])
print(n)

# 面向过程和面向对象



