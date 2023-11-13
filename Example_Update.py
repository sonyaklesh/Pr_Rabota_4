from clsGeography import Geography

# создать объект базы данных
database_geography = Geography()


# обновление по id страны
def update_command(id,  name, region, capital, area, population):
    database_geography.update(id,  name, region, capital, area, population)
    print(f"Данные страны с id = {id} обновлены")


# просмотр всех записей
def view_command():
    for row in database_geography.view():
        print(row)


# основная программа
print("Список стран")
view_command()
id_update = int(input("Введите id страны "))
print("Укажите новые данные: ")
name = input("Название страны")
region = input("Название региона")
capital = input("Название столицы")
area = float(input("Площадь страны в кв.км"))
population = float(input("Количество населения"))
update_command(id_update, name, region, capital, area, population)
print("Список стран")
view_command()




















