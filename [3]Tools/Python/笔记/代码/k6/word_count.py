# 使用多个文件进行单词统计

def count_words(file_name):
    """统计一个文件大致包含多少个单词"""
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print(f'The file {file_name} doesn\'t exist.')
        # 使程序一声不吭
        pass
    else:
        # 计算文件中大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f'The file {file_name} has about {str(num_words)} words.')

file_names = ['alice.txt', 'little_women.txt', 'siddhartha.txt']
for file_name in file_names:
    count_words(file_name)