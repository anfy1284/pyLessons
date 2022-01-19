# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной 
# схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов 
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки 
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

from typing import Match


class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def __str__(self) -> str:
        result_str = ''
        for row in self.matrix:
            result_str += str(row) + '\n'
        return result_str

    def __add__(self, other):
        result = []
        larger_matrix, smaller_matrix = (self.matrix, other.matrix) if len(self.matrix) > len(other.matrix) else (other.matrix, self.matrix)
        larger_matrix_iterator = iter(larger_matrix)
        for matrix_a_row in smaller_matrix:
            matrix_b_row = next(larger_matrix_iterator)
            larger_row, smaller_row = (matrix_a_row, matrix_b_row) if len(matrix_a_row) > len(matrix_b_row) else (matrix_b_row, matrix_a_row)
            larger_row_iterator = iter(larger_row)
            result_row = []
            for item_a in smaller_row:
                item_b = next(larger_row_iterator)
                result_row.append(item_a + item_b)
            result.append(result_row)
        return Matrix(result)


my_matrix_1 = Matrix([[1,3],[4,5,6],[7,8,9],[17,18,19]])
my_matrix_2 = Matrix([[9,8,7],[5,4],[3,2,1]])
my_matrix_3 = my_matrix_1 + my_matrix_2
print(my_matrix_3)
    

