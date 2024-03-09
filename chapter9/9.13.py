# импорт и использование модуля из библиотеки
from random import randint


class Die:
    def __init__(self, sides=6):
        """модель 6-гранного кубика"""
        self.sides = sides

    def roll_die(self):
        """бросок кубика с выбором числа от 1 до количества граней кубика"""
        rolling_sides = self.sides
        number = randint(1, rolling_sides)
        print(number)


die_1_6 = Die(6)
die_1_6.roll_die()

die_1_10 = Die(10)
die_1_10.roll_die()

die_1_20 = Die(20)
die_1_20.roll_die()
