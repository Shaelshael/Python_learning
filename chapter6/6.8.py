# вывести перебором всю информацию о животном из словаря в списке
shusha = {'owner': 'kirill', 'species': 'cat'}
gektor = {'owner': 'sahsa', 'species': 'dogo'}
loki = {'owner': 'kirill', 'species': 'dogo'}
mika = {'owner': 'sahsa', 'species': 'cat'}
pets = [shusha, mika, gektor, loki]
for pet in pets:
    for key, value in pet.items():
        print(f'Animal {key} — {value.title()}')
