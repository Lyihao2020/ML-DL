# 切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # 最后一位不包含在内
print(players[1:4])

# 最后三名
print(players[-3:])
print(players[-3:-1])   # 不包含最后一名

# 遍历切片
for player in players[:3]:
    print(player)

# 前三个元素为
print(players[:3])
# 中间三个元素为
print(players[len(players)//2 - 1:len(players)//2 + 2])
# 最后三个元素为
print(players[-3:])