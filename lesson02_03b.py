season_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
while True:
    month_num = input('Введите номер месяца: ')
    if month_num.isalpha():
        print('ошибочка!')
        continue
    elif 1 <= int(month_num) <= 12:
        break
    print('ошибочка!')
    continue
for k, v in season_dict.items():
    for i in v:
        if i == int(month_num):
            print(k)