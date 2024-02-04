# проверки равенства
games = "good"
print('Are games good?')
print(games == 'good')
print('Are games a waste of time?')
print(games == 'waste of time')
# проверка с функцией lower()
car = 'BMW'
print('\nI dont have BMW.')
print(car.lower() == 'bmw')
# проверки на больше/меньше/равно/не равно
number = 11
print('\nMy numer is 10?')
print(number == 10)
print('My numer is 11?')
print(number == 11)
print('My number is 12?')
print(number != 11)
print('My number is not 15?')
print(number != 15)
print('My number is more then 5?')
print(number > 5)
print('My number is more then 15?')
print(number > 15)
print('My number is less then 20?')
print(number < 20)
print('My number is less then 10?')
print(number < 10)
print('My number is more or equal to 11?')
print(number >= 11)
print('My number is more or equal to 15?')
print(number >= 15)
print('My number less or equal to 11?')
print(number <= 11)
print('My number less or equal to 10?')
print(number <= 10)
# and и or
temperature = 36.6
age = 28
print('\nI am 28 years old and my normal temperature is 36.6.')
print(age == 28 and temperature == 36.6)
print('I am 30 years old and my normal temperature is 36.6.')
print(age == 30 and temperature == 36.6)
print('Now we check 1/2 — age or temperature. Statement will be true if i am 28 years old or my temperature is 36.6.')
print(age == 30 or temperature == 36.6)
print('This statement will be false if i am not 28 years old and my temperature is not 36.6.')
print(age == 26 or temperature == 37.6)
# проверка вхождения в список
dishes = ['pizza', 'sushi', 'soup']
print('\nNow we check if pizza is in our list of dishes.')
print('pizza' in dishes)
print('Maybe we have some fries in our list?')
print('fries' in dishes)
print('Guess we dont.')
# проверка на отсутствие элемента в списке
print('\nThis statement will be true, if we dont have fries in our list.')
print('fries' not in dishes)
print('And this statement will be false, if we dont have pizza in our list.')
print('pizza' not in dishes)