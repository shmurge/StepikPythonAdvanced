# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы
# относительно горизонтальной оси симметрии.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести матрицу, в которой зеркально отображены элементы относительно горизонтальной оси симметрии.


def create_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


n = int(input())
mat_1 = create_matrix(n)

for i in range(n-1, -1, -1):
    row = mat_1[i]
    print(*row)