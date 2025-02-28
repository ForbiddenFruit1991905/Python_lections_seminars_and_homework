# Функции iter и next могут работать с созданными
# генераторами. Например, так:

def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) # StopIteration