# introductory formatting
print("----------------------------------------------------")
print("*** Welcome to Park and Go Parking Application! ***")
print("----------------------------------------------------")

def print_menu():
    # menu formatting
    menu = "Select from the following options:\n\
1- Register a vehicle\n\
2 - Verify vehicle registration\n\
3- Display registered vehicles and save them to a file\n\
4- Display dialy charges and save them to a file\n\
5- Remove a vehicle\n\
6- Clear vehicles\n\
0- Exit"
    return menu

print(print_menu())

choice = int(input(">>> "))

if choice == 1:
    pass
elif choice == 2:
    pass
elif choice == 3:
    pass
elif choice == 4:
    pass
elif choice == 5:
    pass
elif choice == 6:
    pass

def check_password():
    password_input = input("Please enter your password: ").lower()
    if password_input == "password":
        return None
    elif password_input is not "password":
        output = "Password is incorrect!"
        return output

print(check_password())
