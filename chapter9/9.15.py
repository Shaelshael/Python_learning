# аналог задачи 9.14 без класса + цикл, считающий и сравнивающий количество использований функции с заданным параметром
from random import choice

lottery_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')
my_ticket_number = [3, 2, 'a', 1]
number_of_iterations = 0

while True:
    win_ticket_number = [choice(lottery_numbers) for iteration in range(4)]
    if win_ticket_number != my_ticket_number:
        number_of_iterations += 1
    else:
        print(f'My ticket {my_ticket_number} has won!')
        print(f"It took {number_of_iterations} attempts to match.")
        break
