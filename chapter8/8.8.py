# упражнение 8.7, но с добавленным циклом while и пользовательскими данными
def make_album(musician, album, songs=''):
    """формирует словарь из заданных данных"""
    album_definition = {'name': musician.title(), 'title': album.title()}
    if songs:
        album_definition['songs'] = songs
    return album_definition


while True:
    print('\nType information about your favorite music album.'
          '')
    print('Or type "quit" to stop the program.')
    musician_name = input("\nMusician's name: ")
    if musician_name == 'quit':
        break

    album_name = input("Album's name: ")
    if album_name == 'quit':
        break

    song_amount = input("Amount of songs in album (optional): ")
    if song_amount == 'quit':
        break

    message = f'\n{make_album(musician_name, album_name, song_amount)}'
    print(message)
