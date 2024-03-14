# сохранение внесенного пользователем имени в файл guest.txt
user_name = input('Enter your name: ')

with open('guest.txt', 'a') as guest_list:
    guest_list.write(f'{user_name.title()}\n')
