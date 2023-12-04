# 返回值
# 让实参变成可选的

def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

current_name = get_formatted_name('Max', 'steven')
print(current_name)

current_name = get_formatted_name('Max', 'Jenny', 'alex')
print(current_name)