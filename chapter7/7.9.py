# последовательное удаление одноименных элементов из списка через цикл while
sandwich_orders = ['tuna sandwich', 'pastrami sandwich', 'pepperoni sandwich', 'pastrami sandwich', 'salad sandwich'
                   'pastrami sandwich']
finished_sanwiches = []
print('We have no pastrami left.\n')

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    new_sandwich = sandwich_orders.pop()
    print(f'Your {new_sandwich} is ready!')
    finished_sanwiches.append(new_sandwich)

print('\nSandwiches that are prepared:')
for sandwich in finished_sanwiches:
    print(f'\t{sandwich.title()}')
