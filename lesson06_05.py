from random import choice
class Stationery:
    def __init__(self, title):
        self.title = title


    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'на данный момент {self.title} является инструментом отрисовки')


class Pencil(Stationery):
    def draw(self):
        print(f'на данный момент {self.title} является инструментом отрисовки')


class Handle(Stationery):
    def draw(self):
        print(f'на данный момент {self.title} является инструментом отрисовки')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
choice([pen, pencil, handle]).draw()
