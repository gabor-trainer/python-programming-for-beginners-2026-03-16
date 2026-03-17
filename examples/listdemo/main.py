numbers = [11, 20, 35, 4, 5]
x = numbers[:]

numbers.append(100)

n1 = numbers[-1]
n2 = numbers.pop()

print(len(x))
print(n1)
print(n2)

fruits = ["apple", "banana", "cherry"]
# for each fruit in fruits:
for fruit in fruits:
    fruit = fruit.upper()
    print(fruit)

for fruit in fruits:
    print(fruit)

# original |||
# upper |||||
