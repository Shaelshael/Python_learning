# список в словаре, вынести перебором ключ и его значения
favorite_places = {'ivan': ['square', 'forest', 'lake'],
                   'andrew': ['shopping mall', 'dam'],
                   'daniil': ['home', 'bar', 'forest'],
                   }
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f'\t{place.title()}')
