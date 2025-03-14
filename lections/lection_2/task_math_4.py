# Комплексные числа — числа с мнимой единицей, квадратным корнем из минус одного.

a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')

# В каждом случае получим (2+3j) — комплексное число в Python.

# Внимание! Python для обозначения мнимой единицы использует букву "j",
# а в математике принято использовать "i". Во всём остальном математические
# операции в Python совпадают с классической математикой.