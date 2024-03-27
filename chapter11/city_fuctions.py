# задача 11.1, написание функции и написание теста для ее проверки


def get_city_info_check(city_name, city_location):
    """Возвращает отформатированные название и местоположение города (для ручных проверок)."""
    print("Type 'q' to end program.")
    while True:
        city_name = input('Enter name of the city: ')
        if city_name == 'q':
            print('Program stopped.')
            break
        city_location = input('Enter location of the city: ')
        if city_location == 'q':
            print('Program stopped.')
            break
        city_info = f'{city_name.title()}, {city_location.title()}'
        print(f'{city_info}')
        return city_info


def get_city_info(city_name, city_location):
    """Возвращает отформатированные название и местоположение города."""
    city_info = f'{city_name.title()}, {city_location.title()}'
    return city_info

# переработанная функция для задачи 11.2, с дополнительным параметром


def get_city_info_extended(city_name, city_location, population=''):
    """Возвращает отформатированные название и местоположение города."""
    if population:
        city_info = f'{city_name.title()}, {city_location.title()} — population is {int(population)}.'
    else:
        city_info = f'{city_name.title()}, {city_location.title()}'
    return city_info
