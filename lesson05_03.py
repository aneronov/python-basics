with open('lesson05_03.txt', 'r', encoding='utf-8') as text:
    list_txt = text.readlines()
    for i in range(len(list_txt)):
        list_txt[i] = list_txt[i].split()
name = []
sum_ = 0
try:
    for i, j in list_txt:
        if int(j) < 20000:
            name.append(i)
        sum_ += int(j)
    average_salary = sum_ / len(list_txt)
    print(f'Средняя ЗП сотрудников: {average_salary} рублей.')
    print('Сотрудники с окладом меньше 20000 рублей:', *name, sep='\n')
except ValueError:
    print('Ошибка данных в текстовом файле!')
