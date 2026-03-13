# contacts.py - Simple contact book using dictionaries

contacts = {
    "Alice": "+36-20-111-2222",
    "Bob": "+36-30-333-4444",
    "Charlie": "+36-70-555-6666",
}


def show_contacts(book):
    """Display all contacts in a formatted list."""
    if not book:
        print("  (no contacts)")
        return
    for name, phone in sorted(book.items()):
        print(f"  {name:<12} {phone}")
    print(f"\n  Total: {len(book)} contact(s)")


def lookup(book, name):
    """Look up a contact by name using .get() for safe access."""
    phone = book.get(name)
    if phone:
        print(f"  {name}: {phone}")
    else:
        print(f"  '{name}' not found in contacts.")


# Display all contacts
print("=== Contact book ===\n")
show_contacts(contacts)

# Look up contacts
print("\n--- Lookups ---")
lookup(contacts, "Alice")
lookup(contacts, "Diana")

# Add a new contact
print("\n--- Adding Diana ---")
contacts["Diana"] = "+36-20-777-8888"
show_contacts(contacts)

# Update an existing contact
print("\n--- Updating Bob's number ---")
contacts["Bob"] = "+36-30-999-0000"
lookup(contacts, "Bob")

# Remove a contact
print("\n--- Removing Charlie ---")
del contacts["Charlie"]
show_contacts(contacts)

# Safe removal with pop (no error if missing)
print("\n--- Safe removal of 'Eve' (not in contacts) ---")
removed = contacts.pop("Eve", None)
if removed:
    print(f"  Removed Eve: {removed}")
else:
    print("  'Eve' was not in contacts — nothing removed.")
