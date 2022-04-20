import re

import json

class Correct:
    def __init__(self, email: str, password: str):
        Correct.validate_credentials(email, password)
        self.email = email
        self.password = password

    @staticmethod
    def validate_credentials(email, password):
        regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        regex_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z!@#$%^&*^]{8,}$')
        correct_creds = True

        if not re.fullmatch(regex_email, email):
            print("Invalid email")
            correct_creds = False

        if not re.fullmatch(regex_password, password):
            print("Invalid password")
            correct_creds = False

        return correct_creds


class Account:
    @staticmethod
    def authoriz(email: str, password: str):
        creds_dict = Account.read_json('users.json')
        creds = (email, password)
        if creds in creds_dict.items():
            print('Welcome! Authorization was successful.')
        else:
            print('Wrong login or password.')

    @staticmethod
    def sign_up(email: str, password: str):
        creds_dict = Account.read_json('users.json')
        creds_dict[email] = password
        Account.write_json('users.json', creds_dict)

        print('Welcome! Registration was successful.')
        return True

    @staticmethod
    def read_json(file_path):
        with open(file_path) as file:
            creds_dict = json.load(file)
        return creds_dict

    @staticmethod
    def write_json(file_path, creds_dict):
        with open(file_path, 'w') as file:
            json.dump(creds_dict, file)


class Menu:
    def __init__(self, choice):
        self.choice = choice

    @staticmethod
    def show_menu():
        print('Menu: \n1 - Log in\n2 - Enter')

    @staticmethod
    def option():
        return int(input('Enter 1 or 2: '))

    @staticmethod
    def ask_choice():
        email = input('Enter email:')
        password = input('Enter password:')
        return (email, password)

    def us_choice(self):
        if self.choice != 1 and self.choice != 2:
            print('No such option')
        else:
            email, password = self.ask_choice()
            while not Correct.validate_credentials(email, password):
                email, password = self.ask_choice()

            if self.choice == 1:
                Account.sign_up(email, password)
            elif self.choice == 2:
                Account.authoriz(email, password)


Menu.show_menu()
us_ch = Menu.option()
m = Menu(us_ch)
m.us_choice()
