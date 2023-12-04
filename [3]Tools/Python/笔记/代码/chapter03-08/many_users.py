# 将字典存放到字典中（网站信息的存储）
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}

for username, userinfo in users.items():
    print('\nUsername: ' + username.title())
    full_name = userinfo['first'] + ' ' + userinfo['last']
    user_location = userinfo['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + user_location.title())

# 请注意，如果在每位用户的字典都包含不同的键时，for循环内部将更加复杂