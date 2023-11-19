# 模仿 pizza 测试

users = []

if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')
else:
    print("We need to find some users!")

print('--------------------------')

current_users = ['Alex', 'Max', 'Steven', 'Xia', 'Eric']
new_users = ['Lai', 'Eric', 'John', 'Tom', 'Mike']

for new_user in new_users:
    flag = True
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            flag = False
            break
    if flag:
        print(f'{new_user} has not been registered.')
    else:
        print(f'{new_user} has been registered.')

print('--------------------------')

numbers = list(range(1, 11))

for number in numbers:
    match number:
        case 1: print('1st')
        case 2: print('2nd')
        case _: print(f'{number}th')

print('--------------------------')
