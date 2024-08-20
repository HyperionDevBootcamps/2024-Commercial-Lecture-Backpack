MENU = """Please select an option below:

1. Add Contact
2. Remove Contact
3. Search Contact
4. Show Contacts

0. Quit
contacts
: """
phonebook = []

def print_contacts(contacts):
    for i, contact in enumerate(contacts, 1):
        print(i, contact.split(",")[0])

def remove_contact(index, contacts):
    if index.isnumeric():
        index = int(index)-1
        if 0 <= index < len(contacts):
            del contacts[index]

def search_contact(name, contacts):
    for contact in contacts:
        if name == contact.split(",")[0]:
            contact_card = "Name: {}\nNumber: {}\nEmail: {}".format(contact.split(",")[0],
                                                                    contact.split(",")[1],
                                                                    contact.split(",")[2])
            print(contact_card)

def main():
    while True:
        user_option = input(MENU)

        # Add contacts
        if user_option == "1":
            data = input("Please enter contact name: ") + ","
            data += input("Please enter contact number: ") + ","
            data += input("Please enter contact email: ")
            phonebook.append(data)
            print("Contact added!")

        # Remove contacts
        elif user_option == "2" and phonebook:
            print("Please select a contact below to remove: ")
            print_contacts(phonebook)
            user_index = input(": ")
            remove_contact(user_index)

        # Search contact
        elif user_option == "3":
            name = input("Please enter the name to search: ")
            search_contact(name, phonebook)

        # Display contacts
        elif user_option == "4":
            print_contacts(phonebook)


if __name__ == "__main__":
    main()
