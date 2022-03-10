def my_func(x):
    return sum(x) - min(x)

x = []
while True:
    try:
        a = float(input('введите число a: '))
        break
    except:
        print('ввели не число!', end='\n\n')
        continue
x.append(a)
while True:
    try:
        b = float(input('введите число b: '))
        break
    except:
        print('ввели не число!', end='\n\n')
        continue
x.append(b)
while True:
    try:
        c = float(input('введите число c: '))
        break
    except:
        print('ввели не число!', end='\n\n')
        continue
x.append(c)
print('сумма наибольших двух введенных аргументов = ', my_func(x))