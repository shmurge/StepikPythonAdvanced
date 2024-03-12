# На вход программе подаются два натуральных числа n и m.
# Напишите программу, которая создает матрицу размером n×m, заполнив её "спиралью" в соответствии с образцом.

# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент.
# Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇


nums = input().split()
n = int(nums[0])
m = int(nums[1])
count = 1
mat_1 = [[0]*m for _ in range(n)]
flag = True
r = 0
c = 0

while count <= (n*m):
    for i in range(r, m):

        if mat_1[r][i] == 0:
            mat_1[r][i] = count
            count += 1
        else:
            continue

    c = mat_1[r].index(max(mat_1[r]))

    for i in range(r, n):
        if mat_1[i][c] == 0:
            mat_1[i][c] = count
            count += 1
        else:
            continue

    maximum = 0
    for i in range(len(mat_1)):
        if max(mat_1[i]) > maximum:
            maximum = max(mat_1[i])
            r = i
    c -= 1

    for i in range(c, -1, -1):
        if mat_1[r][i] == 0:
            mat_1[r][i] = count
            count += 1
        else:
            continue

    c = mat_1[r].index(max(mat_1[r]))
    r -= 1

    for i in range(r, -1, -1):
        if mat_1[i][c] == 0:
            mat_1[i][c] = count
            count += 1
        else:
            continue

    for i in range(n):
        if 0 in mat_1[i]:
            r = mat_1[i].index(0)
            c = mat_1[i].index(0)
            break

for row in range(n):
    for col in range(m):
        print(str(mat_1[row][col]).ljust(3), end='')
    print()
