# функция с параметром и аргументом
def favorite_books(book):
    """функция, выводящая любимую книгу, в зависимости от значения аргумента"""
    print(f'One of my favorite books is "{book.title()}".')


favorite_books('the lord of the rings')
