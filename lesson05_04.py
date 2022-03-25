eng_rus = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять'}
translated_txt = open('lesson05_04_transl.txt', 'w', encoding='utf-8')
with open('lesson05_04.txt', 'r', encoding='utf-8') as original_txt:
    while True:
        tmp_text = original_txt.readline().split()
        if not tmp_text:
            break
        tmp2_text = eng_rus[tmp_text[0].lower()]
        translated_txt.write(tmp2_text.capitalize() + ' ' + ' '.join(tmp_text[1:]) + '\n')
translated_txt.close()
print('создан файл lesson05_04_transl.txt')
