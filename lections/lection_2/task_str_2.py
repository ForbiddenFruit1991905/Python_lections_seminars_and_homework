# Ещё один способ записать строки, перечислить их последовательно друг за другом.

text = 'Привет.' 'Как ты, друг?' 'Рад тебя видеть.'
print(text)

# Такой приём работает, но считается плохим стилем. Плюс, а точнее минус, строки
# соединились без пробелов.

very_long_text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab alias animi assumenda at aut ' \ 
                 'commodi, consequatur cumque ea harum, hic id illum ipsam itaque laboriosam magnam minus nam nulla ' \ 
                 'numquam obcaecati officia officiis porro possimus praesentium quaerat temporibus ullam veniam? '

# PEP8 рекомендует не писать более 120 символов в одной строке. Обратный слеш “\” позволяет писать
# продолжение с новой строки. Требования в 120 символов выполняются.А Python воспринимает несколько строк как одну.