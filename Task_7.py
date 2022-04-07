import json

import csv

import openpyxl

with open('users.json', 'w') as file:
    login = input('Enter login:')
    password = input('Enter password:')
    creds = str(f'{login}:{password}')
    json.dump(creds, file)

with open('person.csv', 'w') as person_file:
    login = input('Enter login:')
    password = input('Enter password:')
    credentials = f'{login}:{password}'
    writer = csv.writer(person_file)
    writer.writerow([credentials])

login = input('Enter login:')
password = input('Enter password:')
book = openpyxl.Workbook()
sheet = book.active
sheet['A1'] = login
sheet['B1'] = password
book.save('my_book.xlsx')
book.close()
