contact = {
    "name": "Alice",
    "email": "alice@example.com",
    "phone": "+36 30 123 4567",
    "age": 30
}

# a) Not safe access, can cause KeyError if the key does not exist
# a = contact["wpeoriqwpeoriqwpeúr"]
# b) Safe access using get method, returns None if the key does not exist
a = contact.get("nama")


numbers = [1, 2, 3, 4, 5]
# manipulate the list...

if numbers:
    print("The list is not empty.")        





print(a)  # Output: None

x = contact["name"]
y = contact["age"]
contact["name"] = "Bob"
contact["city"] = "New York"
print(x)
print(y)
print(contact["city"])
print(contact)
print("name" in contact)  # Output: True
