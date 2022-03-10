def my_func(x, y):
    z = 1 / x
    for i in range(abs(y) - 1):
        z *= (1 / x)
    return z

while True:
    try:
        x = float(input('введите действительное положительное число: '))
        if x < 0:
            print('число отрицательное!')
            continue
        break
    except:
        print('ввели не число!', end='\n\n')
        continue
while True:
    try:
        y = int(input('введите целое отрицательное число: '))
        if y > 0:
            print('число положительное!')
            continue
        break
    except:
        print('число дробное или содержит символы', end='\n\n')
        continue

print(f'{x} в степени {y} = ', my_func(x, y))