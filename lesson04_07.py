def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f

try:
    n = int(input('Введите число(целое) для вычисления факториала: '))
    for el in fact(n):
        print(el)
except ValueError:
    print('введены данные, не соответсвтующие условию ввода!')