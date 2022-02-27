proceeds = int(input('Введите выручку фирмы: '))
expenses = int(input('Введите издержки фирмы: '))
if proceeds > expenses:
    print('Фирама работает с прибылью!')
    profit = proceeds - expenses
    efficiency = profit / proceeds
    print('Рентабильность выручки: ', efficiency)
    staff_q = int(input('Введите кол-во сотрудников фирмы: '))
    print('Прибыль фирмы в расчёте на одного сотрудника составляет ', profit / staff_q)
elif proceeds < expenses:
    print('Фирма работает в убыток')
else:
    print('выручка равна издержкам')