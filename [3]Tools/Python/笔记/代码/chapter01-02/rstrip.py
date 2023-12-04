# rstrip.py 删除空格

# 确保字符串末尾没有空格
favorite_language = "python "
print(f'\'{favorite_language}\'')
favorite_language.rstrip()  # 只是在"python "上进行了操作，变量指向的对象仍然是"python "
print(f'\'{favorite_language}\'')   # 仍然存在空格

# 要永久的删除这个空格，必须将删除操作的结果存回到变量中
favorite_language = favorite_language.rstrip()
print(f'\'{favorite_language}\'')

first_name = "  ada "
last_name = "  lovelace  "
message = "  Good morning!  "
# 开头删除 lstrip()
# 删除空格 strip()
full_name = first_name.strip() + " " + last_name.strip()
message = message.lstrip()
message = message.rstrip()
print(f'{full_name.title()} said to me, \'{message}\'')




