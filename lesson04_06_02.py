from itertools import cycle
original_list = [i for i in range(1, 45, 6)]
j = 0
try:
    repeat = int(input('Введите число(целое) - кол-во выводимых символов: '))
    for i in cycle(original_list):
        if j > repeat:
            break
        print(i)
        j += 1
except ValueError:
    print('введены данные, не соответсвтующие условию ввода!')
