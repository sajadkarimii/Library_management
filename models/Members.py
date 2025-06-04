from abc import ABC
from dbconn import DB

class Person(ABC):
    def __init__(self, N_Id, FullName, Phone):
        self.N_Id = N_Id
        self.FullName = FullName
        self.Phone = Phone


class Member(Person):
    def __init__(self, N_Id, FullName, Phone, join_date):
        super().__init__(N_Id, FullName, Phone)
        self.join_date = join_date

    def add_member(self):
        with DB() as db:
            db.cursor.execute("INSERT INTO Members(N_Id,FullName,PNumber,Join_Date) VALUES (?,?,?,?)",(self.N_Id,self.FullName,self.Phone,self.join_date,))
            db.conn.commit()

    def delete_member(self):
        with DB() as db:
            db.cursor.execute("DELETE FROM Members WHERE N_Id = ?", (self.N_Id,))
            db.conn.commit()

    @staticmethod
    def show_members():
        with DB() as db:
            db.cursor.execute("SELECT * FROM Members")
            return db.cursor.fetchall()

    def update_member(self):
        with DB() as db:
            db.cursor.execute("UPDATE Members SET FullName = ? , PNumber = ? , Join_Date = ? WHERE N_Id = ?",(self.FullName,self.Phone,self.join_date,self.N_Id,))
            db.conn.commit()

    def search_member(self):
        with DB() as db:
            db.cursor.execute("SELECT * FROM Members WHERE FullName LIKE ?", (f"%{self.FullName}%",))
            return db.cursor.fetchall()