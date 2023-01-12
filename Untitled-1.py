class User:
    def __init__(self,name,roll,password):
        self.name=name
        self.roll=roll
        self.password=password
        self.borrow_books=[]
        self.returned_books=[]

class Library:
    def __init__(self,book_list):
        self.book_list=book_list
    def borrow_book(self,bookName,user):
        for book in self.book_list:
            if book==bookName:
                if bookName in user.borrow_books:
                    print("You have to return it first")
                    return
                if self.book_list[book]==0:
                    print("Sorry,this book is over")
                    return
                self.book_list[book]-=1       
                user.borrow_books.append(bookName)
                print("Borrow done")
                return

        print("This Book is not available")

    def return_book(self,bookName,user):
        if bookName in self.book_list:
            self.book_list[bookName]+=1
            user.borrow_books.remove(bookName)
            user.returned_books.append(bookName)
            print("Book returned successfully")
            return
        print("This book isn't belong to this library")   
    def donate(self,bookname,amount):
        if bookname in self.book_list:
            self.book_list[bookname]+amount
            print("Thanks for donating")  
            return  
        self.book_list[bookname]=amount 
        print("Thanks for donating")     
    def booklist(self):
        for book in self.book_list:
            if self.book_list[book]>0:
                print(book)    

                    


lb=Library({"English":2,"Bangla":5,"Math":3})
allUsers=[]
current_user=None

while True:
    if current_user==None:
        print("Not logged in\nPlease Login or create account(L/C)")
        option=input()
        
        if option=='L':
            roll=int(input("Roll: "))
            password=input("Password: ")
            match=False
            for user in allUsers:
                if user.roll==roll and user.password==password:
                    current_user=user
                    match=True
            if match==False:
                    print("No user found")      

        else:            
            name=input("Name: ")
            roll=int(input("Roll: "))
            password=input("Passwod: ")
            found=False
            #loop to check creating account with same roll or not
            for i in allUsers:
                if i.roll==roll:
                    print("Account already created")
                    current_user==None
                    found=True
            if found==True:
                continue        
            user=User(name,roll,password)
            current_user=user
            allUsers.append(user)
            """ print("End of user")
            break """

    else:
        print("OPTIONS",end='')
        print("__________")
        print("1.Borrow a book")
        print("2.Return a book")
        print("3.Borrowed books list")
        print("4.Returned books list")
        print("5.Check book list")
        print("6.Donate")
        print("7.Logout")
        x=int(input("Choose a option\n"))
        if x==1:
            bookName=input("Book name: ")
            lb.borrow_book(bookName,current_user)
        elif x==2:    
            bookName=input("Book name: ")
            lb.return_book(bookName,current_user)
        elif x==3:
            print(current_user.borrow_books)
        elif x==4:
            print(current_user.returned_books)   
        elif x==5:
              #print(lb.book_list) 
              lb.booklist()
        elif x==6:
            bookName=input("Book name: ")
            """ if bookName in lb.book_list:
                lb.book_list[bookName]+=1
              else:
                lb.book_list[bookName]=1 """
            amount=int(input("amount: "))
            lb.donate(bookName,amount)     
        else:
            current_user=None      
                 
        """ lb.borrow_book("English",current_user)
        print(lb.book_list)
        print(current_user.borrow_books)
        lb.borrow_book("English",current_user)
        lb.return_book("Science",current_user) """
        #break

"""
C
Manar
44
123
"""

""" 
C
Manar
44
123
1
English
2
Science
1
English 

"""


         



