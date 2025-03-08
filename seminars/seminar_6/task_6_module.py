from task_4 import *
from random import shuffle

def func_dict_secret(riddle_l: list[str], data: list[str], attempts: int) -> dict:
    _secret_dict = {}
    count = 0
    while count < attempts:
        count += 1
        mixed_sequence = list(zip(riddle_l, data))
        shuffle(mixed_sequence)
        for riddle, answer in mixed_sequence:
            print(f'\n{riddle}')
            result = func_guess(input("Угадайте слово: "), [answer], attempts)
            _secret_dict[riddle] = count
            if answer in result:
                break
            if count == attempts:
                break
    return _secret_dict

# 📌 Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря
# в удобном для чтения виде.
# 📌 Для формирования результатов используйте генераторное выражение.

def func_print_secret_dict():
    res = func_dict_secret(riddle_list, my_list, 3)
    my_dict_comp = {riddle: count for riddle, count in res.items()}
    readable_results = {riddle: f'Угадано с {count} попытки' if count != 3 else 'Не угадано' for riddle, count in
                        my_dict_comp.items()}
    for riddle, result in readable_results.items():
        print(f'{riddle}: {result}')

riddle_list = ["riddle for lemon: ", "riddle for apple: ", "riddle for banana: ", "riddle for strawberry: ", "riddle for melon: ", "riddle for watermelon: "]
my_list = ["lemon", "apple", "banana", "strawberry", "melon", "watermelon"]
print(func_dict_secret(riddle_list, my_list, 3))
print(func_print_secret_dict())