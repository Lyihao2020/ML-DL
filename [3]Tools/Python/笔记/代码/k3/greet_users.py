# 传递列表

def greet_users(names):
    for name in names:
        print(f'Hello, {name.title()}!')

usernames = ['Alex', 'john', 'max', 'Jenny']
greet_users(usernames)