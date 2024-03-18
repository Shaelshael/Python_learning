# использование блока try-except для ошибки FileNotFound с фичей pass
def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        file_content = contents.split()
        print(f'File "{filename}" contains: {file_content}\n')


filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    read_file(filename)
