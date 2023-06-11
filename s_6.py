# list_1 = [1,2,5,8,6,4,44,88]
# list_2 = [4,8,88,5,1]
# list_3 = [i for i in list_1 if list_2.count(i) == 0]
# print(list_3)


# list_1 = [1, 2, 3, 4, 5]
# count = 0
# for i in range(1, len(list_1) - 1):
#     if list_1[i] > list_1[i - 1] > list_1[i + 1]:
#         count += 1
# print(count)


# Два различных натуральных числа n и m называются дружественными, если сумма делителей
# числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести
# все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
k = 100000
import math
#
#
def divider(num=int):
    list_1 = [1]
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            list_1.append(i)
            list_1.append(num // i)
    return list_1


for i in range(k, 0, -1):
    if i < sum(divider(i)) <= k and sum(divider(sum(divider(i)))) == i:
        print(i, sum(divider(i)))

# list_1 = [1,2,3,4,5]
# list_2 = list(map(lambda x: x, list_1))
# print(list_2)
# import math
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#
#
# def find_farthest_orbit(orbits):
#     s = [0]
#     k = 0
#     for i in orbits:
#         if i[0] == i[1]:
#             continue
#         elif (math.pi * i[0] * i[1]) > s[0]:
#             s[0] = (math.pi * i[0] * i[1])
#             k = i
#     return k
#
# print(find_farthest_orbit(orbits))

# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные друг
# другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

import random

list_size = int(input("Введите количество элементов массива: "))
list1 = [random.randint(0, 10) for i in range(list_size)]
set1 = set(list1)
count = 0
for i in set1:
    count += list1.count(i) // 2

print(list1)
print(f'Количество парных чисел в массиве: {count}')


