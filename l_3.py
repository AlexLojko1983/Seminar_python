def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 2) + fib(n - 1)
list_1 = []
for i in range(1,10):
    list_1.append(fib(i))
print(list_1)
