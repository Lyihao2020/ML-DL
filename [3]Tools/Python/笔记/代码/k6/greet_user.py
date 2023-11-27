import json

file_name = 'user_name.json'

with open(file_name) as file_object:
    contents = json.load(file_object)
    print(f'Welcome back, {contents}!')