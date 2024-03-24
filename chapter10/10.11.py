# запрашиваем любимое число, сохраняем его в файле, выгружаем из файла и сообщаем число
import json


def ask_number():
    # запрашивает число и сохраняет его в json-файле
    favorite_number = input('Hallo! Enter your favorite number: ')
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)


def get_number():
    # выгружает число из файла и сообщает его пользователю
    filename = 'favorite_number.json'
    with open(filename, 'r') as f:
        number_acquired = json.load(f)
        print(f"Hey, i know your favorite number! It's {number_acquired}.")


ask_number()
get_number()
