# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# friend_foods = my_foods # 行不通，因为这样同时指向了同一个对象

my_foods.append('ice cream')
friend_foods.append('cannoli')

print('My favorite foods are:')
print(my_foods)

for my_food in my_foods:
    print(my_food, end=' ')

print('\n')
print('My friend\'s favorite foods are:')
print(friend_foods)

for friend_food in friend_foods:
    print(friend_food, end=' ')
