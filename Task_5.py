numbers = [i for i in range(3, 103, 10)]
print(numbers)

def get_numbers_list(start: int, finish: int, interval: int) -> list:
    return [i for i in range(start, finish, interval) if i not in [23, 63, 83]]
print(get_numbers_list(3, 103, 10))

from datetime import datetime
def dt_now():
    a = datetime.now().time()
    return str(a)
print([dt_now() for x in range(3)])
