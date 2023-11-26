# 写入文件

file_name = 'programming.txt'

# w 写入，r 读取，a 附加，r+ 读取和写入， 如果省略则为只读模式
# 以写入'w'模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件
# Python只能将字符串写入文本文件，要将数值数据存储到文本文件中，必须先使用函数str()将其转化为字符串格式
with open(file_name, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love programming.\n')
    file_object.write('I love programming.\n')


