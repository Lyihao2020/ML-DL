# 使用任意数量的关键字实参

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile

user_profile = build_profile('albert',
                             'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)