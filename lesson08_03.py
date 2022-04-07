class IsDigit(Exception):
    def __str__(self):
        return f'любые символы недопустимы!'


list_ = []
q = False
print('для завершения программы введите "stop"')
while True:
    a = input('введите числа через пробел: ')
    b = a.split()
    for i in b:
        try:
            if i.upper() == "STOP":
                q = True
                break
            if not i.isdigit():
                raise IsDigit
            list_.append(int(i))
        except IsDigit as err:
            print(err)
    if q:
        print('работа программы завершена')
        break
print('список введенных чисел: ', *list_)