# 🔥 Важно! Генератор не обязан быть однострочником.
#
# Генераторы похожи на итераторы тем, что возвращают некую
# последовательность значений. Отличие в том, что итераторы
# чаще всего возвращают коллекции. Т.е.коллекция хранит все
# данные и тратит на хранение память. Далее коллекция возвращает
# хранимые элементы через интерфейс итерации. Генераторы не хранят
# данные в памяти, а вычисляют их по мере необходимости, чтобы
# вернуть очередное значение.

# При создании генератора мы указываем диапазон перебираемых
# целых чисел, но не сохраняем их в памяти. Каждое из значений
# генерируется на очередном витке цикла.

a = range(0, 10, 2)
# for i in a:
#     print(i)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')

# Генератор a на пять значений и генератор b на 1 млн. значений
# занимают одинаковое место в памяти.