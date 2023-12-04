# 向函数传递信息

def greet_user(username):
    print(f'Hello, {username.title()}!')

greet_user('jesse')

# 结合函数和while

def get_formatted_name(first_name, last_name, middle_name):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

prompt1 = '\nPlease tell me your name: '
prompt2 = 'First name: '
prompt3 = 'Middle name: '
prompt4 = 'Last name: '
prompt5 = 'Continue?(yes / no) '

while True:
    print(prompt1)
    first_name = input(prompt2)
    test = input('Do you have middle name?(yes / no) ')
    middle_name = ''
    if test == 'yes':
        middle_name = input(prompt3)
    last_name = input(prompt4)

    full_name = get_formatted_name(first_name, last_name, middle_name)
    print(f'\nHello, {full_name}!')

    test = input(prompt5)
    if test != 'yes':
        break

