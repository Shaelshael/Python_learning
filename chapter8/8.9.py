# функция со списком
def message_sender(messages):
    """выводит сообщения из списка"""
    for message in messages:
        print(message)


message_0 = 'Первое сообщение.'
message_1 = 'Второе сообщение.'
message_2 = 'Третье сообщение.'
message_list = [message_0, message_1, message_2]
message_sender(message_list)
