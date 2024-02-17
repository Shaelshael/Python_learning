# запрос инфы от пользователя + проверка значения на > через if
message = input('How much guests you will bring with you? ')
message = int(message)
if message > 8:
    print('Sorry, you will need to wait a bit.')
else:
    print('We have enough places, welcome!')
