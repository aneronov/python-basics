import re
with open('lesson05_06.txt', 'r', encoding='utf-8') as class_schedule_file:
    try:
        dictionary ={}
        l = class_schedule_file.readlines()
        for j in range(len(l)):
            hours_list = re.findall('[0-9]+',l[j])
            hours = 0
            for i in hours_list:
                hours += int(i)
            dictionary[l[j][:l[j].index(':')]] = hours
        print(dictionary)
    except ValueError:
        print('ошибка')

