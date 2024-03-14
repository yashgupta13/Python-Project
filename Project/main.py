import user_data_handler
import admin_handler
import user_handler

print("Enter 1 to Login")
print("Enter 2 to Sign Up")
choice=int(input("Enter Your Choice -- "))
if choice==1:
    id=user_data_handler.login()
    if id == "admin":
        admin_handler.admin_inteface()
    elif id == "failed":
        print("Login Failed")
    else:
        user_handler.user_inteface(id)
elif choice == 2:
    user_data_handler.add_user()
else:
    print("Invalid Choice")
