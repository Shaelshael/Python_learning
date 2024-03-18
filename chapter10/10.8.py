# использование блока try-except для ошибки FileNotFound
def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'No file {filename} found.')
    else:
        file_content = contents.split()
        print(f'File "{filename}" contains: {file_content}\n')


filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    read_file(filename)
