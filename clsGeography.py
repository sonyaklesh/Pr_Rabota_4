import sqlite3


# создание класса БД
class Geography:
    # конструктор класса
    def __init__(self):

                # Подключение к БД
                self.con = sqlite3.connect("geography.db")
                # Создание курсора
                self.cur = self.con.cursor()
                # Создание таблицы БД
                self.cur.execute(
                "CREATE TABLE IF NOT EXISTS country "
                "(ID INTEGER PRIMARY KEY,"
                "name TEXT,"
                "region TEXT,"
                "capital TEXT,"
                "area INTEGER,"
                "population INTEGER)"

                )
                # сохранить изменения
                self.con.commit()

    def __del__(self):

                    # отключение от БД
     self.con.close()

    def view(self):

    # просмотр всех записей в таблице БД
     self.cur.execute("SELECT * FROM country")
    # список всех записей из таблицы
     rows = self.cur.fetchall()
     return rows

    def insert(self, name, region, capital, area, population):

     # добавить запись
     self.cur.execute("INSERT INTO country "
                     "VALUES (NULL, ?, ?, ?, ?, ?)",
                     (name, region, capital, area, population,))
     self.con.commit()

    def update(self, id, name, region, capital, area, population):

    # редактирование записи
     self.cur.execute("UPDATE country SET "
                     "name=?, region=?, capital=?, area=?, population=? "
                     "WHERE ID = ?",
                     (name, region, capital,
                      area, population, id,))
     self.con.commit()

    def delete(self, id):

    # удаление записи
     self.cur.execute("DELETE FROM country "
                     "WHERE ID=?", (id,))
     self.con.commit()

    def search(self, name):

        self.cur.execute("SELECT region, capital FROM country "
                         "WHERE name=?", (name,))
        rows = self.cur.fetchall()
        return rows
