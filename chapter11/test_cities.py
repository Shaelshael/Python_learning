import unittest
from city_fuctions import get_city_info, get_city_info_extended


class CityInfoTestCase(unittest.TestCase):
    """Тесты для city_functions"""

    def test_city_info(self):
        """Проверка работы функции get_city_info"""
        city_info = get_city_info('ekaterinburg', 'russia')
        self.assertEqual(city_info, 'Ekaterinburg, Russia')

    def test_city_info_extended(self):
        """Проверка работы функции get_city_info_extended"""
        city_info = get_city_info_extended('ekaterinburg', 'russia', '3000')
        self.assertEqual(city_info, 'Ekaterinburg, Russia — population is 3000.')


if __name__ == '__main__':
    unittest.main()
