from clsGeography import Geography

# создать объект базы данных
database_geography = Geography()


# просмотр всех записей
def view_command():
    for row in database_geography.view():
        print(row)


# поиск по названию страны
def search_command(name):
    if len(database_geography.search(name)) > 0:
        for row in database_geography.search(name):
           print(row)
    else:
      print("Такой страны нет")


# основная программа в консоли
# поиск по названию страны
search_command(input("Название страны? "))
