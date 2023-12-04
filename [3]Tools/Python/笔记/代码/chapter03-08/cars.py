# 组织列表，对列表进行排序

cars = ['bwm', 'audi', 'toyota', 'subaru']
cars.sort() # 永久性排序列表
print(cars)
# 反方向排序，使用reverse
cars.sort(reverse=True)
print(cars)

# 对列表进行临时排序
# 使列表保持原来的排列顺序，又以特定的顺序显示他们，可使用sorted()
print('--------------------------')
cars = ['bwm', 'audi', 'toyota', 'subaru']
print(cars)
print('Here is the sorted list: ')
print(sorted(cars))

print('Here is the reversed list: ')
print(sorted(cars, reverse=True))

print('Here is the original list: ')
print(cars)

print('--------------------------')

# 倒着打印列表
# reverse()永久地修改列表元素的排列顺序
cars.reverse()
print(cars)

print('--------------------------')

# 练习

place = ['Taiwan', 'Sweden', 'Tokyo', 'HongKong', 'London']
print(place)
print(sorted(place))
print(place)
print(sorted(place, reverse=True))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)

print('--------------------------')

# if语句测试
cars = ['bwm', 'audi', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':    # python检查是否相等时区分大小写
        print(car.upper())
    else:
        print(car.title())


