from clsGeography import Geography

# создать объект базы данных
database_geography = Geography()


# удаление по id страны
def delete_command(id):
    database_geography.delete(id)
    print(f"Данные страны с id = {id} удалены")


# просмотр всех записей
def view_command():
    for row in database_geography.view():
        print(row)


# основная программа
print("Список стран")
view_command()

id_delete = int(input("Введите id страны "))
delete_command(id_delete)

print("Список стран")
view_command()
