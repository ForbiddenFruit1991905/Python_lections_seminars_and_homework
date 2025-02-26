# Задание №8.
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def func_change(data: list[str]):
    new_data = []
    for elem in data:
        if "s" in elem and len(elem) > 1:
            new_data.append(elem.replace("s", ''))
        else:
            new_data.append(elem)
    return new_data

my_list = ["apples", "bananas", "kiwi", "tree", "s"]
res = func_change(my_list)
print(res)