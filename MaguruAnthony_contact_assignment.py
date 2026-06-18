import re


class ContactManager:
    def __init__(self):
        self.contacts = {}

    # =====================
    # VALIDATION METHODS
    # =====================
    def validate_phone(self, phone):
        return bool(re.fullmatch(r"0\d{9}|\+256-\d{9}", phone))

    def validate_email(self, email):
        if email == "":
            return True

        return "@" in email and "." in email

    # =====================
    # CREATE CONTACT
    # =====================
    def add_contact(self, name, phone, email=""):

        if not self.validate_phone(phone):
            print("Error: Invalid phone number.")
            print("Phone number should be 0712345678 or +256-712345678.")
            return

        if not self.validate_email(email):
            print("Error: Invalid email address.")
            return

        if name in self.contacts:
            print("Error: Contact already exists.")
            return

        self.contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Success: Contact added successfully.")

    # =====================
    # VIEW CONTACT
    # =====================
    def view_contact(self, name):

        if name not in self.contacts:
            print("Error: Contact not found.")
            return

        contact = self.contacts[name]

        print("\n----- Contact Details -----")
        print("Name :", name)
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])

    # =====================
    # UPDATE CONTACT
    # =====================
    def update_contact(self, name, phone=None, email=None):

        if name not in self.contacts:
            print("Error: Contact not found.")
            return

        if phone is not None:

            if not self.validate_phone(phone):
                print("Error: Invalid phone number.")
                return

            self.contacts[name]["phone"] = phone

        if email is not None:

            if not self.validate_email(email):
                print("Error: Invalid email address.")
                return

            self.contacts[name]["email"] = email

        print("Success: Contact updated successfully.")

    # =====================
    # DELETE CONTACT
    # =====================
    def delete_contact(self, name):

        if name not in self.contacts:
            print("Error: Contact not found.")
            return

        del self.contacts[name]

        print("Success: Contact deleted successfully.")

    # =====================
    # SEARCH CONTACTS
    # =====================
    def search_contacts(self, keyword):

        keyword = keyword.lower()
        found = False

        print("\n===== Search Results =====")

        for name, details in self.contacts.items():

            if (
                keyword in name.lower()
                or keyword in details["phone"].lower()
                or keyword in details["email"].lower()
            ):

                found = True

                print("----------------------------")
                print("Name :", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])

        if not found:
            print("No matching contacts found.")

    # =====================
    # LIST ALL CONTACTS
    # =====================
    def list_contacts(self):

        if not self.contacts:
            print("No contacts available.")
            return

        print("\n===== All Contacts =====")

        for name, details in self.contacts.items():

            print("----------------------------")
            print("Name :", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])


# ==================================
# MAIN MENU FUNCTION
# ==================================
def main():

    manager = ContactManager()

    while True:

        print("\n=== CONTACT MANAGER MENU ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        # ADD CONTACT
        if choice == "1":

            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")

            manager.add_contact(name, phone, email)

        # VIEW CONTACT
        elif choice == "2":

            name = input("Enter Contact Name: ")

            manager.view_contact(name)

        # UPDATE CONTACT
        elif choice == "3":

            name = input("Enter Contact Name: ")

            print("Leave blank if you don't want to change a field.")

            phone = input("New Phone: ")
            email = input("New Email: ")

            if phone == "":
                phone = None

            if email == "":
                email = None

            manager.update_contact(name, phone, email)

        # DELETE CONTACT
        elif choice == "4":

            name = input("Enter Contact Name: ")

            manager.delete_contact(name)

        # SEARCH CONTACTS
        elif choice == "5":

            keyword = input("Enter search keyword: ")

            manager.search_contacts(keyword)

        # LIST ALL CONTACTS
        elif choice == "6":

            manager.list_contacts()

        # EXIT
        elif choice == "7":

            print("Thank you for using Contact Manager.")
            break

        else:
            print("Error: Invalid choice. Please select 1-7.")


# ==================================
# PROGRAM STARTS HERE
# ==================================
if __name__ == "__main__":
    main()
    