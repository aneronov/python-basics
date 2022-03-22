from itertools import count
try:
    start = int(input('Введите число(целое) - начало генерации чисел: '))
    step = int(input('Введите число(целое) - шаг генерации чисел: '))
    finish = int(input('Введите число(целое) - окончание генерации чисел: '))
    for i in count(start, step):
        if i > finish:
            break
        else:
            print(i)
except ValueError:
    print('введены данные, не соответсвтующие условию ввода!')
