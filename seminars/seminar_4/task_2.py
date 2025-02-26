# Задание №2.
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def func():
    txt = input("Введите текст: ")
    reversed_list = set(txt)
    print(reversed_list)
    for i in sorted(reversed_list, reverse=True):
        print(ord(i))
func()