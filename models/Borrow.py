from dbconn import DB

class Borrowed:
    def __init__(self,Id_Members,Id_Books,Borrowed_Date,Respite,Returned):
        self.Id_Members = Id_Members
        self.Id_Books = Id_Books
        self.Borrowed_Date = Borrowed_Date
        self.Respite = Respite
        self.Returned = Returned

    def __str__(self):
        return f"Member Id : {self.Id_Members} , Book Id : {self.Id_Books} , Date : {self.Borrowed_Date} , Respite : {self.Respite} , Returned : {self.Returned}"

    def add_borrow(self):
        try:
            with DB() as db:
                db.cursor.execute("INSERT INTO Borrowed(Id_Member,Id_Books,Borrowed_Date,Respite,Returned) VALUES (?,?,?,?,?)",(self.Id_Members,self.Id_Books,self.Borrowed_Date,self.Respite,self.Returned,))
                db.conn.commit()
        except:
            pass
    
    def update_borrow(self,Id):
        try:
            with DB() as db:
                db.cursor.execute("UPDATE Borrowed SET Id_Members = ?, Id_Books = ?, Borrowed_Date = ?, Respite = ?, Returned = ? WHERE Borrowed.Id = ?)",(self.Id_Members,self.Id_Books,self.Borrowed_Date,self.Respite,self.Returned,Id,))
                db.conn.commit()
        except:
            pass
    
    @staticmethod
    def show_borrow():
        try:
            with DB() as db:
                db.cursor.execute("SELECT Borrowed.Id,FullName,Book_Name,Borrowed_Date,Respite,Returned FROM Borrowed,Members,Books WHERE Id_Member = Members.Id and Id_Books = Books.Id")
                return db.cursor.fetchall()
        except:
            pass
    
    def delete_borrow(self,Id):
        try:
            with DB() as db:
                db.cursor.execute("DELETE FROM Borrowed WHERE Id= ?",(Id,))
                db.conn.commit()
        except:
            pass
    
    def search_borrow(self):
        try:
            with DB() as db:
                db.cursor.execute("SELECT Borrowed.Id,FullName,Book_Name,Borrowed_Date,Respite,Returned FROM Borrowed,Members,Books WHERE Id_Member = ? and  Id_Member = Members.Id and Id_Books = Books.Id",(self.Id_Members,))
                return db.cursor.fetchall()
        except:
            pass
