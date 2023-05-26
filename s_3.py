# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
#
# print(len(set(list_1)))




data = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"}
]

unique_values = set()

for item in data:
    for value in item.values():
        unique_values.add(value.strip())  # Добавляем уникальные значения в множество

print(list(unique_values))