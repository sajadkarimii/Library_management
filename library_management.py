import sqlite3
import os
import time

# Connect to sqlite3
conn = sqlite3.connect("library_mange.db")
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
        cursor.execute(f"INSERT INTO Members(N_Id,FullName,PNumber,Join_Date) VALUES ('{self.N_Id}','{self.FullName}','{self.Phone}','{self.join_date}')")
        conn.commit()

    def delete_member(self):
        cursor.execute(f"DELETE FROM Members WHERE N_Id = '{self.N_Id}'")
        conn.commit()
    
    def show_members(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        cursor.execute(f"SELECT * FROM Members")
        for row in cursor.fetchall():
            print(row)

    def update_member(self):
        cursor.execute(f"UPDATE Members SET FullName = '{self.FullName}' , PNumber = '{self.Phone}' , Join_Date = '{self.join_date}' WHERE N_Id = '{self.N_Id}'")
        conn.commit()

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""1: Books mangement\n2: Members management\n3: Borrowed management\n4: Exit""")
        x = input("Choose an option : ")
        match x:
            case "1":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("""1: Add book\n2: Update book\n3: Show books\n4: Delete book\n5: main page""")
                    x = input("Choose an option : ")
                    if(x=='5'):
                        break
            case "2":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("""1: Add member\n2: Update member\n3: Show members\n4: Delete member\n5: main page""")
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
                        new_member = Member('','','','')
                        new_member.show_members()
                        time.sleep(5)
                    elif (x == '4'):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        n_id = input("Enter member's National number : ")
                        new_member = Member(n_id,'','','')
                        new_member.delete_member()
                    elif(x == '5'):
                        break
            case "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                pass
            case "4":
                break

if __name__ == "__main__":
    main()
