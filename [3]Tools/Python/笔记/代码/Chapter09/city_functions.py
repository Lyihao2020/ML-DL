# 测试练习

def city_country(city, country, population=''):
    """接受城市国家名，并返回相匹配字符串"""
    if population:
        city_country = city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        city_country = city.title() + ', ' + country.title()
    return city_country

