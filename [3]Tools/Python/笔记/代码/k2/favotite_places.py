# 练习

favorite_places = {
    'Alex': ['Tokyo', 'Paris', 'HongKong'],
    'Max': ['Shanghai', 'Hangzhou'],
    'Anna': 'London',
}

for name, places in favorite_places.items():
    if isinstance(places, str):
        places = [places]   # 将一个单词变为列表中的一个元素
        # 不可以用list(places), 因为会把单词拆分为 L,O,N,D,O,N

    places_count = len(places)
    places_str = ', '.join(map(str.title, places))

    if places_count == 1:
        print(f'\n{name}\'s favorite place is {places_str}.')
    else:
        print(f'\n{name}\'s favorite places are {places_str}.')

