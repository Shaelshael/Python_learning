# анализ текста из текстового файла
def read_text(text):
    with open(text, encoding='utf-8') as f:
        # высчитывает количество определенных слов в тексте
        content = f.read()
        amount_of_words = content.split()
        print(f'{amount_of_words.count('the')}')


text_list = ['../text_files/the_picnic_party.txt', '../text_files/the_morgan_trail.txt',
             '../text_files/an_altruist.txt']
for text in text_list:
    read_text(text)
