class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w


    def mass_calc(self, t):
        return self._length * self._width * 25.7 * t


try:
    l = float(input('введите длину дорожного полотна в метрах: '))
    w = float(input('введите ширину дорожного полотна в метрах: '))
    road_ = Road(l, w)
    road_mass = road_.mass_calc(int(input('введите толщину дорожного полотна в см: ')))
    print('масса асфальта (тип А марка I), необходимого для покрытия всей дороги: ', road_mass / 1000, 'т.')
except ValueError:
    print('ошибка ввода данных')
