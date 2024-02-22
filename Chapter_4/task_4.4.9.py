# На вход программе подаются два натуральных числа n и m,
# каждое на отдельной строке — количество строк и столбцов в матрице.
# Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке;
# подряд идут элементы сначала первой строки, затем второй, и т.д.

# Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы,
# выводит пустую строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами:
# первая строка выводится как первый столбец, и так далее.
#
# Формат входных данных
# На вход программе подаются два числа n и m — количество строк и столбцов в матрице, далее идут
# n×m слов, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести считанную матрицу, за ней пустую строку и ту же матрицу,
# но поменяв местами строки со столбцами. Элементы матрицы разделять одним пробелом.

n = int(input())
m = int(input())


def create_matrix(rows, cols):
    matrix = list()
    ls = list()
    for _ in range(rows):
        ls = []
        for _ in range(cols):
            word = input()
            ls.append(word)
        matrix.append(ls)

    return matrix


def print_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            print(str(matrix[r][c]), end=' ')
        print()
    print()
    for c in range(cols):
        for r in range(rows):
            print(str(matrix[r][c]), end=' ')
        print()

mat_1 = create_matrix(n, m)
print_matrix(mat_1)