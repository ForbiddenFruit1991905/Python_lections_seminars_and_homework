# Задание №5.
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

# def func_dict(names: list[str], salaries: list[int], awards: list[float]) ->  dict[str, float]:
#     res_dict = {}
#     for name, salary, award in zip(names, salaries, awards):
#         final_sum = salary * award + salary
#         res_dict[name] = final_sum
#     return res_dict
#
# names = ["Иван", "Николай", "Пётр"]
# salaries = [125_000, 96_000, 109_000]
# awards = [0.1, 0.25, 0.13]
# res = func_dict(names, salaries, awards)
# print(res)

def func_dict(names: list[str], salaries: list[int], awards: list[str]) ->  dict[str, float]:
    res_dict = {}
    for name, salary, award in zip(names, salaries, awards):
        award_percent = float(award.replace("%", "")) / 100
        final_sum = salary * award_percent + salary
        res_dict[name] = final_sum
    return res_dict

names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = ["10.0%", "25.0%", "13.0%"]
res = func_dict(names, salaries, awards)
print(res)