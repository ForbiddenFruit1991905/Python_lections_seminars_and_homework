# Задание №5
# 📌 Добавьте в модуль с загадками функцию, которая хранит словарь
# списков.
# 📌 Ключ словаря - загадка, значение - список с отгадками.
# 📌 Функция в цикле вызывает загадывающую функцию, чтобы передать ей
# все свои загадки.

# def func_guess(word: str, data: list[str], attempts: int):
#     count = 0
#     while count < attempts - 1:
#         count += 1
#         if word in data:
#             return f'Вы угадали с {count} попытки'
#         else:
#             print(f'Вы не угадали. Попробуйте еще раз. Осталось попыток {attempts - count}')
#             word = input("Угадайте слово: ")
#     return f'У вас закончились попытки. Правильные слова для отгадки: {", ".join(data)}'
#
# print(func_guess(
#     input("Угадайте слово: "),
#     ["lemon", "apple", "banana", "strawberry", "melon", "watermelon"],
#     3))