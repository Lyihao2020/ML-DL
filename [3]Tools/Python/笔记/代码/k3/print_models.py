# 传递列表

# 原代码

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()

    print(f'Printing models: {current_design}')
    completed_models.append(current_design)

print('\nThe following models have been printed.')
for completed_model in completed_models:
    print(f'\t{completed_model}')

print('--------------------------')

# 重新组织代码

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(f'Printing models: {current_design}')
        completed_models.append(current_design)

def show_printed_models(completed_models):
    print('\nThe following models have been printed.')
    for completed_model in completed_models:
        print(f'\t{completed_model}')

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_printed_models(completed_models)

print('--------------------------')

# 禁止函数修改列表
# function_name(list_name[:])
# 向函数传递列表的副本而不是原件，这样函数做的任何修改都只影响副本，而丝毫不影响原件

# 如果不想清空未打印的设计列表

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)
show_printed_models(completed_models)

# 虽然向函数传递列表的副本可以保留原始列表的内容，但除非有充分的理由需要传递副本
# 否则还是应该将原始的列表传递给函数，因为使用现成的列表可以避免花时间和内存创建副本，从而提高效率

