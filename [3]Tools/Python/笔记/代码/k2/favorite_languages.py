# 使用键值的规范

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print('Sarah\'s favorite language is ' + favorite_languages['sarah'].title() + '.')

for name, language in favorite_languages.items():
    print(f'{name.title()}\'s favorite language is {language.title()}.')

for name in favorite_languages: # 遍历字典时，会默认遍历的是键
    print(f'{name.title()}\'s favorite language is {favorite_languages[name].title()}.')

print('--------------------------')

# 遍历字典中所有的键

for name in favorite_languages.keys():  # 等同于 for name in favorite_languages:
    # .keys() 实际上返回一个列表，其中包含字典中所有的键
    print(f'Key: {name}')

friends = ['phil', 'sarah']

for name in favorite_languages:
    print('\n' + name.title())

    if name in friends:
        print(f'Hi {name},'
              f'I see your favorite language is '
              f'{favorite_languages[name].title()}.')

print('--------------------------')

# 按顺序遍历字典中所有的键

# 一种方法是在for循环中对返回的键进行排序
for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll.')

print('--------------------------')

# 遍历字典中所有的值

print('These following languages have been mentioned.')
for language in sorted(set(favorite_languages.values())):   # 利用集合对values进行去重
    print(language.title())

print('--------------------------')

# 练习

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

members = ['Mike', 'Xia', 'Max', 'Edward', 'Eric', 'Phil']

for member in members:
    flag = True

    for name in favorite_languages:
        if member.lower() == name.lower():
             flag = False
             break

    if flag:
        print(f'{member.title()}, you have not taken the poll.')
        language = input('Please enter your favorite language: ')
        favorite_languages[member.lower()] = language.lower()
    else:
        print(f'{member.title()}, thank you for taking the poll.')

print(favorite_languages)

print('--------------------------')

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c#',
    'edward': ['ruby', 'java'],
    'phil': ['python', 'c++'],
}

for name in favorite_languages:
    languages = favorite_languages[name]

    if isinstance(languages, str):
        # 使用了 isinstance() 函数来检查 languages 的类型。
        # 如果它是字符串，就表示只有一个语言；如果是列表，就表示有多个语言，需要遍历列表。
        print(f"\n{name}'s favorite language is {languages.title()}.")
    else:
        print(f"\n{name}'s favorite languages are as follows:")
        for language in languages:
            print(f"\t{language.title()}")

print('--------------------------')

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c#',
    'edward': ['ruby', 'java'],
    'phil': ['python', 'c++'],
}

for name, languages in favorite_languages.items():
    if isinstance(languages, str):
        languages = [languages]

    print(f"\n{name}'s favorite language{'s' if len(languages) > 1 else ''} are {', '.join(map(str.title, languages))}.")

print('--------------------------')

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c#',
    'edward': ['ruby', 'java'],
    'phil': ['python', 'c++'],
}

for name, languages in favorite_languages.items():
    if isinstance(languages, str):
        languages = [languages]

    language_count = len(languages)
    language_str = ', '.join(map(str.title, languages))

    """
    map() 是 Python 内置函数之一，它用于对可迭代对象中的每个元素应用一个指定的函数。
    具体而言，map(function, iterable) 接受一个函数和一个可迭代对象作为参数，返回一个迭代器，
    该迭代器产生由函数应用于可迭代对象中每个元素的结果。

    在这个特定的例子中，map(str.title, languages) 的作用是对 languages 列表中的每个元素应用 str.title() 函数，
    即将每个语言的首字母大写。这确保了输出的语言名称以大写字母开头，使输出更加规范和易读。
    """

    if language_count == 1:
        print(f"\n{name}'s favorite language is {language_str}.")
    else:
        print(f"\n{name}'s favorite languages are {language_str}.")

print('--------------------------')