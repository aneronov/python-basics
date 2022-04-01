class Matrix:
    def __init__(self, mtrx):
        self.mtrx = mtrx


    def __add__(self, other):
        return Matrix([[self.mtrx[j][i] + other.mtrx[j][i] for i in range(len(self.mtrx[j]))] for j in range(len(self.mtrx))])


    def __str__(self):
        return '\n'.join('\t'.join(map(str, i)) for i in self.mtrx)


try:
    m1 = Matrix([[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]])
    m2 = Matrix([[5, 6, 7, 8], [90, 80, 50, 60], [500, 700, 400, 200]])
    m3 = Matrix([[1, 6, 3, 8], [10, 80, 20, 60], [200, 200, 300, 600]])
    print('m1:', m1, sep='\n', end='\n\n')
    print('m2:', m2, sep='\n', end='\n\n')
    print('m3:', m3, sep='\n', end='\n\n')
    print('m1 + m2:', m1 + m2, sep='\n', end='\n\n')
    print('m3 + m1:', m3 + m1, sep='\n', end='\n\n')
except (ValueError, NameError, TypeError):
        print('ошибка')


