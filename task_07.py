class MyComplex:
    def __init__(self, real, imaginary):
        self.__real = real
        self.__imaginary = imaginary

    @property
    def real(self):
        return self.__real

    @property
    def imaginary(self):
        return self.__imaginary

    def __add__(self, other):
        return MyComplex(self.__real + other.real, self.__imaginary + other.imaginary)

    def __mul__(self, other):
        return MyComplex(self.__real * other.real - self.__imaginary * other.imaginary,
            self.__real * other.imaginary + self.__imaginary * other.real)

    def __str__(self):
        return f'{self.__real} + {self.__imaginary}j'


my_complex_1 = MyComplex(37, 43)
my_complex_2 = MyComplex(64, -7)

print(my_complex_1 + my_complex_2)
print(my_complex_1 * my_complex_2)
