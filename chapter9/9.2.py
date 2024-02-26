# на основе класса из 9.1, создать 3 экземлпяра и вызвать один из методов для каждого
class Restaurant:
    """модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """инициализирует атрибуты описания ресторана"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """выводит отформатированное описание ресторана"""
        print(f'\nRestaurant name is "{self.restaurant_name.title()}".')
        print(f'It specialises at {self.cuisine_type} cuisine.')

    def open_restaurant(self):
        """выводит сообщение об открытии ресторана"""
        print('\nOur restaurant is opened! All are welcome.')


restaurant_0 = Restaurant('mamma mia', 'italian')
restaurant_1 = Restaurant('beer bar', 'german')
restaurant_2 = Restaurant('ching cjong', 'japanese')

restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
