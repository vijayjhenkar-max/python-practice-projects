contacts = []


while True:

    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter the choice :")


    if choice == "1":
        print("Add Contact")
        name = input("Name  : ")
        phone = input("Number : ")
        place = input("Place : ")
        details = input("Details : ")

        entry = {"Name" : name, "Phone" : phone , "Place" : place , "Details" : details}
        contacts.append(entry)
        

    elif choice == "2":
        
        if contacts == []:
            print("The list is empty")  

        else:
            print("\n ---------Saved Contacts----------")
            for x in contacts:
                print("Name    :", x["Name"])
                print("Phone   :", x["Phone"])
                print("Place   :", x["Place"])
                print("Details :", x["Details"])
                print("--------------------------")             

    elif choice == "3":
        print("Search Contact")

    elif choice == "4":
        print("Update Contact")

    elif choice == "5":
        print("Delete Contact")              

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Enter valid choice")