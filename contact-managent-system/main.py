
from file_handling import load_contacts
from contact_function import (
    add_contact,
    view_contact,
    search_contact,
    update_contact,
    delete_contact,
    sort_contacts,
    total_contacts
)

    
contacts = load_contacts()



while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Total Contacts")
    print("7. Sort Contacts")
    print("8. Exit")

    choice = input("Enter the choice: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contact(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        update_contact(contacts)

    elif choice == "5":
        delete_contact(contacts)

    elif choice == "6":
        total_contacts(contacts)  

    elif choice == "7":
        for x in sort_contacts(contacts):
            print(x["Name"], x["Phone"])

    elif choice == "8":
        print("Exiting...")
        break

    

    else:
        print("Enter a valid choice")
