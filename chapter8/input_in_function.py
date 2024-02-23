# заполнение словаря в функции данными от пользователя
def user_profile(first, last, **user_info):
    """возвращает содержимое в виде словаря"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
user_age = input('Возраст: ')
acquired_info = user_profile(name, surname, age=f'{user_age}')
print(acquired_info)
