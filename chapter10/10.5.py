# спрашиваем и сохраняем ответ в файле
reason_file = 'reasons.txt'
print('Hallo! Here you can tell us some reasons why you like programming.')
while True:
    reason = input('Enter a reason or type "end" to stop the program: ')
    if reason != 'end':
        with open(reason_file, 'a') as file_object:
            file_object.write(f'{reason}\n')
    else:
        break
