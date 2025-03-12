import os

def create_py_files(prefix="task_", num_files=7):
    current_dir = os.path.dirname(os.path.realpath(__file__))

    for i in range(1, num_files + 1):
        filename = f"{prefix}{i}.py"
        with open(os.path.join(current_dir, filename), 'w') as file:
            file.write("# some code")

    print(f"{num_files} файлов было успешно создано в каталоге {current_dir}.")

create_py_files()