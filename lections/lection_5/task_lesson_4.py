# Задание.
# Перед вами несколько строк кода. Напишите что по вашему мнению
# выведет print, не запуская код.
from typing import Any, Generator


def gen(a: int, b: int) -> Generator[str, Any, None]:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)

for item in gen(10, 1):
    print(f'{item = }')

# item = 1...10