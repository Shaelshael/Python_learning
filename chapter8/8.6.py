# функция, возвращающая отформатированное название и страну города
def city_country(name, country):
    city_definition = f'{name.title()}, {country.title()}'
    return city_definition


message_0 = city_country('ekaterinburg', 'russia')
print(message_0)
message_1 = city_country('chicago', 'usa')
print(message_1)
message_2 = city_country('beijing', 'china')
print(message_2)
