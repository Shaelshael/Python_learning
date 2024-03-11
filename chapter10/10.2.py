# построчное чтение и замена слов в текстовом файле
with open('learning_python.txt') as text_file:
    lines = text_file.readlines()
text_unchanged = ''
for line in lines:
    text_unchanged += line

# выводим неизмененный текст
print(text_unchanged)
# заменяем часть слов в изначальном тексте
text_changed = text_unchanged.replace('Python', 'C')
# выводим измененный текст
print(text_changed)
