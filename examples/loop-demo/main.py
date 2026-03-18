names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):
    print(f"Index: {i}, Name: {names[i]}")
    names[i] = ""  # This will actually **modify** the original list


for name in names:
    print(f"Name: {name}")
    name = ""


print("After loop:")
print(names)
