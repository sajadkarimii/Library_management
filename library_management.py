import sqlite3
import os
import time

# Connect to sqlite3
conn = sqlite3.connect("library_mange.db")
cursor = conn.cursor()

class Librarian:
    def __init__(self,FullName='sajad karimi',UserName='sajad',Password='2233123'):
        self.FullName = FullName
        self.UserName = UserName
        self.Password = Password

    def login(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        username = input("Enter username :")
        password = input("Enter password :")
        if (username == self.UserName and password == self.Password):
            return True
        else:
            if (self.login()):
                return True

class Borrowed:
    def __init__(self,Id_Members,Id_Books,Borrowed_Date,Respite,Returned):
        self.Id_Members = Id_Members
        self.Id_Books = Id_Books
        self.Borrowed_Date = Borrowed_Date
        self.Respite = Respite
        self.Returned = Returned

    def add_borrow(self):
        cursor.execute(f"INSERT INTO Borrowed(Id_Member,Id_Books,Borrowed_Date,Respite,Returned) VALUES ({self.Id_Members},{self.Id_Books},'{self.Borrowed_Date}',{self.Respite},'{self.Returned}')")
        conn.commit()
    
    def update_borrow(self,Id):
        cursor.execute(f"UPDATE Borrowed SET Id_Members = {self.Id_Members}, Id_Books = {self.Id_Books}, Borrowed_Date = '{self.Borrowed_Date}', Respite = {self.Respite}, Returned = '{self.Returned}')")
        conn.commit()
    
    def show_borrow(self):
        cursor.execute(f"SELECT Borrowed.Id,FullName,Book_Name,Borrowed_Date,Respite,Returned FROM Borrowed,Members,Books WHERE Id_Member = Members.Id and Id_Books = Books.Id")
        for row in cursor.fetchall():
            print(row)
    
    def delete_borrow(self,Id):
        cursor.execute(f"DELETE FROM Borrowed WHERE Id={Id}")
        conn.commit()
    
    def search_borrow(self):
        cursor.execute(f"SELECT Borrowed.Id,FullName,Book_Name,Borrowed_Date,Respite,Returned FROM Borrowed,Members,Books WHERE Id_Member = {self.Id_Members} and  Id_Member = Members.Id and Id_Books = Books.Id")
        for row in cursor.fetchall():
            print(row)

class Book:
    def __init__(self,Book_Name,Publisher,Author,Genre,Quantity):
        self.Book_Name = Book_Name
        self.Publisher = Publisher
        self.Author = Author
        self.Genre = Genre
        self.Quantity = Quantity
    
    def add_book(self):
        cursor.execute(f"INSERT INTO Books(Book_Name,Publisher,Author,Genre,Quantity) VALUES ('{self.Book_Name}','{self.Publisher}','{self.Author}','{self.Genre}',{self.Quantity})")
        conn.commit()

    def delete_book(self):
        cursor.execute(f"DELETE FROM Books WHERE Book_Name = '{self.Book_Name}'")
        conn.commit()
    
    def show_book(self):
        cursor.execute(f"SELECT * FROM Books")
        for row in cursor.fetchall():
            print(row)
    
    def update_book(self,book_name):
        cursor.execute(f"UPDATE Books SET Book_Name = '{self.Book_Name}' , Publisher = '{self.Publisher}' , Author = '{self.Author}' , Genre = '{self.Genre}' , Quantity = {self.Quantity} WHERE Book_Name = '{book_name}'  ")
        conn.commit()

    def search_book(self):
        cursor.execute(f"SELECT * FROM Books WHERE Book_Name LIKE ?", (f"%{self.Book_Name}%",))
        for row in cursor.fetchall():
            print(row)
    

class Person:
    def __init__(self, N_Id , FullName, Phone):
        self.N_Id = N_Id
        self.FullName = FullName
        self.Phone = Phone


class Member(Person):
    def __init__(self, N_Id , FullName, Phone,  join_date):
        super().__init__(N_Id , FullName, Phone)
        self.join_date = join_date

    def add_member(self):
        cursor.execute(f"INSERT INTO Members(N_Id,FullName,PNumber,Join_Date) VALUES ('{self.N_Id}','{self.FullName}','{self.Phone}','{self.join_date}')")
        conn.commit()

    def delete_member(self):
        cursor.execute(f"DELETE FROM Members WHERE N_Id = '{self.N_Id}'")
        conn.commit()
    
    def show_members(self):
        cursor.execute(f"SELECT * FROM Members")
        for row in cursor.fetchall():
            print(row)

    def update_member(self):
        cursor.execute(f"UPDATE Members SET FullName = '{self.FullName}' , PNumber = '{self.Phone}' , Join_Date = '{self.join_date}' WHERE N_Id = '{self.N_Id}'")
        conn.commit()

    def search_member(self):
        cursor.execute(f"SELECT * FROM Members WHERE FullName LIKE ?", (f"%{self.FullName}%",))
        for row in cursor.fetchall():
            print(row)
        

def main():
    login = Librarian()
    if login.login():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1: Books mangement\n2: Members management\n3: Borrowed management\n4: Exit")
            x = input("Choose an option : ")
            match x:
                case "1":
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("1: Add book\n2: Update book\n3: Show books\n4: Delete book\n5: Search book\n6: main page")
                        x = input("Choose an option : ")
                        if (x == '1'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            bookname = input("Enter Book Name: ")
                            publisher = input("Enter Publisher: ")
                            author = input("Enter Author Name: ")
                            genre = input("Enter Genre: ")
                            quantity = int(input("Enter Quantity: "))
                            new_book = Book(bookname,publisher,author,genre,quantity)
                            new_book.add_book()
                        elif (x == '2'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            bookname = input("Enter Book Name you want to edit : ")
                            bookname1 = input("Enter edited Book Name: ")
                            publisher = input("Enter edited Publisher: ")
                            author = input("Enter edited Author Name: ")
                            genre = input("Enter edited Genre: ")
                            quantity = input("Enter edited Quantity: ")
                            new_book = Book(bookname1,publisher,author,genre,quantity)
                            new_book.update_book(bookname)
                        elif (x == '3'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            new_book = Book('','','','','')
                            new_book.show_book()
                            time.sleep(5)
                        elif (x == '4'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            bookname = input("Enter book name to delete: ")
                            new_book = Book(bookname,'','','','')
                            new_book.delete_book()
                        elif (x == '5'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            bookname = input("Enter book name to search : ")
                            new_book = Book(bookname,'','','','')
                            new_book.search_book()
                            time.sleep(5)
                        elif(x == '6'):
                            break
                case "2":
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("1: Add member\n2: Update member\n3: Show members\n4: Delete member\n5: Search member \n6: Main page")
                        x = input("Choose an option : ")
                        if (x == '1'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            n_id = input("Enter member's National number : ")
                            name = input("Enter member's full name : ")
                            pnumber = input("Enter member's phone nubmer : ")
                            jdate = input("Enter join date(yyyy-mm-dd) : ")
                            new_member = Member(n_id,name,pnumber,jdate)
                            new_member.add_member()
                        elif (x == '2'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            n_id = input("Enter member's National number : ")
                            name = input("Enter edited member's full name : ")
                            pnumber = input("Enter edited member's phone nubmer : ")
                            jdate = input("Enter edited join date(yyyy-mm-dd) : ")
                            new_member = Member(n_id,name,pnumber,jdate)
                            new_member.update_member()
                        elif (x == '3'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            new_member = Member('','','','')
                            new_member.show_members()
                            time.sleep(5)
                        elif (x == '4'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            n_id = input("Enter member's National number : ")
                            new_member = Member(n_id,'','','')
                            new_member.delete_member()
                        elif (x == '5'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            fullname = input("Enter member's FullName : ")
                            new_member = Member('',fullname,'','')
                            new_member.search_member()
                            time.sleep(5)
                        elif(x == '6'):
                            break
                case "3":
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("1: Add Borrow\n2: Update Borrow\n3: Show Borrow\n4: Delete Borrow\n5: Search Borrow \n6: Main page")
                        x = input("Choose an option : ")
                        if (x == '1'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            member_id = int(input("Enter member's id : "))
                            book_id = int(input("Enter book's id : "))
                            borrowdate = input("Enter borrow date(yyyy-mm-dd) : ")
                            respite = int(input("Enter respite : "))
                            returned = input("Enter returned date : ")
                            new_Borrow = Borrowed(member_id,book_id,borrowdate,respite,returned)
                            new_Borrow.add_borrow()
                        elif (x == '2'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            id = int(input("Enter borrow id : "))
                            member_id = int(input("Enter member's id : "))
                            book_id = int(input("Enter book's id : "))
                            borrowdate = input("Enter borrow date(yyyy-mm-dd) : ")
                            respite = int(input("Enter respite : "))
                            returned = input("Enter returned date : ")
                            new_Borrow = Borrowed(member_id,book_id,borrowdate,respite,returned)
                            new_Borrow.update_borrow(id)
                        elif (x == '3'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            new_Borrow = Borrowed('','','','','')
                            new_Borrow.show_borrow()
                            time.sleep(5)
                        elif (x == '4'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            id = int(input("Enter borrow id you want to delete: "))
                            new_Borrow = Borrowed('','','','','')
                            new_Borrow.delete_borrow(id)
                        elif (x == '5'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            member_id = int(input("Enter member's id : "))
                            new_Borrow = Borrowed(member_id,'','','','')
                            new_Borrow.search_borrow()
                            time.sleep(5)
                        elif(x == '6'):
                            break
                case "4":
                    break

if __name__ == "__main__":
    main()
