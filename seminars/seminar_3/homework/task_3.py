# Задача 3.
# Проверка палиндрома. Напишите программу, которая принимает
# строку и определяет, является ли она палиндромом
# (читается одинаково с обеих сторон).

def func_palindrome(txt: list[str]):
    odd_chars = set()
    for char in txt.copy():
        if char in odd_chars:
            odd_chars.remove(char)
        else:
            odd_chars.add(char)
    if len(odd_chars) <= 1:
        return True
    return False

msg = input("Введите строку без пробелов: ").lower()
res = func_palindrome(list(msg))
print(res)