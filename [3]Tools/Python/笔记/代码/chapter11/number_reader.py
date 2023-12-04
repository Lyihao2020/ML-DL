# json.load()读取到内存中

import json

file_name = 'numbers.json'
with open(file_name) as file_object:
    contents = json.load(file_object)

print(contents)