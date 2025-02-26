# Задание №8.
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
# а значение — кортеж вещей. Ответьте на вопросы:

# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

friends_items = {
    "Дмитрий": ("палатка", "спальный мешок", "фонарик", "еда", "спички"),
    "Виктория": ("спальник", "рюкзак", "палатка", "вода", "нож", "спички"),
    "София": ("рюкзак", "еда", "фонарик", "переноска для воды", "фляга")
}

# common_items = None
#
# for items in friends_items.values():
#     if common_items is None:
#         common_items = set(items)
#     else:
#         common_items = common_items.intersection(items)
#
# print(common_items)

# new_set_1 = set(friends_items.values())

# Найти общие элементы, взятые всеми тремя друзьями
common_items_all = set(friends_items["Дмитрий"]).intersection(*[set(items) for items in friends_items.values()])

# Найти уникальные элементы, принадлежащие только одному другу
unique_items = set.union(*[set(items) for items in friends_items.values()]) - set.intersection(*[set(items) for items in friends_items.values()])

# Найти элементы, присутствующие у всех друзей, кроме одного, и имя друга, у которого этот элемент отсутствует
common_items_except_one = {}
for name, items in friends_items.items():
    other_items = set.union(*[set(val) for key, val in friends_items.items() if key != name])
    common_items_except_one[name] = set(items).intersection(other_items)

print("Вещи, взятые всеми тремя друзьями:", common_items_all)
print("Уникальные вещи, принадлежащие только одному другу:", unique_items)
print("Вещи, присутствующие у всех друзей кроме одного и имя друга, у которого данная вещь отсутствует:")
for name, items in common_items_except_one.items():
    print(name, ":", items)