class Library:
    def __init__(self, list, name):
        self.name=name
        self.booklist=list
        self.lenddict={}

    def displayBook(self):
        print(f"the list of books in {self.name} are:")
        for bk in self.booklist:
            print(bk)


    def lendBook(self,user,book):
        if book not in self.lenddict.keys():
            print("lenddict updated you can take the book\n")
            self.lenddict.update({book:user})

        else:
            print(f"the book is already issues by {self.lenddict[book]}\n")    

    def showLenders(self):
        print(f"the books with book lender name are as follows: {self.lenddict.items()}\n")
        print(f"the books you cant take are as follows:{self.lenddict.keys()}\n")

    def addBook(self,book):
        print(f"enter the book name you want to add in library {self.name}\n")
        self.booklist.append(book)
        print("book has been added to the list\n")

    def returnBook(self,book):
        self.lenddict.pop(book)
    




if __name__ == '__main__':

    list1=['c++ basics','python','akhimot jar heral xima']        
    mrinal=Library(list1,"greatLibrary")

    while(True):
        print(f"welcome to the {mrinal.name} library. Enter the choice::\n1.display books.  \n2.lend a book. \n3.show lenders. \n4.add a book. \n5.return a book")

        user_choice=int(input())

        if user_choice==1:
            mrinal.displayBook()

            
        elif user_choice==2:
            book=input("enter the book name want to issue\t")
            user=input("enter your name\t")
            mrinal.lendBook(user,book)

        elif user_choice==3:
            mrinal.showLenders()

        elif user_choice==4:
            book=input("enter the book you want to add \t")
            mrinal.addBook(book)

        elif user_choice==5:
            book=input("enter the book you want to return \t")
            mrinal.returnBook(book)

        else:
            print("invalid choice")


        print("press q to quit c to continue")
        user_choice2 = ""
        while(user_choice2 !="q" and user_choice2 !="c" ):
            user_choice2=input()    


            if user_choice2=="q":
                exit()

            elif user_choice2=="c":
                continue

            else:
                print("press a valid one")
                continue

        


        


