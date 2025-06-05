from dbconn import DB

class Book:
    def __init__(self, Book_Name, Publisher, Author, Genre, Quantity):
        self.Book_Name = Book_Name
        self.Publisher = Publisher
        self.Author = Author
        self.Genre = Genre
        self.Quantity = Quantity

    def __str__(self):
        return f"Book name : {self.Book_Name} , Publisher : {self.Publisher} , Author : {self.Author} , Genre : {self.Genre} , Quantity : {self.Quantity}"

    def add_book(self):
        try:
            with DB() as db:
                db.cursor.execute("INSERT INTO Books(Book_Name,Publisher,Author,Genre,Quantity) VALUES (?,?,?,?,?)",(self.Book_Name,self.Publisher,self.Author,self.Genre,self.Quantity,))
                db.conn.commit()
        except:
            pass

    def delete_book(self):
        try:
            with DB() as db:
                db.cursor.execute("DELETE FROM Books WHERE Book_Name = ?",(self.Book_Name,))
                db.conn.commit()
        except:
            pass

    @staticmethod
    def show_book():
        try:
            with DB() as db:
                db.cursor.execute("SELECT * FROM Books")
                return db.cursor.fetchall()
        except:
            pass

    def update_book(self, book_name):
        try:
            with DB() as db:
                db.cursor.execute("UPDATE Books SET Book_Name = ?, Publisher = ? , Author = ? , Genre = ? , Quantity = ? WHERE Book_Name = ?"(self.Book_Name,self.Publisher,self.Author,self.Genre,self.Quantity,book_name,))
                db.conn.commit()
        except:
            pass

    def search_book(self):
        try:
            with DB() as db:
                db.cursor.execute("SELECT * FROM Books WHERE Book_Name LIKE ?", (f"%{self.Book_Name}%",))
                return db.cursor.fetchall()
        except:
            pass


class MathBook(Book):
    def __init__(self, Book_Name, Publisher, Author, Quantity):
        super().__init__(Book_Name, Publisher, Author, "Math", Quantity)


class NovelBook(Book):
    def __init__(self, Book_Name, Publisher, Author, Quantity):
        super().__init__(Book_Name, Publisher, Author, "Novel", Quantity)


class RomanticBook(Book):
    def __init__(self, Book_Name, Publisher, Author, Quantity):
        super().__init__(Book_Name, Publisher, Author, "Romantic", Quantity)


class ScientificBook(Book):
    def __init__(self, Book_Name, Publisher, Author, Quantity):
        super().__init__(Book_Name, Publisher, Author, "Scientific", Quantity)


class ExperimentalBook(Book):
    def __init__(self, Book_Name, Publisher, Author, Quantity):
        super().__init__(Book_Name, Publisher, Author, "Experimental", Quantity)