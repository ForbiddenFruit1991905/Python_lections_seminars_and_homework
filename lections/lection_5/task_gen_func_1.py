# Рассмотрим создание генератора не в одну строку, а как
# отдельную функцию. Например, нам надо посчитать факториал
# чисел от одного до n. Прежде чем создавать генератор, создадим
# обычную функцию, которая вернёт список чисел.

def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result
print(factorial(10))

for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

# Внутри функции создали переменную для хранения очередного числа
# и результирующий список. Далее в цикле перебираем числа от одного
# до n включительно. Число number умножается на очередное число,
# вычисляется следующий по порядку факториал. Результат помещается в
# список. По завершении цикла возвращаем список ответов.