def my_func(word):
    return word.title()


flag = True
word = input('введите слово маленькими латинскими буквами - ')
for i in word:
    if ord(i) > 122 or ord(i) < 97:
        flag = False
        break

if flag: print(my_func(word))
else: print('введеная информация не соответствует условию')