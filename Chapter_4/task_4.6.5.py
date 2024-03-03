# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n,
# заполнив её в соответствии с образцом.

# Формат входных данных
# На вход программе подается натуральное число n — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом:
# разместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.

# Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент.
# Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

n = int(input())
mat_1 = [[0]*n for _ in range(n)]

for i in range(n):
    mat_1[i][i] = 1
    mat_1[i][n-i-1] = 1

for row in range(n):
    for col in range(n):
        print(str(mat_1[row][col]).ljust(3), end='')
    print()
