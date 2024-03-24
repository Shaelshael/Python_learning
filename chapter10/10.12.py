# программы из 10.11 в одном файле
import json


def get_favorite_number():
    # выгружает число из файла и сообщает его пользователю. Если файла с числом нет - запрашивает число, сохраняет и
    # выгружает
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
        print(f"Hey, i know your favorite number! It's {number_acquired}.")


get_favorite_number()
