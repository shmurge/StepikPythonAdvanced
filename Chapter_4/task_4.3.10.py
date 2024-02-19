# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму.
# В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1
#       .....

# На вход программе подается число n.
# Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка
# (нумерация строк начинается с нуля).
#
# Формат входных данных
# На вход программе подается число n (n≥0).
#
# Формат выходных данных
# Программа должна вывести указанную строку треугольника Паскаля в виде списка.
#
# Примечание 1. Решение удобно оформить в виде функции pascal(),
# которая принимает номер строки и возвращает соответствующую строку треугольника Паскаля.

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

    return ls_1[row_num]


n = int(input())
result_ls = pascal(n)
print(result_ls)




