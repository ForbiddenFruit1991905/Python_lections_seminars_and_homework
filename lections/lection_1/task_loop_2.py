num = float(input('Введите число: '))
STEP = 2
limit = num - STEP
count = STEP
while count < limit:
    # print(count)
    count += STEP
    if count % 12 == 0:
        continue
    print(count)