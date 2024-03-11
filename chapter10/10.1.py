# чтение, перебор и сохранение строк из текстового файла

# чтение и вывод файла целиком
with open('learning_python.txt') as text_file:
    content = text_file.read()
    print(content.rstrip())

# чтение и вывод файла построчно
with open('learning_python.txt') as text_file:
    for line in text_file:
        print(line.strip())

# чтение файла, сохранение строк из него в отдельной переменной и вывод содержимого переменной отдельно от блока with
with open('learning_python.txt') as text_file:
    lines = text_file.readlines()

file_string = ''
for line in lines:
    file_string += line.strip()

print(file_string)
