user_list = []
if user_list:
    for user in user_list:
        if user == 'admin':
            print('Hallo, admin, would you like to see system report?')
        else:
            print(f'Hallo, {user.title()}, welcome again!')
else:
    print('We await new users here!')
