# строим подкласс от класса из 9.3
class User():
    """модель пользователя и методы для приветствия и вывода информации о нем"""

    def __init__(self, first_name, last_name, age, birth_place):
        """инициализирует атрибуты описания пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birth_place = birth_place
        self.full_name = f'{first_name} {last_name}'
        self.privileges = Privileges('type in chat')

    def describe_user(self):
        """выводит отформатированное описание пользователя"""
        print(f"\nUser's full name: {self.full_name.title()}")
        print(f"User's age: {self.age}")
        print(f"User's place of birth: {self.birth_place.title()}")

    def greet_user(self):
        """приветствует пользователя по полному имени"""
        print(f'Hallo, {self.full_name.title()}! Welcome.')


class Admin(User):
    """подкласс администратора"""
    def __init__(self, first_name, last_name, age, birth_place):
        super().__init__(first_name, last_name, age, birth_place)
        self.privileges = Privileges('modify user', 'ban user', 'type in chat')


class Privileges():
    """привилегии пользователей"""
    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("\nList of user's abilities:")
        for privilege in self.privileges:
            print(f'— {privilege}')
