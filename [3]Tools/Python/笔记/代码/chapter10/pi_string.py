# 使用文件中的内容

if __name__ == '__main__':
    with open('pi_digits.txt') as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    print(pi_string)
    print(len(pi_string))