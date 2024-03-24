# рефакторим программу из 10.13
import json


def get_favorite_number():
    # запрашивает и сохраняет любимое число пользователя
    favorite_number = input('Hallo! Enter your favorite number: ')
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print(f'Thanks for respond! Now i will remember your favorite number.')


def get_stored_favorite_number():
    # выгружает любимое число из файла
    filename = 'favorite_number.json'
    with open(filename, 'r') as f:
        number_acquired = json.load(f)
    return int(number_acquired)


def return_favorite_number():
    # уточняет соответствие сохраненного числа и выводит его пользователю, если число соответствует
    try:
        get_stored_favorite_number()
    except FileNotFoundError:
        get_favorite_number()
    else:
        number_match = input(f'Your favorite number is {get_stored_favorite_number()}? (y/n) ')
        if number_match == 'y':
            print(f"Hey, i know your favorite number! It's {get_stored_favorite_number()}.")
        else:
            get_favorite_number()


return_favorite_number()
