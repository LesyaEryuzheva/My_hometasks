'''Калькулятор 1 простой'''

def start():

    while True:
        try:
            x = float(input('Введи число: '))
            s = str(input("Введи знак операции: "))
            y = float(input('Введи число: '))

            if s == '+':
                print(f'{x} {s} {y} = {x + y}')
            elif s == '-':
                print(f'{x} {s} {y} = {x - y}')
            elif s == '*':
                print(f'{x} {s} {y} = {x * y}')
            elif s == '/':
                print(f'{x} {s} {y} = {x / y}')
            else:
                if not s in ('+', '-', '*', '/'):
                    print("Неверный знак операции!")

        except ValueError:
            print('Ты не ввел число')

        except ZeroDivisionError:
            print('На 0 делить нельзя')


start()



'''Калькулятор 2 с классами'''

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y


class Menu:
    def show_result_1():

        while True:
            choice = str(input("Выбери действие (+, -, *, /): "))
            if choice in '+-*/' and len(choice) == 1:
                break
            else:
                print('Выбери знак из предложенных вариантов.')

        try:
            if choice == '+':
                print('Результат: ', num.addition())
            elif choice == '-':
                print('Результат: ', num.subtraction())
            elif choice == '*':
                print('Результат: ', num.multiplication())
            elif choice == '/':
                print('Результат: ', num.division())

        except ZeroDivisionError:
                print("Ты пытаешься поделить на 0?")

while True:
    try:
        x = float(input('Введи число: '))
        y = float(input('Введи число: '))

        num = Calculator(x, y)

    except ValueError:
        print("Ну разве это число?")
    else:
        break

Menu.show_result_1()


