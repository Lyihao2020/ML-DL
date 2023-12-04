# 选择何时退出
# while 与 字符串的运用

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter \'quit\' to end the program. "

# message = ""
# while message != "quit":
#     message = input(prompt)
#
#     if message != "quit":
#         print(message)

active = True
while active:
    message = input(prompt)

    if message != 'quit':
        print(message)
    else:
        active = False
