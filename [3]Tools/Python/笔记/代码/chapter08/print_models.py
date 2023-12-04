# # 传递列表
#
# # 原代码
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#
#     print(f'Printing models: {current_design}')
#     completed_models.append(current_design)
#
# print('\nThe following models have been printed.')
# for completed_model in completed_models:
#     print(f'\t{completed_model}')
#
# print('--------------------------')
#
# # 重新组织代码
#
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         print(f'Printing models: {current_design}')
#         completed_models.append(current_design)
#
#
# def show_printed_models(completed_models):
#     print('\nThe following models have been printed.')
#     for completed_model in completed_models:
#         print(f'\t{completed_model}')
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_printed_models(completed_models)
#
# print('--------------------------')
#
# # 禁止函数修改列表
# # function_name(list_name[:])
# # 向函数传递列表的副本而不是原件，这样函数做的任何修改都只影响副本，而丝毫不影响原件
#
# # 如果不想清空未打印的设计列表
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs[:], completed_models)
# print(unprinted_designs)
# show_printed_models(completed_models)
#
# # 虽然向函数传递列表的副本可以保留原始列表的内容，但除非有充分的理由需要传递副本
# # 否则还是应该将原始的列表传递给函数，因为使用现成的列表可以避免花时间和内存创建副本，从而提高效率
#

# 如果你在 `printing_models.py` 中导入了 `print_models` 模块，并在该文件中执行了 `pm.print_models(unprinted_designs[:], completed_models)`，那么确实会执行 `print_models.py` 中的代码。这是因为 `import print_models as pm` 语句导入了整个 `print_models` 模块，并且通过 `pm.print_models` 调用了其中的函数。
#
# 为了避免重复执行代码，你可以将 `print_models.py` 中的代码包装在一个名为 `if __name__ == "__main__":` 的条件中，以确保它只在直接运行 `print_models.py` 文件时才执行，而在被其他文件导入时不执行。修改 `print_models.py` 如下：
#
# ```python
# print_models.py

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing models: {current_design}')
        completed_models.append(current_design)

def show_printed_models(completed_models):
    print('\nThe following models have been printed.')
    for completed_model in completed_models:
        print(f'\t{completed_model}')

if __name__ == "__main__":
    unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    print_models(unprinted_designs, completed_models)
    show_printed_models(completed_models)
# ```
#
# 这样修改后，当你在其他文件中导入 `print_models` 模块时，其中的代码就不会被执行了。
# 只有在直接运行 `print_models.py` 文件时，才会执行模块内的代码。