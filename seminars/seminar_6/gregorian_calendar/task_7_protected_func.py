# 📌 Проверку года на високосность вынести в отдельную защищённую функцию.

from task_7 import func_date

def _func_check_year(data: list[str]):
    if func_date(data):
        year = int(data[2])
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
    return False
txt = input("Введите дату в формате ДД.ММ.ГГГГ: ").split('.')
print(_func_check_year(txt))