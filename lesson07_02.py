from abc import ABC
class Clothes(ABC):
    def __init__(self, x):
        self.x = x
    def __and__(self, other):
        return f'общий расход ткани: {self.coat_calc + other.costume_calc} п.метров(др единицы)'



class Coat(Clothes):
    @property
    def consumption(self):
        coat_calc = round(self.x / 6.5 + 0.5, 2)
        return f'необходимо {coat_calc} п.метров(др единицы) ткани для пошивки пальто.'


class Costume(Clothes):
    @property
    def consumption(self):
        costume_calc = round(self.x * 2 + 0.3, 2)
        return f'необходимо {costume_calc} п.метров(др единицы) ткани для пошивки костюма.'


try:
    coat = Coat(int(input('введите размер верхней одежды(арабские цифры): ')))
    costume = Costume(float(input('введите рост(метры, разделитель целой / дробной части - "."): ')))
    print(coat.consumption)
    print(costume.consumption)
    print(coat.consumption + costume.consumption)
except (ValueError, NameError, TypeError):
    print('ошибка ввода')

