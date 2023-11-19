# 用 while 循环来处理列表和字典

# for循环是一个遍历列表的有效方式，但在for循环中不应该修改列表
# 否则将导致Python难以追踪其中的元素

# 在列表之间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'Verifying {current_user.title()} now.')
    confirmed_users.append(current_user)

print('\nConfirmed users are as followed.')
for confirmed_user in confirmed_users:
    print(f'\t{confirmed_user.title()}')