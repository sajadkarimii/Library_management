import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("library_manage.db")
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

