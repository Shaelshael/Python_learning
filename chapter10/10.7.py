# использование блока try-except для ошибки ValueError
# пропустил задачу 10.6, случайно сразу написал через цикл while программу
print('Enter two numbers and i will summ them.')
print('Type "q" if you want to quit.')
while True:
    number_0 = input('Enter the first number: ')
    if number_0 == 'q':
        break
    number_1 = input('Enter the second number: ')
    if number_1 == 'q':
        break
    try:
        summary = int(number_0) + int(number_1)
    except ValueError:
        print('You should enter digits, not words.')
    else:
        print(f'Summary of your numbers is: {summary}')
