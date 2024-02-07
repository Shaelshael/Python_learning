user_list = ['admin', 'vasya', 'andrei', 'danil']
for user in user_list:
    if user == 'admin':
        print('Hallo, admin, would you like to see system report?')
    else:
        print(f'Hallo, {user.title()}, welcome again!')