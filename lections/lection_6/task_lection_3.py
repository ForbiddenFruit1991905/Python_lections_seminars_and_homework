# Задание.
# Перед вами пример кода. Что выведет программа после запуска?

import random
from sys import argv

print(random.uniform(int(argv[1]), int(argv[2])))
#  любое вещественное число между 10 1010
print(random.randrange(int(argv[1]), int(argv[2]), int(argv[1])))
# число от 10 до 1010 с шагом 10
print(random.sample(range(int(argv[1]), int(argv[2]), int(argv[1])), 10))
# число от 10 до 1010 с шагом 10 (10 случайных чисел)
# Скрипт запущен командой: python3 main.py 10 1010