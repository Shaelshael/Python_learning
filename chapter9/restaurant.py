# строим подкласс от класса из 9.1
class Restaurant:
    """модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """инициализирует атрибуты описания ресторана"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """выводит отформатированное описание ресторана"""
        print(f'Restaurant name is "{self.restaurant_name.title()}".')
        print(f'It specialises at {self.cuisine_type} cuisine.')

    def open_restaurant(self):
        """выводит сообщение об открытии ресторана"""
        print('\nOur restaurant is opened! All are welcome.')


class IceCreamStand(Restaurant):
    """подкласс с моделью киоска с мороженным"""

    def __init__(self, restaurant_name, cuisine_type, flavors=''):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_flavors(self):
        print('In our stand we have this kind of flavors:')
        for flavor in self.flavors:
            print(f'— {flavor.title()}')

