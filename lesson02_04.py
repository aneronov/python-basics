any_string = input('Введите любой текст: ')
string_to_list = any_string.split()
for i, j in enumerate(string_to_list, 1):
    print(i, j[:10])