# 列表的增删改查操作

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'   # 修改
print(motorcycles)

# 在列表末尾进行添加元素
motorcycles.append('bicycles')
print(motorcycles)

# 在任意位置插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 如果事先知道待删除元素的位置，可以使用del进行元素的删除,且不再以任何方式使用它
del motorcycles[0]
print(motorcycles)

# 将元素从列表中删去，并使用他的值
poped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(poped_motorcycle)

# 根据值删除元素,不知道元素在哪个位置
motorcycles.remove('yamaha')
print(motorcycles)  # 只删除第一个指定了的值，很多次需要用到循环

# 练习
name = ['Max', 'Alex', 'John']
print(f'{name[2]} can\'t come!')
name.remove('John')
print('Mike would come!')
name.append('Mike')
print('--------------------------')
print(f'{name[0]} are invited!')
print(f'{name[1]} are invited!')
print(f'{name[2]} are invited!')
print('--------------------------')
print('Now we find a bigger table, let\'s change!')
print('Steven, Xia would come!')
name.insert(0, 'Steven')
name.append('Xia')
print(f'{name[0]} are invited!')
print(f'{name[1]} are invited!')
print(f'{name[2]} are invited!')
print(f'{name[3]} are invited!')
print(f'{name[4]} are invited!')
print('--------------------------')
print('What a pity! We only have two seats! Let\'s change again!')
name.pop()
name.pop()
name.pop()
print(f'{name[0]} are invited!')
print(f'{name[1]} are invited!')
del name[1] # 从后面往前面删除，因为删除以后名单会改变
del name[0]
print(name)
print('--------------------------')


