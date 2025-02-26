# Метод join принимает на вход итерируемую последовательность и
# соединяет все её элементы в строку, разделяя каждый текстом,
# к которому применён метод. В некоторой степени join противоположен
# split.

data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1', 'posts']
url = '/'.join(data)
print(url)

rev = list(reversed(url))
print(url, rev, sep='\n')