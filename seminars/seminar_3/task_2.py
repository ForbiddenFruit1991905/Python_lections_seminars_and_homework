# Задание №2.
# Пользователь вводит данные. Сделайте проверку данных и
# преобразуйте, если возможно в один из вариантов ниже:
# ✔Целое положительное число
# ✔Вещественное положительное или отрицательное число
# ✔Строку в нижнем регистре, если в строке есть хотя бы одна
# заглавная буква
# ✔Строку в нижнем регистре в остальных случаях

data = input('Введите данные: ')

if data.isdigit():
    print(f'int: {int(data)}')

elif any(letter.isupper() for letter in data):
    print(f'txt with capital letters: {data.lower()}')

elif data.replace('.', '', 1).isdigit():
    print(f'float: {data}')

elif float(data) < 0:
    print(f'float negative: {data}')

else:
    print(f'txt: {data.lower()}')