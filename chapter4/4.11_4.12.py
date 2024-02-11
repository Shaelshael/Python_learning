pizza = ["Пепперони", "деревенская", "колбаски-барбекю"]
friends_pizzas = pizza[:]
pizza.append('баварская')
friends_pizzas.append('с ананасами')

print('Мои любимые пиццы:')
print(pizza)
print('\nЛюбимые пиццы моего друга:')
print(friends_pizzas)
# 4.2
for pizzas in pizza:
    print(f'\n"{pizzas.title()}" стоит своих денег')
    print('Хотя, конечно, могла бы стоить и поменьше.')

for stukes in friends_pizzas:
    print(f'\n"{stukes.title()}" особенно хороша под пиво.')
