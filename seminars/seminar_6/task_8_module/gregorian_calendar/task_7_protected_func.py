# 📌 Проверку года на високосность вынести в отдельную защищённую функцию.

from task_7 import func_date

def _func_check_year(data: list[str]):
    if not func_date(data):
        print("Дата не соответствует Григорианскому календарю.")
        # return False
    year = int(data[2])
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Год високосный")
        return True
    else:
        print("Год не является високосным")
        return False
txt = input("Введите дату в формате ДД.ММ.ГГГГ: ").split('.')
print(_func_check_year(txt))