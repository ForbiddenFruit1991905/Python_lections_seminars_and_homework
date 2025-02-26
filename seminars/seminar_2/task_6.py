# Задание №6.
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

sum = 0
operations_counter = 0
def add_money():
    global sum, operations_counter
    amount = int(input("Внесите сумму для пополнения: "))
    if amount % 50 == 0:
        sum += amount
        operations_counter += 1
        return sum
    else:
        print("Ввели неправильную сумму для пополнения.")

def withdraw_money():
    global sum, operations_counter
    amount = int(input("Введите сумму для снятия: "))
    if amount % 50 == 0 and amount <= sum:
        fee = max(30, min(amount * 0.015, 600))
        sum -= amount + fee
        operations_counter += 1
        return sum
       # return (sum - amount) - (sum - amount) * 0.15

def accruals():
    global sum, operations_counter
    if operations_counter % 3 == 0:
        # accrual = sum * 0.03
        # sum += accrual
        sum *= 1.03
        return sum

def tax_rich():
    global sum
    if sum > 5000000:
        fee = sum * 0.1
        sum -= fee
        return sum

def exit():
    print('Выход из приложения')

def process():
    global sum
    while True:
        event = input("Выберите действие: 1 - внести, 2 - снять, 3 - выход\n")
        match event:
            case '1':
                print("Сумма счета: ", add_money())
            case '2':
                print("Сумма счета: ", withdraw_money())
            case '3':
                exit()
                break
            case _:
                print("Неверная команда!")
        tax_rich()
        accruals()

process()