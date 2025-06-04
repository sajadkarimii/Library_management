from dbconn import DB

class Borrowed:
    def __init__(self,Id_Members,Id_Books,Borrowed_Date,Respite,Returned):
        self.Id_Members = Id_Members
        self.Id_Books = Id_Books
        self.Borrowed_Date = Borrowed_Date
        self.Respite = Respite
        self.Returned = Returned

    def add_borrow(self):
        with DB() as db:
            db.cursor.execute("INSERT INTO Borrowed(Id_Member,Id_Books,Borrowed_Date,Respite,Returned) VALUES (?,?,?,?,?)",(self.Id_Members,self.Id_Books,self.Borrowed_Date,self.Respite,self.Returned,))
            db.conn.commit()
    
    def update_borrow(self,Id):
        with DB() as db:
            db.cursor.execute("UPDATE Borrowed SET Id_Members = ?, Id_Books = ?, Borrowed_Date = ?, Respite = ?, Returned = ?)",(self.Id_Members,self.Id_Books,self.Borrowed_Date,self.Respite,self.Returned,))
            db.conn.commit()
    
    def show_borrow(self):
        with DB() as db:
            db.cursor.execute("SELECT Borrowed.Id,FullName,Book_Name,Borrowed_Date,Respite,Returned FROM Borrowed,Members,Books WHERE Id_Member = Members.Id and Id_Books = Books.Id")
            for row in db.cursor.fetchall():
                print(row)
    
    def delete_borrow(self,Id):
        with DB() as db:
            db.cursor.execute("DELETE FROM Borrowed WHERE Id= ?",(Id,))
            db.conn.commit()
    
    def search_borrow(self):
        with DB() as db:
            db.cursor.execute("SELECT Borrowed.Id,FullName,Book_Name,Borrowed_Date,Respite,Returned FROM Borrowed,Members,Books WHERE Id_Member = ? and  Id_Member = Members.Id and Id_Books = Books.Id",(self.Id_Members,))
            for row in db.cursor.fetchall():
                print(row)
