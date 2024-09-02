# python-_project-This Python project is a simple Contact Management System designed to help users create and view a list of contacts. It's structured to allow users to either add new contacts or view the ones they have already saved.

Key Features:
User Interaction:

The program prompts the user for their name and offers them two choices: either create new contacts or view existing contacts.
It handles user input and ensures that valid choices are entered before proceeding.
Contact Creation:

The new_contact() function collects a contact's name and phone number from the user and stores them in a global dictionary (contact_list).
Contacts are stored as key-value pairs, where the key is the contact name and the value is the contact number.
Viewing Contacts:

The show_contacts() function displays all saved contacts.
If no contacts are available, it informs the user that the contact list is empty.
Input Validation:

The program uses a loop to ensure that user input is valid. It converts user input to lowercase and strips extra spaces to avoid issues with case sensitivity or unintended spaces.
Program Flow:

After a user adds a new contact or views existing contacts, the program doesn't exit. It offers the option to continue by either adding more contacts or viewing the contact list again, making it interactive.
This repeat behavior is handled by the next_step() function, which prompts the user to make further choices.
Global Contact List:

The contact list is stored in a dictionary (contact_list), which is accessible throughout the program. This ensures that contacts are retained as long as the program runs.
Code Breakdown:
start() function:

This is the entry point of the program, where the user is greeted and asked for their initial choice of action (creating new contacts or viewing existing ones).
new_contact() function:

This function prompts the user to enter a contact's name and phone number and then saves this information in the contact_list.
show_contacts() function:

Displays the saved contacts. If there are no contacts, it prints a message saying "No contacts found."
next_step() function:

After creating or viewing contacts, this function asks the user if they want to add more contacts or check the current list, ensuring the program remains interactive.
Usage:
The user first enters their name.
Then they choose to either add a new contact or view existing ones.
If they choose "New", they will be prompted to enter the name and phone number of a contact.
If they choose "Contacts", they can view the list of all contacts saved so far.
After performing one of these actions, the program will continue running, allowing the user to make additional contacts or view the list as often as they like until they choose to quit.
Overall:
This project is a simple yet effective way to understand basic concepts in Python, including:

Functions: Each task is separated into functions that can be called repeatedly.
Loops and Conditionals: The program uses while loops and if-elif-else statements to control user input and ensure valid choices.
Dictionaries: Contacts are stored as key-value pairs in a dictionary, providing efficient storage and retrieval.
This is a great beginner project to practice Python fundamentals while building a useful application!
