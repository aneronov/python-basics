from time import sleep
class TrafficLight:
    __color = 'красный, желтый, зеленый'

    def running(self):
        print(u"\u001b[41m   ", end='')
        sleep(7)
        print('\r', end='')
        print(u"\u001b[43m   ", end='')
        sleep(2)
        print('\r', end='')
        print(u"\u001b[42m   ", end='')
        sleep(7)
        print('\r', end='')

try:
    cicle = int(input('введите кол-во циклов работы светофора: '))
    for _ in range(cicle):
        a = TrafficLight()
        a.running()
except ValueError:
    print('ошибка ввода')
print(u'\u001b[0m   ')
