# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа.

# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.

# Формат выходных данных
# Программа должна вывести одно число – количество элементов списка, больших предыдущего.

nums_text = input()
ls_of_nums = nums_text.split()
num_1 = int(ls_of_nums[0])
num_2 = None
count = 0

for i in range(1, len(ls_of_nums)):
    num_2 = int(ls_of_nums[i])
    if num_2 > num_1:
        count += 1
    num_1 = num_2

print(count)

