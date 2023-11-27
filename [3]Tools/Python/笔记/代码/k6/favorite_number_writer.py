# 练习

import json

file_name = 'favorite_number.json'
favorite_number = input('What\'s your favorite number: ')

with open(file_name, 'w') as f_obj:
    json.dump(favorite_number, f_obj)

