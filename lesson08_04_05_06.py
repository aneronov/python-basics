class WareHouse:
    def __init__(self):
        self.dict_ = {}

    def add_(self, equipment):
        self.dict_.setdefault(equipment.class_name(), []).append(str(equipment))
        print(f'на складе - {self.dict_}')

    def remove_(self, equipment):
        if self.dict_[equipment]:
            print(self.dict_.setdefault(equipment).pop(0))
        print(f'на складе - {self.dict_}')


class OfficeEquipment:
    def __init__(self, name, country, year):
        self.name = name
        self.country = country
        self.year = year
        self.group = self.__class__.__name__

    def class_name(self):
        return f'{self.__class__.__name__}'


class Printer(OfficeEquipment):
    def __init__(self, name, country, year, speed):
        super().__init__(name, country, year)
        self.speed = speed
        # speed - q'ty of paper by minute

    def __str__(self):
        return f'{self.name} {self.country} {self.year} {self.speed}'


class Scaner(OfficeEquipment):
    def __init__(self, name, country, year, type_):
        super().__init__(name, country, year)
        self.type_ = type_
        # type - portable or stationary

    def __str__(self):
        return f'{self.name} {self.country} {self.year} {self.type_}'


class CopyMachine(OfficeEquipment):
    def __init__(self, name, country, year, work_param):
        super().__init__(name, country, year)
        self.work_param = work_param
        # work_param - handle (1 by 1 of paper's list) or auto (scanning all lists of paper )

    def __str__(self):
        return f'{self.name} {self.country} {self.year} {self.work_param}'


w_h = WareHouse()
print('добавляем на склад:')
p1 = Printer('Samsung', 'Korea', 2002, '60 l/m')
print(p1.class_name(), p1)
w_h.add_(p1)
print()
print('добавляем на склад:')
p2 = Printer('Panasonic', 'Japan', 1990, '40 l/m')
print(p2.class_name(), p2)
w_h.add_(p2)
print()
print('добавляем на склад:')
s1 = Scaner('HP', 'USA', 2010, 'stationary')
print(s1.class_name(), s1)
w_h.add_(s1)
print()
print('добавляем на склад:')
s2 = Scaner('Fujitsu', 'Japan', 2010, 'portable')
print(s2.class_name(), s2)
w_h.add_(s2)
print()
print('добавляем на склад:')
c_m1 = CopyMachine('XEROX', 'USA', 1980, 'handle')
print(c_m1.class_name(), c_m1)
w_h.add_(c_m1)
print()
print('добавляем на склад:')
c_m2 = CopyMachine('Rongda', 'China', 2020, 'auto')
print(c_m2.class_name(), c_m2)
w_h.add_(c_m2)
print()
print()
print('удаляем первое пришедшее на склад оборудование из раздела "Printer"')
w_h.remove_("Printer") # удаляет первое добавленное оборудование

