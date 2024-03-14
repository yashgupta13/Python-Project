user_database=[]

def login():  
    get_data()
    print("Welcome")
    id=input("Enter Id-- ").strip()
    flag=check_id(id)
    while(flag==-1):
        print("Invalid id")
        print("Enter 'exit' as ID to exit login page")
        id=input("Enter Id-- ")
        if id == "exit":
            return "failed"
        flag=check_id(id)
    password=input("Enter Password--")
    attempts=1
    while(check_password(password,flag) != True and attempts<=5):
        print("Wrong Password")
        if attempts==5:
            return "failed"
        
        print(5-attempts,"attempts remaining")
        password=input("Enter Password--")
        attempts+=1
    print("Welcome",user_database[flag]['name'])
    fill_user_data()
    temp=user_database[flag]['id']
    user_database.clear()
    return temp


def check_id(s)->int:
    for i in range(0,len(user_database)):
        if s == user_database[i]['id']:
            return i
    return -1

def check_password(password,index)->bool:
    if user_database[index]['password']==password:
        return True
    else:
        return False
    

def get_data():
    file_path = 'C:/Users/yashg/Documents/Programs/Python/Project/user.txt'
    try:
        with open(file_path, 'r') as file:
            for line in file:
                fill_user_database(line.strip())
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    

def fill_user_database(line):
    words = line.split(',')
    id=words[0]
    name=words[1]
    password=words[2]
    age=int(words[3])
    amount_pending=int(words[4])
    user={'id':id , 'name':name , 'password':password , 'age':age , 'amount_due':amount_pending}
    user_database.append(user)


def add_user():
    get_data()
    name=input("Enter name --")
    age=int(input("Enter age--"))
    id=input("Enter a id--")
    while check_id(id)!=-1:
        print("This id is already in use")
        id=input("Enter another Id--")
    password=input("Enter your password--")
    user={'id':id , 'name':name , 'password':password , 'age':age , 'amount_due':0}
    user_database.append(user)
    fill_user_data()
    user_database.clear()

def remove_user():
    get_data()
    id=input("Enter user Id to be deleted--")
    index=check_id(id)
    while index==-1:
        print("Invalid Id")
        id=input("Enter user Id to be deleted--")
        index=check_id(id)
    user_database.pop(index)
    fill_user_data()
    user_database.clear()

def update_user_information(id):
    get_data()
    index=check_id(id)
    while index==-1:
        print("Invalid Id")
        id=input("Enter user Id to be Updated--")
        if id =="exit":
            break
        index=check_id(id)
    name=input("Enter new name --")
    age=int(input("Enter new age--"))
    id=input("Enter a new ID--")
    while check_id(id)!=-1:
        print("This id is already in use")
        id=input("Enter another Id--")
    password=input("Enter your new password--")
    user_database[index]['id']=id
    user_database[index]['name']=name
    user_database[index]['password']=password
    user_database[index]['age']=age
    fill_user_data()
    user_database.clear()


def fill_user_data():
    file_path = 'C:/Users/yashg/Documents/Programs/Python/Project/user.txt'
    try:
        with open(file_path, 'w') as file:
            for i in range(0,len(user_database)):
                content=user_database[i]['id']+","+user_database[i]['name']+","+user_database[i]['password']+","+str(user_database[i]['age'])+","+str(user_database[i]['amount_due'])
                file.write(content+'\n')
    except Exception as e:
        print(f"An error occurred: {e}")


def set_bill_for_user(userid,amount):
    get_data()
    index=-1
    for i in range(0,len(user_database)):
        if user_database[i]['id']==userid:
            index=i
    if index== -1:
        print("Invalid Id")
        return
    
    user_database[index]['amount_due']=user_database[index]['amount_due']+amount
    fill_user_data()
    user_database.clear()

def get_user_pending_bill(userid)->int:
    get_data()
    index=-1
    for i in range(0,len(user_database)):
        if user_database[i]['id']==userid:
            index=i
    if index== -1:
        print("Invalid Id")
        return 0
    
    amount_pending=user_database[index]['amount_due']
    fill_user_data()
    user_database.clear()
    return amount_pending

    
    


