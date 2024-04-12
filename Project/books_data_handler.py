import user_data_handler
import analysis
from tabulate import tabulate
books=[]
def get_data():
    file_path = 'C:/Users/yashg/Documents/Programs/Python/Project/Library managment/books.txt'
    try:
        with open(file_path, 'r') as file:
            for line in file:
                get_book_data(line)
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_book_list():
    get_data()
    return books

def get_book_data(line):
    words = line.split(',')
    book_name=words[0]
    book_count=int(words[1])
    book_price=int(words[2])
    book_sold=int(words[3])
    book={'name':book_name , 'count' :book_count,'price':book_price ,'sold':book_sold}
    books.append(book)

def add_book():
    book_name=input("Enter Book Name--")
    book_count=int(input("Enter Book Count--"))
    book_price=int(input("Enter Book Price--"))
    book={'name':book_name , 'count':book_count , 'price':book_price,'sold':0}
    books.append(book)

def print_book_details():
    keys_to_include = ['name', 'price']
    filtered_data = [{key: item[key] for key in keys_to_include} for item in books]
    print(tabulate(filtered_data, headers="keys", tablefmt="grid"))

def remove_book():
    print_book_details()
    id=int(input("Enter book id to be deleted--"))
    books.pop(id)

def update_book_details():
    print_book_details()
    id=int(input("Enter book id to be updated--"))
    if id > len(books) or id <0:
        print("Invalid Id")
    else:
        book_name=input("Enter new name--")
        book_count=int(input("Enter new Book count--"))
        book_price=int(input("Enter new Book Price--"))
        books[id]['name']=book_name
        books[id]['count']=book_count
        books[id]['price']=book_price

def search_book():
    book_name=input("Enter book name to be searched--")
    flag=False
    for i in range(0,len(books)):
        if books[i]['name']==book_name:
            print("Book is available")
            print("id-",(i),books[i])
            flag=True
    if flag==False:
        print("Entered book is not availble")




def fill_book_data():
    file_path = 'C:/Users/yashg/Documents/Programs/Python/Project/Library managment/books.txt'
    try:
        with open(file_path, 'w') as file:
            for i in range(0,len(books)):
                content=books[i]['name']+","+str(books[i]['count'])+","+str(books[i]['price'])+","+str(books[i]['sold'])
                file.write(content+'\n')
    except Exception as e:
        print(f"An error occurred: {e}")

def books_data_controller_for_admin():
    get_data()
    while(True):
        print("Enter 1 to Add Book")
        print("Enter 2 to Remove Book")
        print("Enter 3 to Update Book Information")
        print("Enter 4 to Search for a Book")
        print("Enter 5 to Print Books Information")
        print("Enter 6 exit")
        option=int(input())

        if option==1:
            add_book()
            print("Book was sucessfully added!!") 
        elif option==2:
            remove_book()
            print("Book was sucessfully removed!!") 
        elif option==3:
            update_book_details()
            print("Book details was sucessfully updated!!")
        elif option==4:
            search_book()
        elif option==5:
            print_book_details()
        elif option==6:
            print("Exit")
            break
        else:
            print("Wrong Option")
    fill_book_data()


def books_data_controller_for_user(id):
    get_data()
    while(True):
        print("Enter 1 to Explore Catalogue")
        print("Enter 2 to Search Book")
        print("Enter 3 to Buy Book")
        print("Enter 4 to go back to Main Menu")
        option=int(input())
        if option==1:
            analysis.controller_for_user()
        elif option==2:
            search_book()
        elif option==3:
            buybook(id)
        elif option==4:
            break
        else:
            print("Wrong Option")

    fill_book_data()

def buybook(user_id):
    book_cart=[]
    while True :
        print("Enter -1 as Book Id to Checkout")
        book_id=int(input("Enter Book Id --"))
        if book_id== -1:
            checkout(user_id,book_cart)
            break
        
        if(check_book_id(book_id)):
            print("Book Name ",books[book_id]['name']," Price ",books[book_id]['price'])
            print("Enter 1 to Add Book to Cart")
            print("Enter 2 to Change Book")
            option=int(input("Enter Choice--"))
            if(option==1):
                book_cart.append(books[book_id])
                update_inventory(book_cart)
            elif(option == 2):
                continue
            else:
                print("Wrong Option")
                

def check_book_id(book_id:int)->bool:
    if book_id > len(books) or book_id<0:
        return False
    else:
        return True
    
def checkout(user_id:str , book_cart):
    bill=0
    for i in range(0,len(book_cart)):
        bill=bill+book_cart[i]['price']
    user_data_handler.set_bill_for_user(user_id,bill)
    
def update_inventory(book_cart):
    for i in range(0,len(books)):
        if books[i]['name']==book_cart[-1]['name']:
            if books[i]['count']<=1:
                books.pop(i)
                break
            else:
                books[i]['count']-=1
                books[i]['sold']+=1

        


    

    
