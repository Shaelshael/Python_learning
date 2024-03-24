# версия программы 10.12, с добавлением проверки на соответствие сохраненного числа требованиям пользователя
import json


def get_favorite_number():
    # запрашивает соответствие сохраненного числа, выгружает число из файла и сообщает его пользователю.
    # Если файла с числом нет - запрашивает число, сохраняет и выгружает
    try:
        filename = 'favorite_number.json'
        with open(filename, 'r') as f:
            number_acquired = json.load(f)
    except FileNotFoundError:
        favorite_number = input('Hallo! Enter your favorite number: ')
        filename = 'favorite_number.json'
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)
    else:
        number_match = input(f'Your favorite number is {number_acquired}? (y/n) ')
        if number_match == 'y':
            print(f"Hey, i know your favorite number! It's {number_acquired}.")
        else:
            favorite_number = input('Then, please, enter your favorite number: ')
            filename = 'favorite_number.json'
            with open(filename, 'w') as f:
                json.dump(favorite_number, f)


get_favorite_number()
