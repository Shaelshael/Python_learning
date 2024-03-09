#  импорт и использование модуля из библиотеки в классе
from random import choice


class LotteryTicket:
    """модель лотереи"""
    def __init__(self):
        """описывает характеристики, имеющиеся у лотереи и билетов"""
        self.lottery_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')
        self.win_ticket_number = []

    def choose_win_ticket(self):
        """выбирает случайный 4-значный номер билета и считает количество повторений функции до совпадения билетов"""
        self.win_ticket_number = [choice(self.lottery_numbers) for x in range(4)]
        print(f'Number {self.win_ticket_number} has won!')


lottery_0 = LotteryTicket()
lottery_0.choose_win_ticket()
