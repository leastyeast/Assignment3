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

#

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
elif choice == 0:
    pass
else:
    print("Invalid input.")
    input1 = input("Press enter to continue....")
    if input1 == "":
        print(print_menu())
    else:
        print("Please press enter.")

def check_password():
    password_input = input("Please enter your password: ").lower()
    if password_input == "password":
        return None
    elif password_input is not "password":
        output = "Password is incorrect!"
        return output
