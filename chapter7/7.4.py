# цикличное введение значений пользователем до остановки определенным значением
prompt = '\nPlease, add another topping to your pizza.'
prompt += '\nOr type "quit" to stop. '
new_topping = ""
while new_topping != "quit":
    new_topping = input(prompt)
    if new_topping != 'quit':
        print(f'You added {new_topping} to your pizza.')
    else:
        print('\nThanks for your order!')
