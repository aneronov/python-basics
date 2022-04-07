class DivZeroError(Exception):
    def __str__(self):
        return f"делитель должен быть отличен от '0'!"

class Calculation:
    def __init__(self, divisible, divisor):
        self.divisible = divisible
        self.divisor = divisor

    def calc(self, divisible, divisor):
        if divisor == 0:
            raise DivZeroError()
        return divisible / divisor

try:
    divisible = float(input('введите делимое: '))
    divisor = float(input('введите делитель: '))
    a = Calculation(divisible, divisor)
    try:
        print(f'частное от делимого {divisible} и делителя {divisor} равно {a.calc(divisible, divisor)}')
    except DivZeroError as err:
        print(err)
except ValueError:
    print('вводить нужно только числа!')
