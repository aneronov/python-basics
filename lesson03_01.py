def div(el_1, el_2):
    el_3 = el_1 / el_2
    return el_3


while True:
    while True:
        try:
            a = float(input('введите делимое(число): '))
            break
        except:
            continue
    while True:
        try:
            b = float(input('введите делитель(число): '))
            if b != 0: break
            print('0 вводить нельзя')
            continue
        except:
            continue

    print()
    print(f'частное от делимого {a} и делителя {b} = {round((div(a, b)), 4)}', end='\n\n')

    quit = input('продолжить вычисления (да / нет)?')
    if quit.upper() == 'НЕТ': break
print()
print('работа программы завершена')

