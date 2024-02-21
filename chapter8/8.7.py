# функция, строящая словарь с параметром, имеющим значение по умолчанию None
def make_album(musician, album, songs=''):
    """формирует словарь из заданных данных"""
    album_definition = {'name': musician.title(), 'title': album.title()}
    if songs:
        album_definition['songs'] = int(songs)
    return album_definition


message_0 = make_album('ravanna', 'девять кругов')
print(message_0)
message_1 = make_album('sllep theory', 'paper hearts', '6')
print(message_1)
message_2 = make_album('mitchel dae', 'blue banana peel', '1')
print(message_2)
