# задача 7.4 с завершением цикла при несовпадении while, использованием переменной active и команды break

# завершение цикла при проверке while
prompt = '\nPlease, add another topping to your pizza.'
prompt += '\nOr type "quit" to stop. '
new_topping = ""
while new_topping != "quit":
   new_topping = input(prompt)
   if new_topping != 'quit':
       print(f'You added {new_topping} to your pizza.')
   else:
      print('\nThanks for your order!')

# управление продолжительностью переменной active
prompt = '\nPlease, add another topping to your pizza.'
prompt += '\nOr type "quit" to stop. '
active = True
while active:
   new_topping = input(prompt)
   if new_topping != 'quit':
       print(f'You added {new_topping} to your pizza.')
   else:
       active = False
       print('\nThanks for your order!')

# завершение программы командой break
prompt = '\nPlease, add another topping to your pizza.'
prompt += '\nOr type "quit" to stop. '
while True:
    new_topping = input(prompt)
    if new_topping == 'quit':
        print('\nThanks for your order!')
        break
    else:
        print(f'You added {new_topping} to your pizza.')
