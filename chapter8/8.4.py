# функция с аргументами по умолчанию
def make_shirt(size='l', text='i learn python!'):
    """вывод размера и текста футболки"""
    print(f'Your shirt size is "{size.upper()}" and text on it is: "{text.title()}"')


make_shirt()
make_shirt('m', 'i love beer!')
