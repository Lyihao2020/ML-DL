# 使用用户输入来填充字典

responses = {}
prompt1 = "\nWhat\'s your name? "
prompt2 = "Which mountain would you like to climb someday? "
prompt3 = "Would you like to invite someone else to take this poll?(yes / no) "

active = True

while active:
    name = input(prompt1)
    mountain = input(prompt2)

    responses[name] = mountain

    repeat = input(prompt3)
    active = True if repeat == 'yes' else False

# 调查结束，显示结果
print('\n--- Poll Results ---')
for name, mountain in responses.items():
    print(f'{name} would like to climb {mountain} someday.')

