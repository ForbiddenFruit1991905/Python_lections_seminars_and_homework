# Задание №4.
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 3, 3, 5, 6, 7, 9, 3]
unique_list = []

for i in my_list:
    if my_list.count(i) > 1:
        my_list.remove(i)
    else:
        unique_list.append(i)
print(unique_list)