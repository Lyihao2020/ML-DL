# 元组
dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

# 修改元组变量
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值
dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

# 练习
print('\n')
menu = ('meat', 'milk', 'tea', 'water', 'bread')
print('Original menu:')
for food in menu:
    print(food)

menu = ('meat', 'milk', 'tea', 'vegetable', 'bread')
print('\nModified menu:')
for food in menu:
    print(food)