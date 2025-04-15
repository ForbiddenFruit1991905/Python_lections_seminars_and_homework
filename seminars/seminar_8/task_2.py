# Задание №2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя,
# личный идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключом для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.
import json

def load_users():
    try:
        with open('user_access.json', encoding='utf-8') as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return {}  # возврат пустого словаря при первом запуске

def sort_dict(my_dict):
    my_dict = sorted(my_dict.items())
    my_dict = {key: value for key, value in my_dict}
    return my_dict

def access_rights():
    flag = True
    while flag:
        user_name = input("Введите имя: ")
        list_id = open('text_id.txt', 'r', encoding='utf-8').read().split()
        print(f'Это список всех идентификаторов пользователей: {list_id}')
        user_id = input('Введите идентификатор: ')
        if user_id in list_id:
            print('Пользователь с таким id уже существует')
        else:
            access_level = int(input('Введите уровень доступа от 1 до 7: '))
            if 0 < access_level < 8:
                groups = load_users()
                groups[f'Пользователь с уровнем доступа {access_level}: '] = groups.setdefault(
                    f'Пользователь с уровнем доступа {access_level}: ', []) + [{user_id: user_name}]
                groups = sort_dict(groups)
                with open('user_access.json', 'w', encoding='utf-8') as file:
                    json.dump(groups, file, ensure_ascii=False)
                    print(groups)
                with open('text_id.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{user_id}')
            elif access_level == 0:
                flag = False
            else:
                print('Введен некорректный код доступа')

access_rights()