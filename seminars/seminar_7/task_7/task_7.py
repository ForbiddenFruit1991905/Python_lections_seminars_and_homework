# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import random

def func_sort_by_folders(file_dir):
    os.chdir(file_dir)

    for i in range(1, 4):
        file_ext_audio = ['.MP3', '.WMA', '.WAV']
        random_file_extension = random.choice(file_ext_audio)
        filename_audio = f"{i}_audio{random_file_extension}"
        with open(os.path.join("audio_dir", filename_audio), 'w') as file:
            file.write("# some code")
    for i in range(1, 4):
        file_ext_docs = ['.doc', '.txt', '.exe']
        random_file_extension = random.choice(file_ext_docs)
        filename_doc = f"{i}_docs{random_file_extension}"
        with open(os.path.join("docs_dir", filename_doc), 'w') as file:
            file.write("# some code")
    for i in range(1, 4):
        file_ext_video = ['.MP4', '.WebM', '.AVI']
        random_file_extension = random.choice(file_ext_video)
        filename_video = f"{i}_video{random_file_extension}"
        with open(os.path.join("video_dir", filename_video), 'w') as file:
            file.write("# some code")

current_dir = os.path.dirname(os.path.realpath(__file__))
func_sort_by_folders(current_dir)