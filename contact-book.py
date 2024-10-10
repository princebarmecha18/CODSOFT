contact=[["Prince",8667654917,"prince@gmail.com","sholavaram"],["Prince",8667654919,"prince@gmail.com","sholavaram"]]

#Add new contact
def add_contact():
    print("*=====ADD A NEW CONTACT=====*\n")
    name = input("Enter Name: ").capitalize()
    phone_no=int(input("Enter Phone Number: "))
    email= input("Enter EMAIL ID: ")
    address = input("Enter Address: ").capitalize()
    data=[name,phone_no,email,address]
    contact.append(data)
    print("Contact Added Successfully")

#Delete Contact
def delete_contact():
    print("*=====DELETE A CONTACT=====*\n")
    delete_name=input("Enter The Name of The Contact: ").capitalize()
    found=False
    for data in contact:
        if delete_name in data:
            contact.remove(data)
            print(f"{delete_name} is Deleted Successfully")
            found= True
            break
    if not found:
        print("Name not Found. Try Again!")

#Display All Contact
def display_contact():
    print("*=====ALL CONTACTS=====*\n")
    for data in contact:
        print("Name: ",data[0])
        print("Phone Number: ",data[1])
        print("Mail Id: ",data[2])
        print("Address: ",data[3])
        print(" ")

#Search for an Contact
def search_contact():
    found=False
    print("*=====SEARCH A CONTACT=====*\n")
    search_value=input("Enter The Name of The Contact: ").capitalize()
    for data in contact:
        if search_value in data:
            print(" ")
            print("Name: ",data[0])
            print("Phone Number: ",data[1])
            print("Mail Id: ",data[2])
            print("Address: ",data[3])
            print(" ")
            found=True
    if found!=True:
        print("Not Found. Try Again!")

#Update an Contact    
def update_contact():
    print("*=====UPDATE A CONTACT=====*\n")
    search_value = input("Enter The Name of The Old Contact: ").capitalize()
    found = False 
    for data in contact:
        if search_value == data[0]:
            new_name = input("Enter New Name (leave blank to keep the same): ") or data[0]
            new_phone = input("Enter New Phone Number (leave blank to keep the same): ")
            new_email = input("Enter New Email (leave blank to keep the same): ") or data[2]
            new_address = input("Enter New Address (leave blank to keep the same): ") or data[3]

            data[0] = new_name
            if new_phone:
                data[1] = int(new_phone)
            data[2] = new_email
            data[3] = new_address

            print("Contact" ,search_value,"Updated Successfully.")
            found = True
            break

    if not found:
        print("Not Found. Try Again!")


#main
print("*=====CONTACT BOOK=====*")
print("1.ADD A NEW CONTACT\n2.SEARCH A CONTACT\n3.UPDATE AN CONTACT\n4.DELETE AN CONTACT\n5.VIEW ALL CONTACT\n6.EXIT")

while True:
    try:
        choice=int(input("\nEnter Your Choice: "))
        match choice:
            case 1:
                add_contact()
            case 2:
                search_contact()
            case 3:
                update_contact()
            case 4:
                delete_contact()
            case 5:
                display_contact()
            case 6:
                print("Closing the Program...")
                break
    except ValueError:
        print("Invalid Choice.Try Again")