from dbconn import DB

class Book:
    def __init__(self, Book_Name, Publisher, Author, Genre, Quantity):
        self.Book_Name = Book_Name
        self.Publisher = Publisher
        self.Author = Author
        self.Genre = Genre
        self.Quantity = Quantity

    def add_book(self):
        with DB() as db:
            db.cursor.execute("INSERT INTO Books(Book_Name,Publisher,Author,Genre,Quantity) VALUES (?,?,?,?,?)",(self.Book_Name,self.Publisher,self.Author,self.Genre,self.Quantity,))
            db.conn.commit()

    def delete_book(self):
        with DB() as db:
            db.cursor.execute("DELETE FROM Books WHERE Book_Name = ?",(self.Book_Name,))
            db.conn.commit()

    def show_book(self):
        with DB() as db:
            db.cursor.execute("SELECT * FROM Books")
            for row in db.cursor.fetchall():
                print(row)

    def update_book(self, book_name):
        with DB() as db:
            db.cursor.execute("UPDATE Books SET Book_Name = ?, Publisher = ? , Author = ? , Genre = ? , Quantity = ? WHERE Book_Name = ?"(self.Book_Name,self.Publisher,self.Author,self.Genre,self.Quantity,book_name,))
            db.conn.commit()

    def search_book(self):
        with DB() as db:
            db.cursor.execute("SELECT * FROM Books WHERE Book_Name LIKE ?", (f"%{self.Book_Name}%",))
            for row in db.cursor.fetchall():
                print(row)


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