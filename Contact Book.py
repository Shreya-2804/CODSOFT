def display_menu():
    print("\nContact Book Menu:")
    print("1. Add a new contact")
    print("2. Delete a contact")
    print("3. Update a contact")
    print("4. Show all contacts")
    print("5. Search for a contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added successfully.")


def delete_contact(contacts):
    name=input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("This contact does not exit.")


def update_contact(contacts):
    name=input("Enter name to update: ")
    for contact in contacts:
        if contact==name:
            phone=input("Enter the new phone number: ")
            contacts[name]=phone
            print("Contact updated successfully")
            break
        else:
            print("This contact does not exit.")


def show_all_contacts(contacts):
    if not contacts:
        print("\n No contacts available.")
    else:
        print("\nContacts:")
        for name , contacts in enumerate(contacts, start=1):
            print(f"{name}. {contacts}")


def search_contact(contacts):
    name = input("Enter the name to search for: ")
    if name in contacts:
        print(f"Contact found: {name} - {contacts[name]}")
    else:
        print("Contact not found.")


def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_contact(contacts)
        elif choice== '2':
            delete_contact(contacts)
        elif choice=='3':
            update_contact(contacts)
        elif choice == '4':
            show_all_contacts(contacts)
        elif choice == '5':
            search_contact(contacts)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()