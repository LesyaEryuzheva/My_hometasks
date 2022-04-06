import re

regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
regex_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z!@#$%^&*^]{8,}$')

def check_up(func):
    def wrapper(email, password):

        correct_credential = False
        while not correct_credential:
            correct_credential = True
            if re.fullmatch(regex_email, email):
                pass
            else:
                print("Invalid email")
                correct_credential = False

            if re.fullmatch(regex_password, password):
                pass
            else:
                print("Invalid password")
                correct_credential = False

            if not correct_credential:
                email = input('Enter email:')
                password = input('Enter password:')

        func(email, password)
    return wrapper


def account_login(email, password):
    with open('users.txt', 'r') as users_file:
        creds = f'{email}:{password}\n'
        if creds in users_file:
            print('Welcome! Authorization was successful.')
        else:
            print('Wrong login or password.')
    return True

@check_up
def sign_up(email: str, password: str):
    with open('users.txt', 'a') as users_file:
        creds = f'{email}:{password}\n'
        print('Welcome! Registration was successful.')
        users_file.write(creds)
    return True


def menu():
    while True:
        print('Menu: \n1 - Log in\n2 - Register')

        user_choice = int(input('Enter 1 or 2: '))

        if user_choice == 1:
            email = input('Enter email:')
            password = input('Enter password:')
            account_login (email, password)
            break

        elif user_choice == 2:
            email = input('Enter email:')
            password = input('Enter password:')
            sign_up(email, password)
            break
menu()

