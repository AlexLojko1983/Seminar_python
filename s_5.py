# arr - отсоритровнная последовательность. k - число.
# Нужно найти индекс k. Если к нет, то вывести -1
# k = int(input('k= '))
# list_1 = [1, 2, 3, 4, 5, 6]
#
#
# def search(arr=list, k=int):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if arr[mid] < k:
#             low = mid + 1
#         elif arr[mid] > k:
#             high = mid - 1
#         else:
#             return mid
#
#     return -1
#
#
# print(search(list_1, k))

# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
#
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 2) + fib(n - 1)
#
#
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# n = int(input('n= '))
# # list_1 = [int(input('n[i] = ')) for i in range(n)]
# # max_list = max(list_1)
# # min_list = min(list_1)
# # for i in range(len(list_1)):
# #     if list_1[i] == max_list:
# #         list_1[i] = min_list
# # print(list_1)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
import math
n = int(input('n = '))
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        print('no')
        break
    else:
        print('yes')
