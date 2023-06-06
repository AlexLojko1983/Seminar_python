# list_1 = [1,2,5,8,6,4,44,88]
# list_2 = [4,8,88,5,1]
# list_3 = [i for i in list_1 if list_2.count(i) == 0]
# print(list_3)


# list_1 = [1, 2, 3, 4, 5]
# count = 0
# for i in range(1, len(list_1) - 1):
#     if list_1[i] > list_1[i - 1] and list_1[i] > list_1[i + 1]:
#         count += 1
# print(count)

k = 100000

import math


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
