# pi_million_digits

if __name__ == '__main__':
    with open('pi_million_digits.txt') as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    print(pi_string[:52] + '...')
    print(len(pi_string))

    birthday = input('Enter your birthday, in the form mmddyy: ')
    if birthday in pi_string:
        print('Your birthday appears in the first hundred digits of pi!')
    else:
        print('Your birthday does not appear in the first hundred digits of pi!')