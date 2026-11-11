contacts = []

def add_contact():
        
    print("Add Contact")
    while True:
        name = input("Name  : ").strip()
        if name:
            break
        print("Name cannot be empty")
        
    while True:
        phone = input("Number : ").strip()
        if len(phone)==10 and phone.isdigit() and phone[0] in "6789":
            duplicate = False
            for x in contacts:
                if phone == x['Phone']:
                    duplicate = True
                    break
            
            if duplicate:
                print("Phone number already exists")
                return

            else:
                break    


                       
        else:
            print("Enter correct number")

    while True:
        place = input("Place  : ").strip()
        if place:
            break
        print("Place cannot be empty!")       
        
    details = input("Details : ")

    entry = {"Name" : name, "Phone" : phone , "Place" : place , "Details" : details}
    contacts.append(entry)
        

def view_contact():
        
    if not contacts:
        print("The list is empty")  

    else:
        print("\n ---------Saved Contacts----------")
        for x in contacts:
            print("Name    :", x["Name"])
            print("Phone   :", x["Phone"])
            print("Place   :", x["Place"])
            print("Details :", x["Details"])
            print("--------------------------")             

def search_contact():
    search = input("Enter the name to be searched: ")
    found = False

    for x in contacts:
        if search.lower() in x["Name"].lower():
            print("Contact found")
            print(f"Name :{x['Name']}\nNumber :{x['Phone']}\nPlace :{x['Place']}\nDetails :{x['Details']}")
            found = True      

    if not found:
        print("Contact not found")

def update_contact():
    pass

def delete_contact():
    pass


while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter the choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contact()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Enter a valid choice")
