# Задание №8
# 📌 Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# 📌 Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

num = int(input('Введите кол-во рядов: '))
step = ' '
star = '*'

for i in range(num):
    print(step * (num - i - 1) + star + (2 * i) * star)
    # step = ' ' + step
    # star += '**'

# for i in range(1, num * 2, 2):
#     print(step * ((num * 2 - i) // 2) + star * i)

# Другой вариант решения (семинар)
steps = int(input('Введите кол-во рядов: '))
figure = '*'
space = ' '
num_fig = 1
num_space = steps - 1
for _ in range(steps):
    print((space * num_space) + (figure * num_fig) + (space * num_space))
    num_fig += 2
    num_space -= 1