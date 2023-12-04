# 文件读取异常

file_name = 'alice.txt'

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + file_name + 'doesn\'t exist.'
    print(msg)
else:
    # 计算文件中大致包含多少个单词
    words = contents.split()    # 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中
    print(words)
    num_words = len(words)
    print(f'The file {file_name} has about {str(num_words)} words.')
