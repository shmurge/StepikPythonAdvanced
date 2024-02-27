# На вход программе подается натуральное число n.
# Напишите программу, которая выводит первые n строк треугольника Паскаля.

# Формат входных данных
# На вход программе подается число n (n≥1).
#
# Формат выходных данных
# Программа должна вывести первые
# n строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.


def pascal(row_num): # принимает желаемый номер строки Треугольника Паскаля и возвращает его в виде списка
    ls_1 = list()
    ls_2 = list()

    for i in range(row_num + 1):
        for j in range(i + 1):
            if j == 0 or j == i: # Первое и последнее число = 1
                ls_2.append(1)
                continue
            # в эту переменную заносится сумма двух чисел из списка, созданного на прошлой итерации
            # например элемент №3 этого списка равен сумме элементов №2 и №3 предыдущего
            num = ls_1[i-1][j-1] + ls_1[i-1][j]
            ls_2.append(num)

        ls_1.append(ls_2)
        ls_2 = []

    return ls_1


n = int(input())
result_ls = pascal(n)

for i in range(len(result_ls)-1):
    row = result_ls[i]
    print(*row)