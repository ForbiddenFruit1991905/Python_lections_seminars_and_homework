from mathematical import base_module as bm
from mathematical.advanced_math import exp

x = bm.div(12,5)
z = exp(2,3)
print(x)
print(z)

# Если импортировать пакет верхнего уровня, для работы с
# функциями необходимо указать всю цепочку через точечную
# нотацию: имя пакета, имя модуля, имя объекта. Для сокращения
# объема кода обычно импортируют нужные модули или объекты
# модуля через точечную нотацию после import.

# В первом случае импортировали модуль base_module под именем
# bm. Во-втором — функцию exp из модуля advanced_math пакета
# mathematical.

# Отдельно стоит упомянуть особенности импорта внутри
# подпакетов. Например, импорт модуля other_module в другой
# модуль того же пакета можно осуществить через относительный
# импорт:

# from .import other_module

# А если модулю надо выйти из своего пакета в пакет верхнего
# уровня, используют вторую точку:

# from ..import other_module

# Или так
# from ..other_package import other_module

# 🔥 Важно! Модуль, который является основным в вашем проекте
# должен использовать только абсолютные имена пакетов и модулей.
# Связано это с тем, что у запускаемого модуля в переменной
# __name__ хранится значение “__main__”, а не имя модуля.