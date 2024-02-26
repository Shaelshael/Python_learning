# программа из 9.3 + новый атрибут и методы, увеличивающие его значение и уменьшающие
class User():
    """модель пользователя и методы для приветствия и вывода информации о нем"""

    def __init__(self, first_name, last_name, age, birth_place):
        """инициализирует атрибуты описания пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f'{first_name} {last_name}'
        self.age = age
        self.birth_place = birth_place
        self.login_attempts = 0

    def describe_user(self):
        """выводит отформатированное описание пользователя"""
        print(f"User's full name: {self.full_name.title()}")
        print(f"User's age: {self.age}")
        print(f"User's place of birth: {self.birth_place.title()}")

    def greet_user(self):
        """приветствует пользователя по полному имени"""
        print(f'Hallo, {self.full_name.title()}! Welcome.')

    def show_login_attempts(self):
        """показывает текущее количество попыток авторизации"""
        print(f'\nCurrent amount of login attempts: {self.login_attempts}')
    def increment_login_attempts(self):
        """добавляет к количеству попыток авторизации один"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """сбрасывает количество попыток авторизации до нуля"""
        self.login_attempts = 0


# создаем экземпляр класса User, несколько раз увеличиваем количество попыток авторизации и потом сбрасываем их, с
# выводом чисел для проверки
user_0 = User('ivan', 'ivanov', '33', 'russia')
# выводим изначальное число попыток
user_0.show_login_attempts()
# добавляем 3 попытки по одной
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
# проверяем, что изначальное число стало 3
user_0.show_login_attempts()
# сбрасываем количество попыток до нуля
user_0.reset_login_attempts()
# проверяем, что сброс прошел успешно
user_0.show_login_attempts()
