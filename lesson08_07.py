class Complex:
    def __init__(self, complex):
        self.complex = complex

    def __add__(self, other):
        return Complex([self.complex[i] + other.complex[i] for i in range(2)])

    def __mul__(self, other):
        return Complex([self.complex[0] * other.complex[0] - self.complex[1] * other.complex[1], self.complex[0] * other.complex[1] + self.complex[1] * other.complex[0]])

    def __str__(self):
        if self.complex[1] < 0:
            return f'{self.complex[0]}{self.complex[1]}i'
        return f'{self.complex[0]}+{self.complex[1]}i'


def cmplx(complex1_str):
    c = []
    for i in complex1_str:
        if i.isdigit():
            c.append(float(i))
    for i in range(len(complex1_str)):
        if complex1_str[i] == '-':
            if i == 0:
                c[0] *= -1
            else:
                c[1] *= -1
    return c


print(f'арифметические действия с комплексными числами a + bi:')
complex1_str = (input('введите первое комплексное число: ').strip())
complex2_str = (input('введите второе комплексное число: ').strip())
complex1 = list(cmplx(complex1_str))
complex2 = list(cmplx(complex2_str))
cp1 = Complex(complex1)
cp2 = Complex(complex2)
print('результат сложения комплексных чисел: ', cp1 + cp2)
print('результат умножения комплексных чисел: ', cp1 * cp2)
