# проверка введённого пользователем числа на чет/нечет
number = input('Type a number and i will check if it is even or odd: ')
number = int(number)
if number % 2 == 0:
    print(f'The number {number} is even.')
else:
    print(f'The number {number} is odd.')
