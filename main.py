#  Python3 Code for Library Management System using OOPs Concept.


class Library:

    def __init__(self , list, name):
        self.booksList = list
        self.name = name
        self.lenddict = {}
    
    def displaybook(self):
        print(f"We have following books in our library  : {self.name}")
        for book in self.booksList:
            print(book)

    def lendbook(self,user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lenddict[book]}")
    
    def searchbook(self , book):
        if book not in self.booksList:
            print("This book is not avaliable.")
            print("You want to add this book: 'Y' or 'N' ")
            c = input()
            if c=="Y":
                book = input("Enter the book name:")
                ram.addbook(book)
            else:
                pass

    def addbook(self , book):
        self.booksList.append(book)
        print("Book has been added to the book list.")

    def returnbook(self,book):
        self.lenddict.pop(book)
if __name__=="__main__":
    ram = Library(['Python','Rich Daddy Poor Daddy','Harry Potter','C++ Basics'],"World")

    while(True):

        print(f"Welcome to the {ram.name} Library. \n Enter your choice to continue: ")
        print("1. Display Books") 
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Enter the book to Search")

        user_choice = int(input())

        if user_choice == 1:
            ram.displaybook()
        elif user_choice==2:
            book = input("Enter the name of book you want to land")
            user = input("Enter your name")
            ram.lendbook(user, book)
        elif user_choice ==3:
            book = input("Enter the name of book you want to add")
            ram.addbook(book)
        elif user_choice ==4:
            book= input("Enter the book you want to return")
            ram.returnbook(book)
        elif user_choice==5:
            book = input("Enter the book to search")
            ram.searchbook(book)
        else:
            print("Not a valid choice")
        
        print("Press q to Quit and c to continue")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2  = (input("Enter your choice:"))
            if user_choice2 == "q":
                exit()
            elif user_choice2=="c":
                continue
