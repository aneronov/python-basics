class Cell:
    def __init__(self, q):
        self.q = q

    def __add__(self, other):
        return Cell(self.q + other.q)


    def __sub__(self, other):
        if (self.q - other.q) >= 0:
            return Cell(self.q - other.q)
        else:
            return f'операция не может быть выполнена'


    def __mul__(self, other):
        return Cell(self.q * other.q)


    def __truediv__(self, other):
        return Cell(self.q // other.q)


    def __str__(self):
        return f'{self.q}'


    def make_order(self, z):
        x = self.q
        while True:
            if x >= z:
                print('*' * z)
                x -= z
            else:
                print('*' * x)
                break


a = Cell(15)
b = Cell(14)
c = Cell(5)
print(f'клетка "a" имеет {a} ячеек\nклетка "b" имеет {b} ячеек\nклетка "c" имеет {c} ячеек\n')
print('целая часть от a / b = ', a / b)
print('a + b + c =', a + b + c)
print('b - c =', b - c)
print('c - a =', c - a)
print('c * c * b =', c * c * b)
a.make_order(4)
print()
b.make_order(6)