filename = input("Enter a filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: file '{filename}' not found.")
except PermissionError:
    print(f"Error: no permission to read '{filename}'.")
except Exception as e:
    print(f"Unexpected error: {e}")

print("End of program.")
