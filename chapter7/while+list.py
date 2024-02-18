# просто решил проверить, как работает добавление в список элементов через цикл while
test_list = []
prompt = 'Type "quit" to stop the program.'
prompt += '\nOr add smth to the list: '
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        test_list.append(message)
        print(f'\nYou added "{message}" to your list.')
    else:
        print(f'\nYou have in list: {test_list}')
        print('End of program.')
