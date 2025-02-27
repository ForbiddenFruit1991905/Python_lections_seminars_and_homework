# Задача 5. Нахождение анаграмм.
# Напишите программу, которая принимает два слова и определяет, являются ли они анаграммами.

# Подсказка №2. Создайте два пустых словаря для хранения частоты символов каждого слова.
# Один словарь для первого слова, другой для второго.
# Подсказка №3.
# Пройдитесь по каждому символу в первом слове и увеличьте счётчик в словаре. Повторите это для
# второго слова.
# Подсказка №4.
# После подсчета символов сравните оба словаря. Если они идентичны, слова являются анаграммами.

def func_anagram(txt_1: str, txt_2: str):
    data_1 = {}
    data_2 = {}
    if len(txt_1) != len(txt_2):
        print("Длина слов не совпала")
        return  False
    for key_char in txt_1:
        if key_char in data_1:
            data_1[key_char] += 1
        else:
            data_1[key_char] = 1
    for key_char in txt_2:
        if key_char in data_2:
            data_2[key_char] += 1
        else:
            data_2[key_char] = 1
    # проверка для себя
    # for key, value in data_1.items():
    #     print(f'[{key}: {value}]', end=' ')
    # for key, value in data_2.items():
    #     print(f'[{key}: {value}]', end=' ')
    if sorted(data_1.items()) == sorted(data_2.items()):
        return True
    else:
        return "Слова не являются анаграммами"

word_1 = input("Введите слово: ").lower()
word_2 = input("Введите слово: ").lower()
res = func_anagram(word_1, word_2)
print(res)
