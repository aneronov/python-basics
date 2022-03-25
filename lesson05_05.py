with open('lesson05_05.txt', 'w+', encoding='utf-8') as num_file:
    try:
        print('введите числа через пробел.')
        num_file.write(input())
        num_file.seek(0)
        tmp_list = num_file.read().split()
        sum = 0
        for i in tmp_list:
            sum += int(i)
        print('сумма чисел, указанных в файле lesson05_05.txt = ', sum)
    except ValueError:
        print('ошибка типа данных')
