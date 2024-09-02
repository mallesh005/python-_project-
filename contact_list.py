contact_list = {}  # Renamed the list to contact_list to avoid conflicts with the reserved keyword

def start():
    print("Welcome to Contact+ \n\nPlease enter your name: ", end="")
    name = input()  # input() for Python 3
    print(f"Hi {name}, would you like to check your current contacts or make new ones?")
    print("To make new contacts type in 'New'")
    print("To check current contacts type in 'Contacts'")
    print("Go to: ", end="")
    choose = input().strip().lower()  # Simplified input checking by using lower()

    while True:
        if choose == "new":
            new_contact()
            break
        elif choose == "contacts":
            show_contacts()
            break
        else:
            print("Invalid option. Please type 'New' or 'Contacts'.")
            choose = input().strip().lower()

def new_contact():
    print("\nPlease input the name: ", end="")
    contact_name = input().strip()
    print("Please input the number: ", end="")
    contact_number = input().strip()
    
    contact_list[contact_name] = contact_number  # Updating the global contact list
    print("Contact created.")
    
    next_step()

def show_contacts():
    if contact_list:
        for name, number in contact_list.items():
            print("\n---------------------------------------------------------")
            print(f"Name: {name}")
            print(f"Number: {number}")
            print("---------------------------------------------------------")
    else:
        print("No contacts found.")

    next_step()

def next_step():
    print("\nWould you like to make more contacts or check current contacts?")
    print("To make new contacts type in 'New'")
    print("To check current contacts type in 'Contacts'")
    print("Go to: ", end="")
    
    choose = input().strip().lower()
    
    while True:
        if choose == "new":
            new_contact()
            break
        elif choose == "contacts":
            show_contacts()
            break
        else:
            print("Invalid option. Please type 'New' or 'Contacts'.")
            choose = input().strip().lower()

# Start the program
start()
