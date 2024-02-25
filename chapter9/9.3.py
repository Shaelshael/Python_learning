# создать класс User с разными атрибутами и методы для описания пользователя и приветствия
class User():
    """модель пользователя и методы для приветствия и вывода информации о нем"""

    def __init__(self, first_name, last_name, age, birth_place):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f'{first_name} {last_name}'
        self.age = age
        self.birth_place = birth_place

    def describe_user(self):
        print(f"User's full name: {self.full_name.title()}")
        print(f"User's age: {self.age}")
        print(f"User's place of birth: {self.birth_place.title()}")

    def greet_user(self):
        print(f'Hallo, {self.full_name.title()}! Welcome.')


user_0 = User('ivan', 'ivanov', '31', 'russia')
user_0.describe_user()
user_0.greet_user()
