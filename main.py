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
#original print menu
print(print_menu())

#first input check
choice = int(input(">>> "))

#password check function
def check_password():
    password_input = input("Please enter your password: ")
    if password_input != "password":
        return print("Password is incorrect!")
    elif password_input == "password":
        return None

#registering vehicles
def register_vehicle():
    i = 0
    if i >= 50:
        print("The parking lot is full")
    elif i < 50:
        print("The parking lot has spaces")
        
        plate_number = []
        credit_card_number = []

        plate_number = input("Please input your plate number: ")
        credit_card_number = input("Enter your Credit Card Number (4.00$ charge): ")

        if plate_number in plate_number:
            print(f"{plate_number} is already registered")
        else:
            print(f"Thank you, your plate {plate_number} has been added to the lot.")
    for plate_number in plate_number:
        i + 1
    
#displaying vehicles
def display_vehicles():
    pass

while choice != 0 and choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
    print("Invalid input.")
    input1 = input("Press enter to continue....")
    if input1 == "":
        print(print_menu())
        choice = int(input(">>> "))
    else:
        print("Please input enter.")
    #valid choices
while choice == 0 or choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6:
    if choice == 1:
        register_vehicle()

        input1 = input("Press enter to continue....")
        if input1 == "":
            print(print_menu())
            choice = int(input(">>> "))
        else:
            print("Please input enter.")
        continue
    elif choice == 2:
        #verify_vehicle()
        continue
    elif choice == 3:
        check_password()
        display_vehicles()

        input1 = input("Press enter to continue....")
        if input1 == "":
            print(print_menu())
            choice = int(input(">>> "))
        else:
            print("Please input enter.")
        continue
    elif choice == 4:
        check_password()
        #diplay_charges()
        continue
    elif choice == 5:
        #remove_vehicle()
        continue
    elif choice == 6:
        #clear_vehicles()
        continue
    elif choice == 0:
        print("Thank you, goodbye!")
        break
    else:
        print("Invalid input.")
        input = input("Press enter to continue....")