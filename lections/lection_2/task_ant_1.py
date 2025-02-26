# можно указать несколько типов через вертикальную черту

a: int | float = 42
b: float = float(input('Введи число: '))
a = a / b
print(a)