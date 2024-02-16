# взять программу из 6.2 и изменить её, чтобы в значениях можно было хранить несколько цифр + вывести все данные
# перебором

# favorite_numbers = {'Seva': 69, 'Sasha': 11, 'Kirill': 8, 'Andrew': 33, 'Ivan': 10}
# print(f"Seva's favorite number is {favorite_numbers['Seva']}.")
# print(f"Sasha's favorite number os {favorite_numbers['Sasha']}.")
# print(f"My favorite number is {favorite_numbers['Kirill']}.")
# print(f"Andrew's favorite number is {favorite_numbers['Andrew']}.")
# print(f"Ivan's favorite number is {favorite_numbers['Ivan']}.")

favorite_numbers = {'ivan': [14, 33, 25],
                    'andrew': [77, 666],
                    'daniil': [1, 3, 5, 7],
                    }
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f'\t{number}')
