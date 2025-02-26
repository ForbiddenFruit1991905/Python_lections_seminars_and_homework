my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(list(res))
print(type(res), res)
rev_list = list(reversed(my_list))
print(rev_list)

#  Если нужен новый развёрнутый список, объект итератор
#  стоит обернуть в функцию list. В таком случае мы получим
#  новый развёрнутый список.

# Обычно функция reversed используется в сочетании с циклом for in.
# Такой приём позволяет работать с элементами списка внутри цикла в
# обратном порядке.

for item in reversed(my_list):
    print(item, end=' ')
# # #
my_list = [4, 8, 2, 9, 1, 7, 2]
for item in reversed(my_list):
    print(item, end='.', sep='')
    print()
