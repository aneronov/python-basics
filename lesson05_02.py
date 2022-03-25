txt_file = open('lesson05_02.txt', 'r', encoding='utf-8')
list_txt = txt_file.readlines()
txt_file.close()
print(f'текстовый файл lesson05_02.txt содержит {len(list_txt)} строк:')
for i, q_words in enumerate(list_txt):
    print(f'{i}-я строка содержит {len(q_words.split())} слов')

