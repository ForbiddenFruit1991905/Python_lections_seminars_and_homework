# buffering — определяет режим буферизации. При работе
# с бинарными файлами можно передать 0 — отключить буферизацию.
# В текстовом режиме можно передать 1 — использовать буферизацию
# строк. Число больше единицы определяет размер буфера в байтах
# для двоичных файлов. По умолчанию размер буфера подстраивается
# под файловую систему и обычно равен 4096 или 8192 байта.

f = open('bin_data', 'wb', buffering=64)
f.write(b'X' * 1200)
f.close()