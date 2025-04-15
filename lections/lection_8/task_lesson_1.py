# Задание
# Перед вами несколько строк кода. Какой объект будет получен после его
# выполнения?

import json

a = 'Hello world!'
b = {key: value for key, value in enumerate(a)}
c = json.dumps(b, indent=3, separators=('; ', '= '))
print(c)

# {
#    "0"= "H";
#    "1"= "e";
#    "2"= "l";
#    "3"= "l";
#    "4"= "o";
#    "5"= " ";
#    "6"= "w";
#    "7"= "o";
#    "8"= "r";
#    "9"= "l";
#    "10"= "d";
#    "11"= "!"
# }