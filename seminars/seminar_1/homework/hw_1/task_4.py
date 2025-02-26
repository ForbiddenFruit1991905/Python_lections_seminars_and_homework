# Задача 4. Яма.
# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
# Вам поручили создать генератор ландшафта. Напишите программу, которая получает
# на вход число N и выводит на экран числа в виде ямы.
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345


lines = int(input("Введите глубину ямы: "))

# for i in range(lines, 0, - 1):
#     dots = (lines - i) * '.'
#     for left_nums in range(i, 0, - 1):
#         print(left_nums, end='')
#     # dots = i * '.'
#     print(dots)

for i in range(lines):
    for left in range(lines, lines - i - 1, -1):
        print(left, end='')
    dots = 2 * (lines - i - 1)
    print('.' * dots, end='')

    for right in range(lines - i, lines + 1):
        print(right, end='')
    print()