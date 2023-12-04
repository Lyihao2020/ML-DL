# 加法运算

# def is_number(value):
#     return isinstance(value, (int, float))
while True:
    try:
        # 提示用户输入第一个数字
        num1 = float(input("请输入第一个数字: "))

        # 提示用户输入第二个数字
        num2 = float(input("请输入第二个数字: "))

        # 计算并打印两个数字的和
        result = num1 + num2
        print("两个数字的和是:", result)

    except ValueError as e:
        # 捕获 ValueError 异常，提示用户输入的不是数字
        print("输入错误:", e)
    except Exception as e:
        # 捕获其他异常，并打印错误消息
        print("发生错误:", e)

# 判断是否为数字
# def is_number(s):
#         return s.isdigit()
#
# # 示例
# input_str = input("请输入一个字符串: ")
# if is_number(input_str):
#     print("是数字")
# else:
#     print("不是数字")

# def is_number(value):
#     return isinstance(value, (int, float))
#
# # 示例
# input_value = input("请输入一个值: ")
# try:
#     input_value = float(input_value)
#     if is_number(input_value):
#         print("是数字")
#     else:
#         print("不是数字")
# except ValueError:
#     print("不是数字")
