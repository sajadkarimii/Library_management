import sqlite3
import os
import time

# Connect to sqlite3
conn = sqlite3.connect("library_mange.db")
cursor = conn.cursor()

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
                os.system('cls' if os.name == 'nt' else 'clear')
                pass
            case "4":
                break

if __name__ == "__main__":
    main()
