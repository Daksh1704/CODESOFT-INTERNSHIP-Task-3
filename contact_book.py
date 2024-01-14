class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"\nContact added: {contact.name}\n")

    def view_contact_list(self):
        if not self.contacts:
            print("\nContact book is empty.\n")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone_number]
        if results:
            print("\nSearch Results:")
            for result in results:
                print(f"Name: {result.name}, Phone: {result.phone_number}")
        else:
            print(f"\nNo contacts found with '{keyword}'.\n")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                new_phone = input("Enter the new phone number: ")
                new_email = input("Enter the new email: ")
                new_address = input("Enter the new address: ")

                contact.phone_number = new_phone
                contact.email = new_email
                contact.address = new_address

                print(f"\nContact updated for {contact.name}\n")
                return

        print(f"\nContact not found with the name {name}.\n")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"\nContact deleted: {contact.name}\n")
                return

        print(f"\nContact not found with the name {name}.\n")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            keyword = input("Enter the name or phone number to search: ")
            contact_book.search_contact(keyword)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            contact_book.update_contact(name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
