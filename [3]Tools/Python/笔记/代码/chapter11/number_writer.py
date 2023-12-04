# 使用json来存储数据

# 我们来编写一个存储一组数字的简短程序
# 使用json.dump()来存储这组数据
# json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象

import json

numbers = [1, 2, 3, 4, 5, 6]

file_name = 'numbers.json'
with open(file_name, 'w') as file_object:
    json.dump(numbers, file_object)