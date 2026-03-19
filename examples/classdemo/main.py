def add(a, b):
    return a + b


numbers = [1, 2, 3, 4, 5]


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Contact(name={self.name}, email={self.email}, phone={self.phone})"


class Building:
    def __init__(self, address, floors, is_lights_on=False):
        self.address = address
        self.floors = floors
        self.is_lights_on = is_lights_on
        self.color = "white"
        self.qweqwe = ""

    def toggle_lights(self):
        self.is_lights_on = not self.is_lights_on

    def paint(self, color):
        self.color = color
    
    def __str__(self):
        return f"Building(address={self.address}, floors={self.floors}, is_lights_on={self.is_lights_on}, color={self.color})"        


a = Contact("John Doe", "john.doe@example.com", "123-456-7890")
b = Contact("Jane Smith", "jane.smith@example.com", "987-654-3210")

x = Building("123 Main St", 5)
y = Building("456 Elm St", 3, True)
x.paint("blue")
y.paint("red")

x.color
y.color


add(10, 20)

print(a)
print(b)
