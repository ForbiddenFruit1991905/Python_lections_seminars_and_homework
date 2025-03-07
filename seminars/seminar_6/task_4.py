# Задание №4
# 📌 Создайте модуль с функцией внутри.
# 📌 Функция получает на вход загадку, список с возможными вариантами
# отгадок и количество попыток на угадывание.
# 📌 Программа возвращает номер попытки, с которой была отгадана загадка
# или ноль, если попытки исчерпаны.

# def func_guess(guess_word: str, data: list[str], attempts: int):
#     count = 0
#     while count < attempts - 1:
#         count += 1
#         if guess_word in data:
#             return f'Вы угадали с {count} попытки'
#         else:
#             print(f'Вы не угадали. Попробуйте еще раз. Осталось попыток {attempts - count}')
#             guess_word = input("Угадайте слово: ")
#     return f'У вас закончились попытки. Правильные слова для отгадки: {", ".join(data)}'
#
# print(func_guess(
#     input("Угадайте слово: "),
#     ["lemon", "apple", "banana", "strawberry", "melon", "watermelon"],
#     3))


def func_guess(guess_word: str, data: list[str], attempts: int):
    count = 0

    while count < attempts - 1:
        count += 1
        if guess_word in data and guess_word == 'apple':
            return f'Вы угадали с {count} попытки'
        else:
            print(f'Вы не угадали. Попробуйте еще раз. Осталось попыток {attempts - count}')
            guess_word = input("Угадайте слово: ")
    return f'У вас закончились попытки. Правильные слова для отгадки: {", ".join(data)}'


print("Угадайте фрукт, который упал на голову Ньютона -> ")
print(func_guess(
    input("Ваш ответ: "),
    ["lemon", "apple", "banana", "strawberry", "melon", "watermelon"],
    3))