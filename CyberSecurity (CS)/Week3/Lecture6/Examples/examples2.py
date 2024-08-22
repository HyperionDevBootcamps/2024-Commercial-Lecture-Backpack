class Contact:

    def __init__(self, name, number, email=""):
        self.name = name
        self.number = number
        self.email = email

    @property
    def contact_card(self):
        return "Name: {}\nNumber: {}\nEmail: {}".format(self.name, self.number, self.email)

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
        print(i, contact.name)

def remove_contact(index, contacts):
    if index.isnumeric():
        index = int(index)-1
        if 0 <= index < len(contacts):
            del contacts[index]

def search_contact(name, contacts):
    for contact in contacts:
        if name == contact.name:
            print(contact.contact_card)

def main():
    while True:
        user_option = input(MENU)

        # Add contacts
        if user_option == "1":
            name = input("Please enter contact name: ")
            number = input("Please enter contact number: ")
            email = input("Please enter contact email: ")
            contact = Contact(name, number, email)
            phonebook.append(contact)
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
