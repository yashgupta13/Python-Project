import books_data_handler
import user_data_handler
def user_inteface(id):
    while(True):
        print("Enter 1 to Go to Store")
        print("Enter 2 to Update profile")
        print("Enter 3 to Generate Invoice of pending bill")
        print("Enter 4 exit")
        option=int(input())
        if option==1:
            books_data_handler.books_data_controller_for_user(id)
        elif option==2:
            user_data_handler.update_user_information(id)
        elif option==3:
            amount_due=user_data_handler.get_user_pending_bill(id)
            print("Your Total Amount Due --",amount_due)
            print("Enter 1 to pay")
            option=int(input("Enter your Choice -- "))
            if option==1:
                user_data_handler.set_bill_for_user(id,-amount_due)
                print("Thank You For Paying Bill")
        elif option==4:
            print("Thank You , Have a Nice Day!!")
            break
        else:
            print("Wrong Option")
