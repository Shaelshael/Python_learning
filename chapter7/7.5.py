# цикл while с проверкой значения на >=/<= и выводом определенного значения при совпадении с определенным условием
prompt = '\nEnter your age so we can tell you the price of a ticket.'
age = ''
while age != 'quit':
    age = input(prompt)
    age = int(age)
    if age < 3:
        print('You can pass for free.')
    elif age <= 12:
        print("Ticket's cost is 10$.")
    else:
        print("Ticket's cost is 15$.")

# спросить, как при использовании переменной цикла в формате int() вписать в цикл его завершение
