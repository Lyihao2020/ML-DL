# 练习

cats_names = ['Mike', 'Tom', 'Jenny']
with open('cats.txt', 'w') as file_object:
    for cats_name in cats_names:
        file_object.write(cats_name + '\n')

try:
    with open('cats.txt') as file_object:
        contents = file_object.read()
        print(contents.rstrip())

    with open('dogs.txt') as file_object:
        contents = file_object.read()
        print(contents.rstrip())
except FileNotFoundError:
    pass

"""
line = "Row, row, row your boat"
line.count('row')   # 确定特定的单词或短语在字符串中出现了多少次
line.lower().count('row')
"""

