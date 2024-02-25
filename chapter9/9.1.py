# создаем класс и методы в нем
class Restaurant:
    """модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name is "{self.restaurant_name.title()}".')
        print(f'It specialises at {self.cuisine_type} cuisine.')

    def open_restaurant(self):
        print('\nOur restaurant is opened! All are welcome.')


restaurant = Restaurant('mamma mia', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
