class Contact:
    # Initialize the Contact class with name, email, and phone attributes
    # constructor method to set the attributes when a new Contact object is created
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def validate_email(self):
        # Simple email validation: check if it contains "@" and "."
        if "@" in self.email and "." in self.email:
            return True
        return False

    def __str__(self):
        return f"Contact(name={self.name}, email={self.email}, phone={self.phone})"


# same data with dictionary:
contact_d1 = {"name": "Alice",
              "email": "alice@example.com", "phone": "123-456-7890"}
contact_d2 = {"name": "Bob",
              "email": "bob@example.com", "phone": "987-654-3210"}

contact1 = Contact("Alice", "alice@example.com", "123-456-7890")
contact2 = Contact("Bob", "bob@example.com", "987-654-3210")
contact2.validate_email()

contact1.name = "Alice X"
contact1.email = "alice.x@example.com"
contact1.validate_email()


x = contact1.name
print(f"Name: {contact1.name}")
print(f"Email: {contact1.email}")
print(f"Phone: {contact1.phone}")

print(f"Name: {contact2.name}")
print(f"Email: {contact2.email}")
print(f"Phone: {contact2.phone}")

print(contact1)
