# Задание №2.
# Создайте в переменной data список значений разных
# типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
from unicodedata import digit

data = [1, 1, 5, 5.3, 'cat', '135']
list = []
for i, elem in enumerate(data, start=1):
    print(i, elem, id(elem), elem.__sizeof__(), hash(elem))
    if isinstance(elem, int):
        print('Целое число', elem)
        list.append(str(elem))
        print(list)
    elif isinstance(elem, str) and elem.isalpha():
        print('Все символы буквенные: ', elem)
        list.clear()
        list.append(elem)
        print(list)

