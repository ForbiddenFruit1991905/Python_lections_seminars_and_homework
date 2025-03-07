# Задание №6
# 📌 Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана).
# 📌 Функция формирует словарь с информацией о результатах отгадывания.
# 📌 Для хранения используйте защищённый словарь уровня модуля.
# 📌 Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря
# в удобном для чтения виде.
# 📌 Для формирования результатов используйте генераторное выражение.

from random import shuffle

def func_guess(word: str, data: list[str], attempts: int):
    count = 0
    while count < attempts - 1:
        count += 1
        if word in data:
            return f'Вы угадали с {count} попытки'
        else:
            print(f'Вы не угадали. Попробуйте еще раз. Осталось попыток {attempts - count}')
            word = input("Угадайте слово: ")
    return f'У вас закончились попытки. Правильные слова для отгадки: {", ".join(data)}'

def func_dict(riddle: list[str], data: list[str]) -> dict:
    return dict(zip(riddle, data))

def func_key_riddle(riddle_l: list[str], data: list[str], attempts: int):
    mixed_sequence = list(zip(riddle_l, data))
    shuffle(mixed_sequence)
    for riddle, answer in mixed_sequence:
        print(f'\n{riddle}')
        print(func_guess(input("Угадайте слово: "), [answer], attempts))




riddle_list = ["riddle for lemon: ", "riddle for apple: ", "riddle for banana: ", "riddle for strawberry: ", "riddle for melon: ", "riddle for watermelon: "]
my_list = ["lemon", "apple", "banana", "strawberry", "melon", "watermelon"]
print(func_guess(input("Угадайте слово: "), my_list, 3))
print(func_dict(riddle_list, my_list))
print(func_key_riddle(riddle_list, my_list, 3))