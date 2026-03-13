# string_methods.py - Exploring string methods

# Cleaning input
raw_input = "   Alice Johnson   "
cleaned = raw_input.strip()
print(f"Original:  {raw_input}]")
print(f"Stripped:  [{cleaned}]")
print()

# Case conversion
name = "alice JOHNSON"
print(f"lower:  {name.lower()}")
print(f"upper:  {name.upper()}")
print(f"title:  {name.title()}")
print()

# Splitting and joining
csv_line = "Budapest,Hungary,1.7 million,47.4979,19.0402"
fields = csv_line.split(",")
print(f"Fields: {fields}")
print(f"City: {fields[0]}")
print(f"Country: {fields[1]}")

# Rejoin with a different separator
reformatted = " | ".join(fields)
print(f"Reformatted: {reformatted}")
print()

# Searching
email = "alice.johnson@example.com"
at_pos = email.find("@")
username = email[:at_pos]
domain = email[at_pos + 1:]
print(f"Email: {email}")
print(f"Username: {username}")
print(f"Domain: {domain}")
print()

# Replacing
text = "Python is hard. Python is confusing."
updated = text.replace("hard", "readable").replace("confusing", "clear")
print(f"Before: {text}")
print(f"After:  {updated}")
print()

# Counting
paragraph = "the cat sat on the mat and the cat saw the rat"
the_count = paragraph.count("the")
print(f"Text: {paragraph}")
print(f"'the' appears {the_count} times")
