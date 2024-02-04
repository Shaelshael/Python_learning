WoW = 'alive'
print("Is WoW == alive? I predict TRUE.")
print(WoW == 'alive')
print("\nIs WoW == dead? I predict FALSE.")
print(WoW == 'dead')

liked = ['WoW', 'GW2', 'SWtOR']
played = ['Lineage', 'TeSO', 'WoW', 'GW2', 'SWtOR']
# statements about WoW
print('\nI played WoW.')
print('WoW' in played)
print('I played and liked WoW.')
print(('WoW' in played) and ('WoW' in liked))
# statements about Lineage
print('\nI played Lineage.')
print('Lineage' in played)
print('I liked Lineage.')
print('Lineage' in liked)
# statement about TeSO
print('\nI played and liked TeSO.')
print('TeSO' in played and 'TeSO' in liked)
print('But at least i played it.')
print('TeSO' in played)
# statements about GW2
print("\nI didn't played GW2.")
print('GW2' not in played)
print("I played GW2, but didn't liked it.")
print('GW2' in played and 'GW2' not in liked)
print('Okay, I played it and i liked it.')
print('GW2' in played and 'GW2' in liked)
# statement about SWtOR
print("\nI played SWtOR, but i don't like it.")
print('SWtOR' in played and 'SWtOR' not in liked)
