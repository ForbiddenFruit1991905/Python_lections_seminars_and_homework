# Модуль fraction
# Для работы с дробями есть модуль fractions.

import fractions

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)

# Модуль полезен при работе с бесконечными дробями, когда decimal не обеспечивает необходимую точность хранения числа.