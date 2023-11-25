# 读取文件

if __name__ == '__main__':
    with open('pi_digits.txt') as file_object:
        """不需要调用close(), Python会在合适的时机将其关闭"""
        contents = file_object.read()
        """
        如果仅仅这样，会存在一个多的空行，因为read()在文件末尾时，会返回一个空字符串
        因此需要添加contents.rstrip()
        """
        print(contents.rstrip())

    print('--------------------------')

    with open('pi_digits.txt') as file_object:
        """逐行读取"""
        for line in file_object:
            print(line.rstrip())

    print('--------------------------')

    """
    使用with关键字时，open()返回的文件对象只在with代码块中可以使用，
    如果要在代码块外进行引用，可在代码块内部将各行存储在一个列表中
    """

    with open('pi_digits.txt') as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())

    print('--------------------------')