
from file_handling import load_contacts, save_contacts

    
contacts = load_contacts()



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

    save_contacts(contacts)
        

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
    while True:
        print("----------SEARCH CONTACTS----------\n1. Search by name\n2. Search by Phone number\n3. Exit to main menu\n")
        choice =input("Enter your option:").strip()
        

        if choice == "1":
            search = input("Enter the name to be searched: ").strip()
            found = False
            if contacts:
               
                for x in contacts:
                    if search.lower() in x["Name"].lower():
                        print("Contact found")
                        print(f"Name :{x['Name']}\nNumber :{x['Phone']}\nPlace :{x['Place']}\nDetails :{x['Details']}")
                        found = True      

                if not found:
                    print("Contact not found")

            else:
                print("Contact list is empty")


        elif choice == "2":
            search = input("Enter the phone number to be searched :").strip()
            found = False
            if contacts:
                
                for x in contacts:
                    if search == x["Phone"]:
                        print("Contact found")
                        print(f"Name :{x['Name']}\nNumber :{x['Phone']}\nPlace :{x['Place']}\nDetails :{x['Details']}")
                        found = True      
            
                if not found:
                    print("Contact not found")

            else:
                print("Contact list is empty")

        elif choice == "3":
            break

        else:
            print("Enter correct choice")            


def update_contact():
    update = input("Enter the name that you desire to update :")
    if not contacts:
        print("List is empty")
    else:
        found = False
        
        for x in contacts:
            if update.lower() == x["Name"].lower():

                while True:
                    print("What do you want to update:\n1.Name\n2.Phone\n3.Place\n4.Details\n5.Exit")

                    choice = input("").strip()

                    if choice == '1':
                        duplicate = False
                        n_name = input("Enter the new name :").strip()
                        
                            
                        
                        for y in contacts:
                            if n_name.lower() == y["Name"].lower() and y!=x:
                                duplicate = True
                                break
                        
                        if not n_name:
                            print("Name cannot be empty")
                        
                        elif duplicate == True:
                            print("Name already exists")

                        else:
                            x["Name"] = n_name
                            save_contacts(contacts)
                            print("Sucessfully updated")

                    elif choice == '2':
                        n_phone = input("Enter the new phone :").strip()
                        if len(n_phone)==10 and n_phone.isdigit() and n_phone[0] in "6789":
                            
                            duplicate = False
                            for y in contacts:
                                if n_phone == y['Phone'] and y != x:
                                    duplicate = True
                                    break
                                        
                            if duplicate:
                                print("Phone number already exists")
                                continue
                            
                            else:
                                x["Phone"] = n_phone  
                                save_contacts(contacts) 
                                print("Sucessfully updated")

                        else:
                            print("Invalid number")

                        

                    elif choice == '3':
                        n_place = input("Enter the new place :").strip()
                        if not n_place:
                            print("Place cannot be empty")
                        else:    
                            x["Place"] = n_place
                            save_contacts(contacts)
                            print("Sucessfully updated")

                    elif choice == '4':
                        n_details = input("Enter the new details") 
                        x["Details"] = n_details 
                        save_contacts(contacts)
                        print("Sucessfully updated")

                    elif choice == '5':
                        break

                    else:
                        print("Invalid choice")    


                found = True      
                break
        if not found:
            print("Contact not found")
            

        


def delete_contact():
    if not contacts:
        print("Contact list is empty")
        return

    delete = input("Enter the name of the contact you want to delete: ").strip()
    found = False

    for x in contacts:
        if delete.lower() == x["Name"].lower():

            print("\nContact found!")
            print("Name  :", x["Name"])
            print("Phone :", x["Phone"])
            print("Place :", x["Place"])

            confirm = input(
                "Are you sure you want to delete? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                contacts.remove(x)
                save_contacts(contacts)  
                print("Contact successfully deleted")

            elif confirm == "no":
                print("Deletion cancelled")

            else:
                print("Invalid choice. Deletion cancelled")

            found = True
            break

    if not found:
        print("Contact not found")

      

def total_contacts():
    print("Total contacts:", len(contacts))     

def sort_contacts():
    
    sorted_contacts = sorted(contacts,key = lambda x: x["Name"].lower())
    return sorted_contacts




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
        total_contacts()  

    elif choice == "7":
        for x in sort_contacts():
            print(x["Name"], x["Phone"])

    elif choice == "8":
        print("Exiting...")
        break

    

    else:
        print("Enter a valid choice")
