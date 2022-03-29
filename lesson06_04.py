from random import choice, randint
from time import sleep
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def show_speed(self):
        print(f'скорость {self.name} составляет {self.speed} км/ч')


    def go(self):
        print('разгон')


    def stop(self):
        print('остановка')


    def direction(self):
        print(choice(['налево', 'направо']))


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превысила скорость на {self.speed - 60} км/ч')
        else:
            print(f'скорость {self.name} составляет {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превысила скорость на {self.speed - 40} км/ч')
        else:
            print(f'скорость {self.name} составляет {self.speed} км/ч')


class PoliceCar(Car):
    pass


z = [TownCar, SportCar, WorkCar, PoliceCar]
flag = False
try:
    i = int(input('введите номер нужного типа машины (1 - городская, 2 - спортивная, 3 - рабочая, 4 полицейская): '))
    if i == 4:
        flag = True
    car_info = [randint(5, 100), choice(['синий', 'белый', 'черный', 'красный']), choice(['LADA', 'NIVA', 'KAMAZ', 'AUDI']), flag]
    a = z[i - 1](*car_info)
    a.go()
    sleep(1)
    a.direction()
    sleep(1)
    a.go()
    sleep(1)
    a.show_speed()
    sleep(1)
    a.stop()
except ValueError:
    print('ошибка ввода данных')
