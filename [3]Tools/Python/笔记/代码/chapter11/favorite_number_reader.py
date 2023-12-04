# 练习

import json

# file_name = 'favorite_number.json'
#
# with open(file_name) as f_obj:
#     favorite_number = json.load(f_obj)
#     print(f'I know your favorite number!It\'s {favorite_number}.')
#

def get_stored_number():
    """如果储存了最喜欢的数字，就返回他"""
    file_name = 'favorite_number.json'
    try:
        with open(file_name) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def update_number():
    """
    如果储存的数字不是最喜欢的数字，就更新他
    如果没有储存数字，就获取他"""
    file_name = 'favorite_number.json'
    favorite_number = input('What\'s your favorite number: ')
    with open(file_name, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        print('We\'ll remember your favorite number!')

def favorite_number():
    """储存并打印最喜欢的数字"""
    favorite_number = get_stored_number()
    test_number = input(f'Is {favorite_number} your favorite number?(yes/no) ')
    if test_number == 'yes':
        print(f'I know your favorite number!It\'s {favorite_number}.')
    else:
        update_number()

favorite_number()