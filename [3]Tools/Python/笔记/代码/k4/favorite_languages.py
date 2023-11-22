# Python标准库
from collections import OrderedDict
# 根据插入的顺序来维护项目的顺序
favorite_languages = OrderedDict()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


for name, language in favorite_languages.items():
    print(f'{name.title()}\'s favorite language is {language.title()}.')

print('--------------------------')

from collections import OrderedDict

# Creating an ordered dictionary
ordered_dict = OrderedDict()

# Adding items to the ordered dictionary
ordered_dict['one'] = 1
ordered_dict['three'] = 3
ordered_dict['five'] = 5
ordered_dict['two'] = 2

# Displaying the ordered dictionary
print("OrderedDict 1:", ordered_dict)

# Output:
# OrderedDict 1: OrderedDict([('one', 1), ('three', 3), ('five', 5), ('two', 2)])

print('--------------------------')

from collections import OrderedDict

# Creating an ordered dictionary with items in a specific order
ordered_dict = OrderedDict([('one', 1), ('three', 3), ('five', 5), ('two', 2)])

# Displaying the ordered dictionary
print("OrderedDict 2:", ordered_dict)

# Output:
# OrderedDict 2: OrderedDict([('one', 1), ('three', 3), ('five', 5), ('two', 2)])

print('--------------------------')

from collections import OrderedDict

# Creating an ordered dictionary
ordered_dict = OrderedDict([('one', 1), ('three', 3), ('five', 5), ('two', 2)])

# Iterating over key-value pairs in order
for key, value in ordered_dict.items():
    print(key, value)

# Output:
# one 1
# three 3
# five 5
# two 2

print('--------------------------')