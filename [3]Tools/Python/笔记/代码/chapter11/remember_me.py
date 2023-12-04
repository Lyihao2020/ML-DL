# 使用json文件存储用户数据不易丢失
# 重构：将代码划分为一系列完成具体工作的函数

import json

# 一轮重构
# def greet_user():
    # 如果以前存储了用户名，就加载他
    # 否则，就提示用户输入用户名并存储他
#     try:
#         file_name = 'user_name.json'
#         with open(file_name) as file_object:
#             contents = json.load(file_object)
#     except FileNotFoundError:
#         user_name = input('What\'s your name? ')
#         with open(file_name, 'w') as file_object:
#             json.dump(user_name, file_object)
#             print(f'We\'ll remember you when you come back, {user_name}!')
#     else:
#         print(f'Welcome back, {contents}!')
#
# greet_user()

# try:
      # 一些可能引发异常的代码
      # 如果没有异常发生，则执行这里的代码
# except ExceptionType as e:
      # 处理异常的代码
# else:
      # 如果没有异常发生，则执行这里的代码
# finally:
      # 无论是否发生异常，都会执行这里的代码

# 二轮重构
def get_stored_username():
    """如果存储了用户名，就获取他"""
    file_name = 'user_name.json'
    try:
        with open(file_name) as file_object:
            user_name = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return user_name

def get_new_username():
    """提示用户输入用户名，获取新的用户名"""
    user_name = input('What\'s your name? ')
    file_name = 'user_name.json'
    with open(file_name, 'w') as file_object:
        json.dump(user_name, file_object)
    return user_name

def greet_user():
    # 如果以前存储了用户名，就加载他
    # 否则，就提示用户输入用户名并存储他
    user_name = get_stored_username()
    test_name = input(f'Are you {user_name}(yes/no)? ')
    if test_name == 'yes':
        print(f'Welcome back, {user_name}!')
    else:
        user_name = get_new_username()
        print(f'We\'ll remember you when you come back, {user_name}!')

greet_user()