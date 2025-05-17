import tkinter
import pyodbc

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=SAJAD;'
    r'DATABASE=Library_management;'
    r'UID=sa;'
    r'PWD=s2233943j;'
)

cursor = conn.cursor()


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
        cursor.execute(f"INSERT INTO Members VALUES ('{self.N_Id}','{self.FullName}','{self.Phone}','{self.join_date}')")
        conn.commit()


def main():
    while True:
        print("""1: Show books
2: Add book
3: Delete book
4: Add member
5: Exit""")
        x = input("Choose an option : ")
        match x:
            case "1":
                cursor.execute("SELECT * FROM Books")
                for row in cursor.fetchall():
                    print(row)
            case "2":
                name = input("Enter name of the book : ")
                nop = input("Enter number of pages : ")
                pub = input("Enter publisher's name : ")
                auth = input("Enter Author's name : ")
                cursor.execute(f"INSERT INTO Books(Book_Name,NOP,Publisher,Author) VALUES ('{name}',{nop},'{pub}','{auth}')")
                conn.commit()
            case "3":
                id = int(input("Enter Book's id : "))
                cursor.execute(f"DELETE FROM Books WHERE Id={id}")
                conn.commit()
            case "4":
                n_id = input("Enter your National number : ")
                name = input("Enter your full name : ")
                pnumber = input("Enter your phone nubmer : ")
                jdate = input("Enter join date(mm/dd/yyyy) : ")
                new_member = Member(n_id,name,pnumber,jdate)
                new_member.add_member()
            case "5":
                break

if __name__ == "__main__":
    main()