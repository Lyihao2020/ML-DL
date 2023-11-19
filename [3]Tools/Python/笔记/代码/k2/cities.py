# 练习

cities = {
    'HongKong': {
        'country': 'China',
        'population': '1100w',
        'fact': 'Beautiful',
    },

    'TaiBei': {
        'country': 'China',
        'population': '700w',
        'fact': 'Nice',
    },

    'Tokyo': {
        'country': 'Japan',
        'population': '1500w',
        'fact': 'Free',
    },

}

for city_name, city_info in cities.items():
    print(f'\nName: {city_name}')
    print(f'\tCountry: {city_info["country"]}')
    print(f'\tCountry: {city_info["population"]}')
    print(f'\tCountry: {city_info["fact"]}')

