# Напишите программу для определения, является ли число произведением двух чисел из данного набора.
# Программа должна выводить результат в виде ответа «ДА» или «НЕТ».
#
# Формат входных данных
# В первой строке подаётся число n (0<n<1000) – количество чисел в наборе. В последующих n строках вводятся целые числа,
# составляющие набор (могут повторяться). Затем следует целое число, которое является или не является произведением
# двух каких-то чисел из набора.
import random

# Формат выходных данных
# Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.

# Примечание 1. Само на себя число из набора умножиться не может.
# Другими словами, два множителя должны иметь разные индексы в наборе.

# Примечание 2. Для решения задачи используйте вложенные циклы.

n = int(input())
ls_of_nums = []
flag = False

for i in range(n):
    num = int(input())
    ls_of_nums.append(num)

score = int(input())

for i in range(len(ls_of_nums)):
    if flag:
        break
    x = int(ls_of_nums[i])
    for j in range(i+1, len(ls_of_nums)):
        y = int(ls_of_nums[j])
        if x * y == score:
            flag = True
            break

if flag:
    print("ДА")
else:
    print("НЕТ")
