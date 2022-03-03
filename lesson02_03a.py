season_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
while True:
    month_num = input('Введите номер месяца: ')
    if month_num.isalpha():
        print('ошибочка!')
        continue
    elif 1 <= int(month_num) <= 12:
        break
    print('ошибочка!')
    continue
print(month_list[int(month_num) - 1], '-', season_list[int(month_num) - 1])
