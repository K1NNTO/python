def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)
 
n = int(input("Задайте число:" ))
print(fib(n))