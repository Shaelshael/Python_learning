# программа из 9.1 + атрибут со значением по умолчанию и его изменения
class Restaurant:
    """модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """инициализирует атрибуты описания ресторана"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """выводит отформатированное описание ресторана"""
        print(f'Restaurant name is "{self.restaurant_name.title()}".')
        print(f'It specialises at {self.cuisine_type} cuisine.')

    def open_restaurant(self):
        """выводит сообщение об открытии ресторана"""
        print('\nOur restaurant is opened! All are welcome.')

    def number_customers_served(self):
        """выводит количество обслуженных посетителей"""
        print(f"Customers served: {self.number_served}")

    def increment_number_served(self):
        """увеличивает количество обслуженных посетителей на заданное значение"""
        self.number_served += 10


restaurant_0 = Restaurant('mamma mia', 'italian')
# вызов количества обслуженных посетителей без использования метода
print(f'Number of customers served: {restaurant_0.number_served}')

# вызов количества обслуженных посетителей через метод без изменения значения
restaurant_0.number_customers_served()

# вызов количества обслуженных посетителей через метод с изменением значения
restaurant_0.number_served = 3
restaurant_0.number_customers_served()

# вызов количества обслуженных посетителей через метод с увеличением значения по умолчанию
restaurant_0.increment_number_served()
restaurant_0.number_customers_served()
