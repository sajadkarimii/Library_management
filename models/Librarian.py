import os
import time

class Librarian:
    def __init__(self,FullName='sajad karimi',UserName='sajad',Password='2233123'):
        self.__FullName = FullName
        self.__UserName = UserName
        self.__Password = Password

    def login(self):
        os.system("cls" if os.name == "nt" else "clear")
        username = input("Enter username :")
        password = input("Enter password :")
        if (username == self.__UserName and password == self.__Password):
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Wellcome {self.__FullName}")
            time.sleep(2)
            return True
        else:
            if (self.login()):
                return True
