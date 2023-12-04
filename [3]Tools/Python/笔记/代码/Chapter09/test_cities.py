# 测试练习

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """测试城市国家匹配程度的类"""

    def test_city_country(self):
        """测试城市国家匹配用例"""
        city_country_case = city_country('santiago', 'chile')
        self.assertEquals(city_country_case, 'Santiago, Chile')

    def test_city_country_population(self):
        """测试城市国家人口匹配用例"""
        city_country_case = city_country('santiago', 'chile', 5000000)
        self.assertEquals(city_country_case, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
