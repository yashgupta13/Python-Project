import books_data_handler
import user_data_handler
def admin_inteface():
    while(True):
        print("Enter 1 to Update catalogue")
        print("Enter 2 to Add User")
        print("Enter 3 to Remove User")
        print("Enter 4 to Update User Information")
        print("Enter 5 to Update User Bill")
        print("Enter 6 exit")
        option=int(input())

        if option==1:
            books_data_handler.books_data_controller_for_admin()
        elif option==2:
            user_data_handler.add_user()
        elif option==3:
            user_data_handler.remove_user()
        elif option==4:
            id=input("Enter Id to be Updated--")
            user_data_handler.update_user_information(id)
        elif option==5:
            id=input("Enter Id --")
            amount=int(input("Enter Amount to be Added--"))
            user_data_handler.set_bill_for_user(id,amount)
        elif option==6:
            print("Exit")
            break
        else:
            print("Wrong Option")
            