from prettytable import PrettyTable 
users = []  

def sign_up():
    user = {}  
    user["name"] = input("Enter Name: ")
    user["email"] = input("Enter Email: ")
    user["password"] = input("Enter Password: ")
    users.append(user) 
    print("Sign-up successful!\n")

def login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    
    for user in users: 
        if user["email"] == email and user["password"] == password:
            print("Login successful!\n")
            return
    print("Login failed! Incorrect email or password.\n")

def show_users():
    if not users:
        print("No users available.\n")
        return

    table = PrettyTable(["Name", "Email"]) 
    for user in users:
        table.add_row([user["name"], user["email"]])
    
    print("\nRegistered Users:")
    print(table)

def delete_user():
    email = input("Enter Email to delete: ")
    
    for user in users: 
        if user["email"] == email:
            users.remove(user)
            print("User deleted.\n")
            return
    print("User not found.\n")