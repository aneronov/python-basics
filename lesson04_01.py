from sys import argv
def zp(h, time_rate, bonus):
    return h * time_rate + bonus


try:
    file_name, h, time_rate, bonus = argv
    h = float(h)
    time_rate = float(time_rate)
    bonus = float(bonus)
    print(f'ЗП согласно отработанным часам - ({h}) и премии в размере {bonus} рублей составляет -', zp(h, time_rate, bonus), 'рублей', end='\n\n\n')
except ValueError:
    print('ошибка ввода - после имени файла по расчету ЗП в командой строке введите кол-во отработанных часов, ставку за час работы и премию через пробел.', end='\n\n\n')
