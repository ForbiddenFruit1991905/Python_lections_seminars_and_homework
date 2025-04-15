# Задание №3
# 📌 Напишите функцию, которая сохраняет созданный в прошлом задании
# файл в формате CSV.

import json, csv

def convert_file():
    classes_access = []
    users = []
    with open('user_access.json', encoding='utf-8') as f:
        data = json.load(f)
        for key, value in data.items():
            classes_access.append(key)
            users.append(value)
    print(classes_access, users, sep='\n')

    with open('users_access.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=' ')
        for i in range(len(classes_access)):
            writer.writerow(''.join(classes_access[i]).split())
            writer.writerow(users[i])

convert_file()