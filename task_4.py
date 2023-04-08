# Задание 4.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31 22
# 37 43
# 51 86
#
# 3 5 32
# 2 4 6
# -1 64 -8
#
# 3 5 8 3
# 8 3 7 1
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, data:list):
        self.data = data

    def __str__(self):
        result = []
        for row in self.data:
            result.append(' '.join([str(k) for k in row]))
        return '\n'.join(result)

    def __add__(self, other):
        if len(self.data) == len(other.data):
            result = []
            for i, row in enumerate(self.data):
                new_list = list(map(lambda x, y: x + y, row, other.data[i]))
                result.append(new_list)
            return Matrix(result)
        else:
            return



list_lists_01 = [[4, 1, 7], [9, 2, 2], [1, 2, 1]]
list_lists_02 = [[3, 3, 1], [6, 5, 7], [9, 2, 4]]

matrix01 = Matrix(list_lists_01)
matrix02 = Matrix(list_lists_02)
matrix03 = matrix01 + matrix02

print(matrix01, end='\n\n')
print(matrix02, end='\n\n')
print(matrix03)