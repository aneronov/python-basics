x = []
q = False
print('для завершения программы введите "Q"')
while True:
    a = input('введите числа через пробел: ')
    b = a.split()
    for i in b:
        if i.isdigit():
            x.append(int(i))
        elif i.upper() == "Q":
            q = True
            break
    print('сумма всех введенных чисел = ', sum(x))
    if q:
        print('работа программы завершена')
        break