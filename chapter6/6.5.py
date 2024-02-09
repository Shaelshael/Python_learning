rivers = {'nile': 'egypt', 'volga': 'russia', 'amazon': 'brazil'}
for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}.")

print('\nList of rivers in dictionary:')
for river in rivers.keys():
    print(f'{river.title()}')

print('\nList of countries in dictionary:')
for country in rivers.values():
    print(f'{country.title()}')
