# Напишите программу, которая выводит максимальный элемент в заштрихованной (левой нижней) области квадратной матрицы

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
#
# Примечание. Элементы главной диагонали также учитываются.


def create_sqrt_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = int(matrix[i][j])

    return matrix


n = int(input())
mat_1 = create_sqrt_matrix(n)
num = mat_1[0][0]

for i in range(1, len(mat_1)):
    for j in range(i+1):
        if mat_1[i][j] > num:
            num = mat_1[i][j]

print(num)