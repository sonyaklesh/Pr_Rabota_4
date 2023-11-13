from clsGeography import Geography

# создать объект базы данных
database_geography = Geography()


# логика
# добавление записи
def add_command(name, region, capital, area, population):
    database_geography.insert(name, region, capital, area, population)


# просмотр всех записей
def view_command():
    for row in database_geography.view():
        print(row)


# основная программа в консоли
# добавление записи
for i in range(5):
    add_command(input("Введите название страны: "),
                input("Введите регион: "),
                input("Введите столицу: "),
                float(input("Введите площадь страны в кв.км: ")),
                float(input("Введите количество населения: ")))
# просмотр всех записей
view_command()
