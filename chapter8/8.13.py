# функция с частью обязательных аргументов и произвольным количеством дополнительных
def user_profile(first_name, last_name, *user_info):
    """печатает отформатированную информацию о пользователе"""
    print(f'Нашего респондента зовут {first_name.title()}, его фамилия {last_name.title()}. Вот что он рассказал:')
    for info in user_info:
        print(f' - {info}')


user_profile('иван', 'иванов', 'живет в россии', 'работает слесарем')
