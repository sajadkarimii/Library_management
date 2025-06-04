import os
import time
from models.Librarian import Librarian
from models.Borrow import Borrowed
from models.Books import *
from models.Members import *

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    login = Librarian()
    if login.login():
        while True:
            clear_screen()
            print(
                "1: Books mangement\n2: Members management\n3: Borrowed management\n4: Exit"
            )
            x = input("Choose an option : ")
            match x:
                case "1":
                    while True:
                        clear_screen()
                        print(
                            "1: Add book\n2: Update book\n3: Show books\n4: Delete book\n5: Search book\n6: main page"
                        )
                        x = input("Choose an option : ")
                        if x == "1":
                            clear_screen()
                            genre_book = {
                                "1": MathBook,
                                "2": NovelBook,
                                "3": RomanticBook,
                                "4": ScientificBook,
                                "5": ExperimentalBook,
                            }
                            print(
                                "1: MathBook\n2: NovelBook\n3: RomanticBook\n4: ScientificBook\n5: ExperimentalBook"
                            )
                            y = input("Please first, choose a genre: ")
                            if y in genre_book:
                                clear_screen()
                                bookname = input("Enter Book Name: ")
                                publisher = input("Enter Publisher: ")
                                author = input("Enter Author Name: ")
                                quantity = int(input("Enter Quantity: "))
                                bk = genre_book[y]
                                new_book = bk(bookname, publisher, author, quantity)
                                new_book.add_book()
                        elif x == "2":
                            clear_screen()
                            bookname = input("Enter Book Name you want to edit : ")
                            bookname1 = input("Enter edited Book Name: ")
                            publisher = input("Enter edited Publisher: ")
                            author = input("Enter edited Author Name: ")
                            genre = input("Enter edited Genre: ")
                            quantity = input("Enter edited Quantity: ")
                            new_book = Book(bookname1, publisher, author, genre, quantity)
                            new_book.update_book(bookname)
                        elif x == "3":
                            clear_screen()
                            new_book = Book("", "", "", "", "")
                            for book in new_book.show_book():
                                print(book)
                            time.sleep(5)
                        elif x == "4":
                            clear_screen()
                            bookname = input("Enter book name to delete: ")
                            new_book = Book(bookname, "", "", "", "")
                            new_book.delete_book()
                        elif x == "5":
                            clear_screen()
                            bookname = input("Enter book name to search : ")
                            new_book = Book(bookname, "", "", "", "")
                            for book in new_book.search_book():
                                print(book)
                            time.sleep(5)
                        elif x == "6":
                            break
                case "2":
                    while True:
                        clear_screen()
                        print(
                            "1: Add member\n2: Update member\n3: Show members\n4: Delete member\n5: Search member \n6: Main page"
                        )
                        x = input("Choose an option : ")
                        if x == "1":
                            clear_screen()
                            n_id = input("Enter member's National number : ")
                            name = input("Enter member's full name : ")
                            pnumber = input("Enter member's phone nubmer : ")
                            jdate = input("Enter join date(yyyy-mm-dd) : ")
                            new_member = Member(n_id, name, pnumber, jdate)
                            new_member.add_member()
                        elif x == "2":
                            clear_screen()
                            n_id = input("Enter member's National number : ")
                            name = input("Enter edited member's full name : ")
                            pnumber = input("Enter edited member's phone nubmer : ")
                            jdate = input("Enter edited join date(yyyy-mm-dd) : ")
                            new_member = Member(n_id, name, pnumber, jdate)
                            new_member.update_member()
                        elif x == "3":
                            clear_screen()
                            new_member = Member("", "", "", "")
                            for member in new_member.show_members():
                                print(member)
                            time.sleep(5)
                        elif x == "4":
                            clear_screen()
                            n_id = input("Enter member's National number : ")
                            new_member = Member(n_id, "", "", "")
                            new_member.delete_member()
                        elif x == "5":
                            clear_screen()
                            fullname = input("Enter member's FullName : ")
                            new_member = Member("", fullname, "", "")
                            for member in new_member.search_member():
                                print(member)
                            time.sleep(5)
                        elif x == "6":
                            break
                case "3":
                    while True:
                        clear_screen()
                        print("1: Add Borrow\n2: Update Borrow\n3: Show Borrow\n4: Delete Borrow\n5: Search Borrow \n6: Main page")
                        x = input("Choose an option : ")
                        if (x == '1'):
                            clear_screen()
                            member_id = int(input("Enter member's id : "))
                            book_id = int(input("Enter book's id : "))
                            borrowdate = input("Enter borrow date(yyyy-mm-dd) : ")
                            respite = int(input("Enter respite : "))
                            returned = input("Enter returned date : ")
                            new_Borrow = Borrowed(member_id,book_id,borrowdate,respite,returned)
                            new_Borrow.add_borrow()
                        elif (x == '2'):
                            clear_screen()
                            id = int(input("Enter borrow id : "))
                            member_id = int(input("Enter member's id : "))
                            book_id = int(input("Enter book's id : "))
                            borrowdate = input("Enter borrow date(yyyy-mm-dd) : ")
                            respite = int(input("Enter respite : "))
                            returned = input("Enter returned date : ")
                            new_Borrow = Borrowed(member_id,book_id,borrowdate,respite,returned)
                            new_Borrow.update_borrow(id)
                        elif (x == '3'):
                            clear_screen()
                            new_Borrow = Borrowed('','','','','')
                            for borrow in new_Borrow.show_borrow():
                                print(borrow)
                            time.sleep(5)
                        elif (x == '4'):
                            clear_screen()
                            id = int(input("Enter borrow id you want to delete: "))
                            new_Borrow = Borrowed('','','','','')
                            new_Borrow.delete_borrow(id)
                        elif (x == '5'):
                            clear_screen()
                            member_id = int(input("Enter member's id : "))
                            new_Borrow = Borrowed(member_id,'','','','')
                            for borrow in new_Borrow.search_borrow():
                                print(borrow)
                            time.sleep(5)
                        elif(x == '6'):
                            break
                case "4":
                    break

if __name__ == "__main__":
    main()
