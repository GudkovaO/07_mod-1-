import csv

csv_file = []


# Открываю csv файл
def file_open():
    global csv_file
    with open('new 1.csv', "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print(row)
            csv_file.append(row)
    print('Файл открыт. Записей:', len(csv_file))


# Добавление данных
def insert(vin, gos, mar, mod, god, mosh, probeg, vladel, zena):
    global csv_file
    try:
        csv_file.append({'VIN-номер': vin, 'Гос_номер:': gos, 'Марка': mar, 'Модель: ': mod,
                         'Год_выпуска: ': god, 'Мощн_дв: ': mosh, 'Пробег: ': probeg, 'Кол_вл: ': vladel,
                         'Цена: ': zena})
    except Exception as e:
        return f'Ошибка при добавленнии новой записи {e}'
    return "Данные добавлены."


# Добавление данных
def insert(vin, gos, mar, mod, god, mosh, probeg, vladel, zena):
    global csv_file
    try:
        csv_file.append({'VIN-номер': vin, 'Гос_номер:': gos, 'Марка': mar, 'Модель: ': mod, 'Год_выпуска: ': god,
                         'Мощн_дв.: ': mosh, 'Пробег: ': probeg, 'Кол_вл: ': vladel, 'Цена: ': zena})
    except Exception as e:
        return f'Ошибка при добавленнии новой записи {e}'
    return "Данные добавлены."


# Удалить по VIN-номеру
def drop_by_arg(val, col_name='VIN-номер'):
    global csv_file
    try:
        csv_file = list(filter(lambda x: x[col_name] != val, csv_file))
    except Exception as e:
        return f'Строка со значением {val} поля {col_name} не найдена'
    return (f'Строка со значением "{val}" столбца "{col_name}" удалена.')


# Поиск по марке и модели
def find(val, col_name='Марка'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))

# Поиск по году выпуса
def find(val, col_name='Год_выпуска_авто'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))
# Поиск авто с самым большим пробегом
def find(val, col_name='Авто с самым большим пробегом'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))

    # Поиск по гос номеру
    def find(val, col_name='Гос номер_авто'):
        print(*list(filter(lambda x: x[col_name] == val, csv_file)))
# Сохранение
def save():
    with open('new 1.csv', "w", encoding="utf-8", newline="") as file:
        columns = ['ном', 'фио', 'возраст', 'телефон', 'отдел']
        writer = csv.DictWriter(file, delimiter=";", fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_file)
        print("Данные добавлены!")


# Открыт ли файл или нет
def show_csv():
    if len(csv_file) == 0:
        print(type(csv_file))
    else:
        print('{:<5}{:<25}{:<8}{:<12}{:<15}'.format(
            'ном', 'фио', 'возраст', 'телефон', 'отдел'
        ))
        for el in csv_file:
            print('{:<5}{:<25}{:<8}{:<12}{:<15}'.format(el["ном"],
                                                        el["фио"],
                                                        el["возраст"],
                                                        el["телефон"],
                                                        el['отдел']))
