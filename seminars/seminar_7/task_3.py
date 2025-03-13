# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    # ✔ если результат умножения отрицательный, сохраните имя записанное
    # строчными буквами и произведение по модулю
    # ✔ если результат умножения положительный, сохраните имя прописными
    # буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в
# более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

# def func_res_file():
#     with (open('example_1.txt', 'r', encoding='utf-8') as f_1,
#           open('example_2.txt', 'r', encoding='utf-8') as f_2,
#           open('example_3.txt', 'a', encoding='utf-8') as new_filename):
#         for line_f_1 in f_1:
#             list_line = list(line_f_1.split())
#             res = float(list_line[0]) * float(list_line[2])
#             formatted_res = "{:.2f}".format(res)
#             new_filename.write(formatted_res + '\n')
#         for line_f_2 in f_2:
#             line_final = f"{formatted_res} | {line_f_2}\n"
#             new_filename.write(line_final)
#
# func_res_file()

def func_res_file():
    with (open('example_1.txt', 'r', encoding='utf-8') as f_1,
          open('example_2.txt', 'r', encoding='utf-8') as f_2,
          open('example_3.txt', 'a', encoding='utf-8') as new_filename):

        results = []

        # total_lines_f1 = sum(1 for _ in f_1)
        # total_lines_f2 = sum(1 for _ in f_2)
        # max_lines = max(total_lines_f1, total_lines_f2)
        #
        # for _ in range(max_lines):
        #     line_f_1 = f_1.readline().strip()
        #     line_f_2 = f_2.readline().strip()
        #
        #     if not line_f_1:
        #         f_1.seek(0)
        #         f_1.readline().strip()
        #
        #     if not line_f_2:
        #         f_2.seek(0)
        #         f_2.readline().strip()

        for line_f_1, line_f_2 in zip(f_1, f_2):

            list_line_num = list(line_f_1.split())
            res = float(list_line_num[0]) * float(list_line_num[2])
            formatted_res = "{:.2f}".format(res)
            results.append(formatted_res)

            name = line_f_2.split()[0]
            result_num = abs(res) if res < 0 else round(abs(res))
            if res < 0:
                name = name.lower()
            else:
                name = name.upper()
            new_line = f"{name} | {result_num}\n"
            new_filename.write(new_line)

func_res_file()

# a = "496 | -222.60926711703917"
# b = list(a.split())
# print(b)
# for i in b:
#     res = float(b[0]) * float(b[2])
# print(res)
