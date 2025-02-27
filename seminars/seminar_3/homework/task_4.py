# Задача 4. Генерация паролей.
# Напишите программу, которая генерирует случайный пароль заданной длины,
# состоящий из букв, цифр и специальных символов.

# Подсказка№2.
# Примите длину пароля от пользователя, используя функцию input(), и преобразуйте
# её в целое число с помощью int().
# Подсказка №3.
# Определите набор символов для пароля, используя строки из модуля string.
# Объедините буквы, цифры и специальные символы в одну строку.
# Подсказка №4.
# Используйте генератор выражений и функцию random.choice() для выбора
# случайных символов из набора. Соберите символы в строку с помощью метода join().

import random
import string

n = 5  # Желаемая длина последовательности выбранных элементов
random_digits = ''.join(random.choice(string.digits) for _ in range(n))
random_letter = ''.join(random.choice(string.ascii_letters) for _ in range(n))
random_special_char = ''.join(random.choice(string.punctuation) for _ in range(n))
custom_characters = random_digits + random_letter + random_special_char
len_password = int(input("Введите целочисленную длину пароля: "))
password = []

while len(password) < len_password:
    password.append(random.choice(custom_characters))
print(''.join(password))


