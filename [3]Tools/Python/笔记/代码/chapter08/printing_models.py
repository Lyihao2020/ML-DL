# 练习
import print_models as pm

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm.print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)
pm.show_printed_models(completed_models)