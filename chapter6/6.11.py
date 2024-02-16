# словари о городах в словаре из городов, вывести название города и всю инфу о нём
cities = {'moscow': {
                'country': 'russia',
                'population': 13_104_177,
                'fact': 'Cities name is given in honor of the Moscow River.'
                },
          'ekaterinburg': {
              'country': 'russia',
              'population': 1_539_371,
              'fact': 'Ekaterinburg previously was known as Sverdlovsk.'
              },
          'minsk': {
              'country': 'belarus',
              'population': 1_075_324,
              'fact': 'Minsk burned 18 times.'
              },
          }
for city, city_info in cities.items():
    print(f'\nCity — {city.title()}')
    location = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f'Located in {location.title()}.')
    print(f'Population of this city is {population}.')
    print(fact)
