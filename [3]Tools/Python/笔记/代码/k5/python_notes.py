# PythonNotes
if __name__ == '__main__':
    with open('PythonNotes.txt') as file_object:
        lines = file_object.readlines()
        content = ''.join(lines)
        print(content, end='')  # 将列表拆解为单个字符串并输出
        print('\n-----------------------------------')
        for line in lines:
            print(line, end='')

    print('\n-----------------------------------')
    python_strings = []
    for line in lines:
        python_strings.append(line.strip())
    for python_string in python_strings:
        print(python_string)  # 不添加换行符

    print('-----------------------------------')
    for python_string in python_strings:
        print(python_string.replace('Python', 'C++'))  # 手动添加换行符

    print('-----------------------------------')
    for python_string in python_strings:
        python_string.replace('Python', 'C++')  # Python replace 临时变换不是永久变换
        print(python_string)  # 不手动添加换行符
