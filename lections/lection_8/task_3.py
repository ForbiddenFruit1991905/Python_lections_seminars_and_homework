# А теперь представим, что мы подготовили информацию в виде
# многострочного str в python и хотим превратить его из JSON строки в
# объекты Python.

import json
json_text = """ 
[ 
    { 
        "userId": 1,
        "id": 9, 
            "title": "nesciunt iure omnis dolorem tempora et accusantium", 
        "body": "consectetur animi nesciunt iure dolore" 
    }, 
    { 
        "userId": 1, 
        "id": 10, 
        "title": "optio molestias id quia eum", 
        "body": "quo et expedita modi cum officia vel magni" 
    }, 
    { 
        "userId": 2, 
        "id": 11, 
        "title": "et ea vero quia laudantium autem", 
        "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus" 
    }, 
    { 
        "userId": 2, 
        "id": 12, 
        "title": "in quibusdam tempore odit est dolorem", 
        "body": "praesentium quia et ea odit et ea voluptas et" 
    }
]"""

print(f'{type(json_text) = }\n{json_text = }')
json_list = json.loads(json_text)
print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')

# Функция loads принимает на вход строку, хранящуюся как структуру JSON
# и преобразует её к нужным типам. В нашем примере получили список list
# с четырьмя словарями внутри.

# Запомнить различия между функциями просто. Окончание s у loads намекает
# на строку. А load требует объект с методом read для чтения информации.
# Напомним, что файловый дескриптор имеет метод read для чтения информации
# из файла.

# 🔥 Важно! При открытии файлов важно учитывать их размер. Огромные JSON
# объекты дают высокую нагрузку на процессор и оперативную память.

# ● Преобразование Python в JSON
# Что делать, если мы хотим превратить Словарь Python в JSON объект? Для
# этого используем функции сериализации dump и dumps. Смысл окончания s у
# dumps такой же, как и у loads.

import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}

print(f'{type(my_dict) = }\n{my_dict = }')
with open('new_user.json', 'w') as f:
    json.dump(my_dict, f)

# Символы отличные от ASCII были заменены на специальные коды
# в файле new_user.json.
# Проведём десериализацию уже знакомым способом и проверим
# целостность данных.

import json
with open('new_user.json', 'r', encoding='utf-8') as f:
    new_dict = json.load(f)
print(f'{new_dict = }')

# Если же мы хотим отказаться от символов экранирования в JSON файле,
# следует установить дополнительный параметр ensure_ascii в значение ложь.

with open('new_user.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)

# Воспользуемся словарём my_dict ещё раз для проверки функции dumps:

dict_to_json_text = json.dumps(my_dict)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

# На выходе получаем объект типа str хранящий структуру json.

# ● Дополнительные параметры dump и dumps
# Функции для сериализации объектов в JSON поддерживают несколько
# дополнительных параметров. Они позволяют сделать полученные объекты
# более удобочитаемыми для пользователя. Разберём на примере функции
# dumps. Но стоит помнить, что функция dump обладает такими же параметрами
# с тем же смыслом.

import json

my_dict = {
    "id": 123,
    "name": "Clementine Bauche",
    "username": "Cleba",
    "email": "cleba@corp.mail.ru",
    "address": {
        "street": "Central",
        "city": "Metropolis",
        "zipcode": "123456"
    },
    "phone": "+7-999-123-45-67"
}

res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)
print(res)

# ➢ Параметр indent отвечает за форматирование с отступами. Теперь JSON
# выводится не в одну строку, а в несколько. Читать стало удобнее, но
# размер увеличился.
# ➢ Параметр separators принимает на вход кортеж из двух строковых
# элементов. Первый — символ разделитель элементов. По умолчанию это
# запятая и пробел. Второй — разделитель ключа и значения. По умолчанию
# это двоеточие и пробел. Передав запятую и двоеточие без пробела JSON
# стал компактнее.
# ➢ Параметр sort_keys отвечает за сортировку ключей по алфавиту. Нужна
# сортировка или нет, решать только вам.