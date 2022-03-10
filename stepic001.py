
def my_func(word):
    return word.title()


x = []
flag = True
word = input('введите слова маленькими латинскими буквами через пробел - ')
for i in word:
    if i != ' ' and (ord(i) > 122 or ord(i) < 97):
        flag = False
        break
if flag:
    x = word.split()
    for i in range(len(x)):
        x[i] = my_func(x[i])
    print(' '.join(x))
else: print('введеная информация не соответствует условию')