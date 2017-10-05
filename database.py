import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("uploaded.db")
        self.cursor = self.connection.cursor()
        self.check_table_existence()

    def check_table_existence(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Added (PKId INTEGER PRIMARY KEY AUTOINCREMENT, NameOfSerial VARCHAR(50) NOT NULL, UploadedDate VARCHAR(50) NOT NULL)")

    def is_uploaded(self, name, date):
        result = self.cursor.execute(
            "SELECT * FROM Added WHERE NameOfSerial = '%s' AND UploadedDate = '%s'" % (name, date))
        return result.fetchone() is not None

    def add_uploaded(self, name, date):
        self.cursor.execute("INSERT INTO Added (NameOfSerial, UploadedDate) VALUES ('%s','%s')" % (name, date))

    def close(self):
        self.connection.commit()
        self.connection.close()

    def commit(self):
        self.connection.commit()
