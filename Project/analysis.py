import books_data_handler
from tabulate import tabulate
class book_sales_analysis:
    books=None
    def __init__(self) -> None:
        self.books=books_data_handler.get_book_list()

    def most_sold_book(self):
        mostsold=self.books[0]
        for i in range(len(self.books)):
            if(self.books[i]['sold'] > mostsold['sold']):
                mostsold=self.books[i]
        print(mostsold)
    def trending_books(self):
        sorted_list = sorted(self.books, key=lambda x: x['sold'],reverse=True)
        sorted_list=sorted_list[:5]
        keys_to_include = ['name', 'price']
        filtered_data = [{key: item[key] for key in keys_to_include} for item in sorted_list]
        print(tabulate(filtered_data, headers="keys", tablefmt="grid"))
    def total_sales(self):
        sales=0
        for i in range(len(self.books)):
            sales=sales+(self.books[i]['sold']*self.books[i]['price'])
        print("Total Sales--\u20B9",sales)

def controller_for_user():
    a=book_sales_analysis()
    option=4
    print("Enter 1 to get most sold book")
    print("Enter 2 to get trending books")
    print("Enter 3 to go back")
    try:
        option=int(input("Enter Choice"))
    except ValueError:
        print("Wrong Format")
            
    if option==1:
        a.most_sold_book()
    elif option==2:
        a.trending_books()
    elif option==3:
        print()
    else:
        print("Wrong Option")
    
def controller():
    a=book_sales_analysis()
    option=4
    print("Enter 1 to get most sold book")
    print("Enter 2 to get total sales")
    print("Enter 3 to get trending books")
    print("Enter 4 to Exit")
    try:
        option=int(input("Enter Choice"))
    except ValueError:
        print("Wrong Format")
            
    if option==1:
        a.most_sold_book()
    elif option==2:
        a.total_sales()
    elif option==3:
        a.trending_books()
    elif option==4:
        print("Exit")
    else:
        print("Wrong Option")
    