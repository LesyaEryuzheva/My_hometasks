'''Вариант 1'''

def get_progression(x, y):
    s = 1
    for i in range(1, y):
        yield s*x
        s = s*x

a = get_progression(3, 8)

for i in a:
    print(i)


'''Вариант 2'''

def get_progression(num, den, am):
    for i in range(1, am):
        yield num*den
        num = num*den

while True:
    try:
        s = int(input('Введи первое число прогресии: '))
        x = int(input('Введи знаменатель прогрессии: '))
        y = int(input('Введи количество элементов прогресии: '))

        if s == 0 or x == 0 or y == 0:
            print('Нелогично вводить 0')
        else:
            a = get_progression(s, x, y)

            for i in a:
                print(i)

    except ValueError:
        print('Здесь должны быть только цифры')
    else:
        break

