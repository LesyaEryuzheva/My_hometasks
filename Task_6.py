movie = {"< 12": "Незнайка на луне", "> 12": "Титаник"}

def decorator(func):
    '''
    Данная функция позволяет ввести имя не более 10 символов
    и в соотсветсвии с возрастом ограничивает просмотр фильма из словаря movie
    '''
    def wrapper(arg1, arg2):
        if len(arg1) > 10:
            print("Введи имя меньше 10 символов")
            return

        if arg2 < 12:
            print("Посмотри мультик", movie['< 12'])

        if arg2 >= 12:
            print("Тебе можно посмотреть", movie['> 12'])

        func(arg1, arg2)
    return wrapper

print(decorator.__doc__)


@decorator
def print_persone(name, age):
    print(f'Привет {name}, тебе {age} лет')


print_persone("Катя", 12)


print()


def decorator(function):
    def wrapper():
        func = function()
        title = func.upper()
        return title
    return wrapper

@decorator
def greeting():
    return 'приветствие'

print(greeting())

c = list(greeting())
print(c)

test = list(filter(lambda x: x == 'Т', c))
print(test)


