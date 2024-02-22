# Напишите функцию func(num1, num2), принимающую в качестве аргументов два натуральных числа num1 и num2 и
# возвращающую значение True если число num1 делится без остатка на число num2 и False в противном случае.

# Результатом вывода программы должно быть "делится" (если функция func() вернула True) и "не делится"
# (если функция func() вернула False).

x = int(input())
y = int(input())


def is_divisible(num_1, num_2):
    return num_1 % num_2 == 0


if is_divisible(x, y):
    print("делится")
else:
    print("не делится")