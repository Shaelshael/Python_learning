# перемещение элементов из списка в список через цикл while
sandwich_orders = ['tuna sandwich', 'pepperoni sandwich', 'salad sandwich']
finished_sanwiches = []

while sandwich_orders:
    new_sandwich = sandwich_orders.pop()
    print(f'Your {new_sandwich} is ready!')
    finished_sanwiches.append(new_sandwich)

print('\nSandwiches are prepared:')
for sandwich in finished_sanwiches:
    print(f'\t{sandwich.title()}')
