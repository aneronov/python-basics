with open('lesson05_01.txt', 'w', encoding='utf-8') as new_file:
    print('Веедите несколько строк любой информации.')
    print('Для завершения ввода информации введите пустую строку!')
    while True:
        tmp = input()
        new_file.write(tmp + '\n')
        if tmp == '':
            break
