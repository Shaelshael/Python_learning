# функции, которые печатают сообщение из списка и переносят его в новый список
def message_sender(messages, sent_messages):
    """выводит сообщения из списка"""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


# сообщения для списка, сами списки и вызов функции
message_0 = 'Первое сообщение.'
message_1 = 'Второе сообщение.'
message_2 = 'Третье сообщение.'
message_list = [message_0, message_1, message_2]
messages_sent = []
message_sender(message_list, messages_sent)

# вызов списков, для проверки содержимого. всё содержимое message_list должно перейти в messages_sent
print('\nСписки и их содержимое:')
print(message_list)
print(messages_sent)
