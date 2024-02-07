current_users = ['admin', 'vasya', 'andrei', 'danil', 'evgenyi']
new_users = ['vadim', 'alexander', 'ilya', 'Vasya', 'DANIL']
for user in new_users:
    if user.lower() in current_users:
        print(f'{user.title()}, you need to choose different nickname.')
    else:
        print(f'Hallo, {user.title()}, welcome to the club!')
