name = 'Vika'
age = None
a = 42
print(id(a))
a = "Hello world"
print(id(a))
a = 3.14 / 3
print(id(a))

print(name, age, a, 456, 'text', sep=' (=^.^=) ', end='\n')
print('any text')

print(name, age, a, 456, 'text', sep=' (=^.^=) ', end='#')
print('any text')

res = input('Print your text: ')
print('Your message: ', res)

ADULT = 18
age = int(input('Сколько тебе лет? '))
how_old = ADULT - age
print(how_old, 'год(а) осталось до совершеннолетия')