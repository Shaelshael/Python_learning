# функция с одним аргументом по умолчанию
def describe_city(name, country='usa'):
    """вывод сообщения со страной, в которой находится город"""
    if country == 'usa':
        print(f'{name.title()} is in {country.upper()}.')
    else:
        print(f'{name.title()} is in {country.title()}.')


# в техасе есть москва
describe_city('moscow')
describe_city('ekaterinburg', 'russia')
describe_city(country='china', name='beijing')

# спросить, как внедрить проверку if на 'usa' в функции для вывода в функции переменной .upper()
