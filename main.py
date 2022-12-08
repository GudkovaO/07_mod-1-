from mod1 import file_open, insert, drop_by_arg, find, save, show_csv
from builtins import print

FILENAME = "new 1.csv"

MENU = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Найти по марке и модели',
    '5': 'Сохранить в файл',
    '6': 'Вывести записи',
    '7': 'Найти авто по году выпуска',
    '8': 'Найти авто по гос номеру',
    '0': '<-Меню',
    'exit': 'Выход'
}

for key, val in MENU.items():
    print(key, '-', val)

while True:
    action = input('>_ ')
    if action == '1':
        file_open()
    elif action == '2':
        print(insert(input('VIN-номер:'), (input('Гос.номер:')), input('Марка: '), input('Модель: '),
                     int(input('Год_выпуска: ')),
                     int(input('Мощн_дв: ')),
                     int(input('Пробег: ')),
                     int(input('Кол_вл: ')), input('Цена: '), ))
    elif action == '3':
        col = input('Колонка: ')
        val = input('Значение: ')
        print(drop_by_arg(val, col_name=col))
    elif action == '4':
        col = input('Введите марку или модель: ')
        val = input('Значение: ')
        find(val, col_name=col)
    elif action == '7':
        col = input('Введите год выпуска авто: ')
        val = input('Значение: ')
        find(val, col_name=col)
     elif action == '8':
        col = input('Введите гос номер авто: ')
        val = input('Значение: ')
        find(val, col_name=col)
    elif action == '5':
        save()

    elif action == '0':
        for key, val in MENU.items():
            print(key, '-', val)
    elif action == '6':
        show_csv()
    elif action == 'exit':
        break
