# цикл while для сохранения внесенных имен с приветствием ответившему
print("Type 'end' to stop the program.")
while True:
    user_name = input('Please, enter your name: ')
    print(f'Hallo, {user_name.title()}! Welcome.')
    with open('guest.txt', 'a') as user_list:
        user_list.write(f'{user_name.title()}\n')
    # запрашиваем продолжение цикла или завершение программы
    cycle_continuation = input('Anyone else wanna join? (y/n) ')
    if user_name == 'end':
        break
    elif cycle_continuation == 'n':
        break
