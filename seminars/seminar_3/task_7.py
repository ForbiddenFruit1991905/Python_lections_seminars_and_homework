# Задание №7.
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке
# без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение —
# частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают
# или не совпадают в ваших решениях.

# Вар.1 без использования метода count()

txt = input("Введите текст соблюдая пробелы: ")
new_txt = sorted(txt.replace(' ', '', len(txt)).lower())
res_txt = {}

for key in new_txt:
    if key in res_txt:
        res_txt[key] += 1
    else:
        res_txt[key] = 1
for key, value in res_txt.items():
    print(f'[{key}: {value}]', end=' ')

print()

# Вар.2 с использованием метода count()

# txt = input("Введите текст соблюдая пробелы: ")
# new_txt = sorted(txt.replace(' ', '', len(txt)).lower())
# res_txt = {}

for key in new_txt:
    if key in res_txt:
        continue
    else:
        res_txt[key] = new_txt.count(key)

print(res_txt)


    # res_dict[key].append(value)