coordinates = (10.5, 20.3)
print(coordinates[0])      # 10.5
print(len(coordinates))    # 2

person = ("Alice", 28, "Budapest")
name, age, city = person

person2 = name, age, city

print(person)
print(person2)


# TypeError: 'tuple' object does not support item assignment
# coordinates[0] = 99.9
