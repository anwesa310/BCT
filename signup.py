import main as a
while True:
    print("\n1. Sign Up\n2. Login\n3. Show Users\n4. Delete User\n5. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        a.sign_up()
    elif choice == "2":
        a.login()
    elif choice == "3":
        a.show_users()
    elif choice == "4":
        a.delete_user()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")