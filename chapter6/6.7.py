# программа из 6.1
# first_user = {'age': 35, 'first_name': 'Ivan', 'last_name': 'Ivanov', 'city': 'Moscow'}
# print(first_user['age'])
# print(first_user['city'])
# print(first_user['first_name'])
# print(first_user['last_name'])

# сохранение словарей в списке и их перебор
first_user = {'age': 35, 'first_name': 'ivan', 'last_name': 'ivanov', 'city': 'moscow'}
second_user = {'age': 25, 'first_name': 'andrei', 'last_name': 'andreev', 'city': 'ekaterinburg'}
third_user = {'age': 20, 'first_name': 'sasha', 'second_name': 'alexandrov', 'city': 'piter'}
people = [first_user, second_user, third_user]
for user in people:
    for key, value in user.items():
        print(f'{key.title()} — {value}')
