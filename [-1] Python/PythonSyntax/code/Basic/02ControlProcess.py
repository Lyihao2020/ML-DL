# 控制流程
# 顺序流程

# res = 1 + 2 + 3 + 4 + 5
res = 0
res += 1
res += 2
res += 3
res += 4
res += 5
print(res)

# 循环流程（遍历循环for）
res = 0
for i in [1, 2, 3, 4, 5]:
    res += i
print(res)

# 循环流程（无限循环while）
i = 1
res = 0
while i <= 5:
    res += i
    i += 1
print(res)

# 分支流程if
age = 18
if age > 22:
    print("可以结婚啦")
else:
    print("不可以哦~~~")

