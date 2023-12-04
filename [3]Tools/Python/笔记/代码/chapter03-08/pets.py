# 练习

Steven = {
    'name': 'Steven',
    'owner': 'Max',
    'type': 'dog',
}

John = {
    'name': 'John',
    'owner': 'Mike',
    'type': 'dog',
}


Alex = {
    'name': 'Alex',
    'owner': 'Xia',
    'type': 'cat',
}


Eric = {
    'name': 'Eric',
    'owner': 'Lai',
    'type': 'bird',
}

pets = [Steven, John, Alex, Eric]

for pet in pets:
    for k, v in pet.items():
        if k == 'name':
            print(f'{k}: {v}')
        else:
            print(f'\t{k}: {v}')

print('--------------------------')

# 创建多个字典，每个字典表示一个宠物
pets = [
    {'name': 'Steven', 'type': 'dog', 'owner': 'Max'},
    {'name': 'John', 'type': 'dog', 'owner': 'Mike'},
    {'name': 'Alex', 'type': 'cat', 'owner': 'Xia'},
    {'name': 'Eric', 'type': 'bird', 'owner': 'Lai'},
]

# 遍历列表，并打印宠物的所有信息
for pet in pets:
    for key, value in pet.items():
        if key == 'name':
            print(f'{key}: {value}')
        else:
            print(f'\t{key}: {value}')

# 删除包含特定值的所有列表元素

pets = ['dog', 'cat', 'cat', 'rabbit', 'bird', 'dog', 'cat', 'pig']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)