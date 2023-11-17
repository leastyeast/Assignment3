def print_menu():
    # menu formatting
    menu = "----------------------------------------------------\n\
*** Welcome to Park and Go Parking Application! ***\n\
----------------------------------------------------\n\
Select from the following options:\n\
1- Register a vehicle\n\
2- Verify vehicle registration\n\
3- Display registered vehicles and save them to a file\n\
4- Display daily charges and save them to a file\n\
5- Remove a vehicle\n\
6- Clear vehicles\n\
0- Exit"
    return menu

print(print_menu())

choice = int(input(">>> "))

while choice != 0 and choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
    #invalid choices
    print("Invalid input.")
    input1 = input("Press enter to continue....")
    if input1 == "":
        print(print_menu())
        choice = int(input(">>> "))
    else:
        print("Please input enter.")
    #valid choices
    if choice == 1:
        print("1")
        continue
    elif choice == 2:
        print("2")
        continue
    elif choice == 3:
        print("3")
        continue
    elif choice == 4:
        print("4")
        continue
    elif choice == 5:
        print("5")
        continue
    elif choice == 6:
        print("6")
        continue
    elif choice == 0:
        print("0")
        continue

def check_password():
    password_input = input("Please enter your password: ").lower()
    if password_input == "password":
        return None
    elif password_input is not "password":
        output = "Password is incorrect!"
        return output
