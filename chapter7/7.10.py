# опрос через добавление в словарь списком while + вывод результата опроса
responders = {}
program_active = True

while program_active:
    name = input('Hallo, enter your name, please: ')
    place = input('Where you would like to go? ')
    responders[name] = place
    repeat = input('Shall we continue? (y/n) ')
    if repeat == 'n':
        program_active = False

print('\n\tPoll results:')
for name, place in responders.items():
    if place.lower() != 'usa':
        print(f"{name.title()} would like to go to {place.title()}.")
    else:
        print(f"{name.title()} would like to go to {place.upper()}.")
