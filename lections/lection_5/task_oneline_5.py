# Если нам нужна часть данных в переменных, а упакованный
# список в дальнейших расчётах не участвует, в качестве
# переменной используют подчеркивание.

link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-op tional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')
print(prefix, *_, suffix)