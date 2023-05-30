# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
#
# 20:22
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#
# string = 'a a a b c a a d d d'
# elements = {}
# mess = ""
# for element in string.split():
#     if element not in elements:
#         elements[element] = 1
#         mess += f"{element} "
#     else:
#         elements[element] += 1
#         mess += f"{element}_{elements[element]-1} "
# print(mess)

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# str_1 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# # str_1 = input()
# list_1 = str_1.strip().split()
#
# set_1 = set(list_1)
# print(set_1)
# print(len(set_1))

# Задача No29. Решение в группах # Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего
# элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца
# сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах

n = int(input('кол-во чисел: '))
list_2 = [int(input('числа ')) for i in range(n)]
print(max(list_2[:list_2.index(0)]))