# Lambda Functions in Python

**Understanding Anonymous Functions and Their Practical Applications**  
**A Beginner's Guide to Lambda Expressions**

---

## What Are Lambda Functions?

Lambda functions are small, anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression. The expression is evaluated and returned automatically.

**Syntax:**
```python
lambda arguments: expression
```

**Key Characteristics:**
- Anonymous (no name required)
- Single expression only
- Automatically return the result
- Often used for short, simple operations
- Can be assigned to variables or used inline

---

## Basic Lambda Syntax

### Simple Lambda Function
```python
# Regular function
def add(x, y):
    return x + y

# Equivalent lambda
add_lambda = lambda x, y: x + y

print(add(3, 5))         # 8
print(add_lambda(3, 5))  # 8
```

### Lambda with Single Argument
```python
# Square a number
square = lambda x: x ** 2
print(square(5))  # 25

# Convert to uppercase
uppercase = lambda text: text.upper()
print(uppercase("hello"))  # HELLO
```

### Lambda with Multiple Arguments
```python
# Multiply three numbers
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 24

# Full name formatter
full_name = lambda first, last: f"{first} {last}"
print(full_name("John", "Doe"))  # John Doe
```

### Lambda with No Arguments
```python
# Return a constant value
get_pi = lambda: 3.14159
print(get_pi())  # 3.14159

# Return current timestamp
from datetime import datetime
get_time = lambda: datetime.now()
print(get_time())  # Current date and time
```

---

## Lambda vs Regular Functions

### When to Use Lambda
✅ **Use Lambda When:**
- Function is simple and used once
- Passing a function as an argument
- Creating quick transformations
- Function fits on one line

```python
# Good use of lambda
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
```

### When to Use Regular Functions
✅ **Use Regular Function When:**
- Function has multiple statements
- Function is reused multiple times
- Function needs documentation
- Function logic is complex

```python
# Better as regular function
def calculate_bmi(weight, height):
    """Calculate Body Mass Index."""
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return bmi, "Underweight"
    elif bmi < 25:
        return bmi, "Normal"
    else:
        return bmi, "Overweight"
```

---

## Common Use Cases

### 1. With `map()` Function

Transform each item in a sequence.

```python
# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Convert all to uppercase
names = ["alice", "bob", "charlie"]
upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# Format prices
prices = [10.5, 20.75, 5.99]
formatted = list(map(lambda p: f"${p:.2f}", prices))
print(formatted)  # ['$10.50', '$20.75', '$5.99']
```

### 2. With `filter()` Function

Keep only items that meet a condition.

```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter short words
words = ["hi", "hello", "hey", "greetings"]
short_words = list(filter(lambda w: len(w) <= 3, words))
print(short_words)  # ['hi', 'hey']

# Filter positive numbers
numbers = [-5, 3, -2, 8, -1, 7]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)  # [3, 8, 7]
```

### 3. With `sorted()` Function

Custom sorting logic.

```python
# Sort by absolute value
numbers = [-5, 2, -8, 3, -1]
sorted_abs = sorted(numbers, key=lambda x: abs(x))
print(sorted_abs)  # [-1, 2, 3, -5, -8]

# Sort people by age
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_people = sorted(people, key=lambda p: p["age"])
print(sorted_people)
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Sort strings by length
words = ["apple", "pie", "banana", "kiwi"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)  # ['pie', 'kiwi', 'apple', 'banana']
```

### 4. With `reduce()` Function

Accumulate values into a single result.

```python
from functools import reduce

# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Find maximum
numbers = [5, 2, 8, 1, 9, 3]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 9

# Multiply all numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120
```

---

## Practical Examples

### Example 1: Data Transformation
```python
# Convert temperature data
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

### Example 2: Filtering User Data
```python
users = [
    {"name": "Alice", "age": 28, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 32, "active": False},
    {"name": "Diana", "age": 25, "active": True}
]

# Get active adult users
adult_active = list(filter(lambda u: u["age"] >= 18 and u["active"], users))
print([u["name"] for u in adult_active])  # ['Alice', 'Diana']
```

### Example 3: Custom Sorting
```python
# Sort files by extension then name
files = ["report.pdf", "image.jpg", "data.csv", "photo.jpg", "notes.pdf"]
sorted_files = sorted(files, key=lambda f: (f.split('.')[-1], f.split('.')[0]))
print(sorted_files)
# ['data.csv', 'image.jpg', 'photo.jpg', 'notes.pdf', 'report.pdf']
```

### Example 4: Event Handling
```python
# Button click handlers (conceptual example)
buttons = {
    "submit": lambda: print("Form submitted!"),
    "cancel": lambda: print("Action cancelled"),
    "help": lambda: print("Opening help...")
}

buttons["submit"]()  # Form submitted!
buttons["help"]()    # Opening help...
```

---

## Lambda with Conditional Expressions

Lambda functions can include conditional expressions (ternary operators).

```python
# Check if even or odd
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(4))  # Even
print(check_even(7))  # Odd

# Get absolute value
absolute = lambda x: x if x >= 0 else -x
print(absolute(-5))   # 5
print(absolute(3))    # 3

# Grade classifier
grade = lambda score: "Pass" if score >= 60 else "Fail"
print(grade(75))  # Pass
print(grade(45))  # Fail

# Nested conditional
classify = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
print(classify(5))   # positive
print(classify(-3))  # negative
print(classify(0))   # zero
```

---

## Lambda with Default Arguments

Lambda functions can have default argument values.

```python
# Power function with default exponent
power = lambda x, exp=2: x ** exp
print(power(5))      # 25 (5^2)
print(power(5, 3))   # 125 (5^3)

# Greeting with default name
greet = lambda name="Guest": f"Hello, {name}!"
print(greet())           # Hello, Guest!
print(greet("Alice"))    # Hello, Alice!

# Format with default currency
format_price = lambda amount, symbol="$": f"{symbol}{amount:.2f}"
print(format_price(99.9))       # $99.90
print(format_price(99.9, "€"))  # €99.90
```

---

## Common Patterns and Idioms

### Pattern 1: Immediate Invocation
```python
# Call lambda immediately (IIFE - Immediately Invoked Function Expression)
result = (lambda x, y: x * y)(5, 3)
print(result)  # 15

# Useful for initialization
config = (lambda: {"host": "localhost", "port": 8080})()
print(config)  # {'host': 'localhost', 'port': 8080}
```

### Pattern 2: Creating Functions with Functions
```python
# Function factory using lambda
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### Pattern 3: Lambda in List Comprehensions
```python
# Apply different functions to values
operations = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
number = 5
results = [op(number) for op in operations]
print(results)  # [6, 10, 25]
```

### Pattern 4: Dictionary of Operations
```python
# Calculator using lambda
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Error: Division by zero"
}

print(operations["+"](10, 5))  # 15
print(operations["*"](10, 5))  # 50
print(operations["/"](10, 0))  # Error: Division by zero
```

---

## Best Practices

### ✅ DO

**Keep it Simple**
```python
# Good: Simple and readable
evens = filter(lambda x: x % 2 == 0, numbers)
```

**Use for Short Operations**
```python
# Good: One-time transformation
prices = map(lambda x: x * 1.1, base_prices)
```

**Use as Arguments**
```python
# Good: Sorting key
sorted_names = sorted(names, key=lambda n: n.lower())
```

### ❌ DON'T

**Don't Make Complex Lambdas**
```python
# Bad: Too complex for lambda
result = lambda x: x * 2 if x > 0 else x / 2 if x < 0 else 0 if x == 0 else None

# Better: Use regular function
def process_value(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return x / 2
    else:
        return 0
```

**Don't Assign Lambdas for Reuse**
```python
# Bad: Named lambda defeats the purpose
calculate_tax = lambda amount: amount * 0.08

# Better: Use def
def calculate_tax(amount):
    return amount * 0.08
```

**Don't Use for Multiple Statements**
```python
# Impossible: Lambda can't have multiple statements
# This won't work:
# process = lambda x: (
#     y = x * 2
#     return y + 1
# )

# Use regular function instead
def process(x):
    y = x * 2
    return y + 1
```

---

## Performance Considerations

Lambda functions have similar performance to regular functions. The choice between them should be based on readability, not performance.

```python
import timeit

# Regular function
def square_func(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

# Performance is nearly identical
func_time = timeit.timeit(lambda: square_func(5), number=1000000)
lambda_time = timeit.timeit(lambda: square_lambda(5), number=1000000)

print(f"Function: {func_time:.4f}s")
print(f"Lambda: {lambda_time:.4f}s")
# Both will be very similar
```

---

## Common Mistakes to Avoid

### Mistake 1: Attempting Multiple Statements
```python
# ❌ Wrong: Lambda can't have multiple statements
# process = lambda x: x *= 2; return x

# ✅ Correct: Use regular function
def process(x):
    x *= 2
    return x
```

### Mistake 2: Variable Scope Issues
```python
# ❌ Problem: Late binding
functions = [lambda: i for i in range(5)]
results = [f() for f in functions]
print(results)  # [4, 4, 4, 4, 4] - all reference the same 'i'

# ✅ Solution: Use default argument
functions = [lambda i=i: i for i in range(5)]
results = [f() for f in functions]
print(results)  # [0, 1, 2, 3, 4] - correct
```

### Mistake 3: Forgetting Parentheses
```python
# ❌ Wrong: Prints the lambda object
greet = lambda name: f"Hello, {name}"
print(greet)  # <function <lambda> at 0x...>

# ✅ Correct: Call the lambda
print(greet("Alice"))  # Hello, Alice
```

### Mistake 4: Overcomplicating
```python
# ❌ Convoluted: Hard to read
result = (lambda x: (lambda y: x + y))(5)(3)

# ✅ Clear: Use regular functions or just calculate
result = 5 + 3
```

---

## Exercises

### Exercise 1: Basic Lambdas
Write lambda functions for the following:
1. Convert Celsius to Fahrenheit
2. Check if a number is divisible by 3
3. Extract the first character of a string
4. Calculate the area of a circle given radius

<details>
<summary>Solutions</summary>

```python
# 1. Celsius to Fahrenheit
celsius_to_f = lambda c: (c * 9/5) + 32
print(celsius_to_f(100))  # 212.0

# 2. Divisible by 3
div_by_3 = lambda n: n % 3 == 0
print(div_by_3(9))  # True

# 3. First character
first_char = lambda s: s[0] if s else ""
print(first_char("Hello"))  # H

# 4. Circle area
import math
circle_area = lambda r: math.pi * r ** 2
print(circle_area(5))  # 78.53981633974483
```
</details>

### Exercise 2: With Built-in Functions
Use lambda with `map()`, `filter()`, and `sorted()`:
1. Filter numbers greater than 50 from `[23, 65, 19, 90, 45, 78]`
2. Convert all temperatures in `[20, 25, 30]` from Celsius to Fahrenheit
3. Sort words by last letter: `["apple", "banana", "kiwi", "orange"]`

<details>
<summary>Solutions</summary>

```python
# 1. Filter numbers > 50
numbers = [23, 65, 19, 90, 45, 78]
filtered = list(filter(lambda x: x > 50, numbers))
print(filtered)  # [65, 90, 78]

# 2. Convert temperatures
celsius = [20, 25, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  # [68.0, 77.0, 86.0]

# 3. Sort by last letter
words = ["apple", "banana", "kiwi", "orange"]
sorted_words = sorted(words, key=lambda w: w[-1])
print(sorted_words)  # ['banana', 'orange', 'apple', 'kiwi']
```
</details>

### Exercise 3: Practical Application
Create a lambda-based system to process student records:
```python
students = [
    {"name": "Alice", "grade": 85, "age": 20},
    {"name": "Bob", "grade": 92, "age": 19},
    {"name": "Charlie", "grade": 78, "age": 21},
    {"name": "Diana", "grade": 95, "age": 20}
]
```

Tasks:
1. Filter students with grade >= 90
2. Sort by grade (highest first)
3. Extract just the names

<details>
<summary>Solutions</summary>

```python
students = [
    {"name": "Alice", "grade": 85, "age": 20},
    {"name": "Bob", "grade": 92, "age": 19},
    {"name": "Charlie", "grade": 78, "age": 21},
    {"name": "Diana", "grade": 95, "age": 20}
]

# 1. Filter grade >= 90
high_achievers = list(filter(lambda s: s["grade"] >= 90, students))
print(high_achievers)
# [{'name': 'Bob', 'grade': 92, 'age': 19}, {'name': 'Diana', 'grade': 95, 'age': 20}]

# 2. Sort by grade (highest first)
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
print(sorted_students)
# [{'name': 'Diana', 'grade': 95, ...}, {'name': 'Bob', 'grade': 92, ...}, ...]

# 3. Extract names
names = list(map(lambda s: s["name"], students))
print(names)  # ['Alice', 'Bob', 'Charlie', 'Diana']
```
</details>

---

## Summary

**Key Takeaways:**
- Lambda functions are anonymous, single-expression functions
- Use `lambda arguments: expression` syntax
- Perfect for simple operations with `map()`, `filter()`, `sorted()`
- Keep lambdas simple and readable
- Use regular functions for complex logic
- Common with functional programming patterns

**When to Choose Lambda:**
- One-time use
- Simple transformation
- Function as argument
- Fits comfortably on one line

**When to Choose Regular Function:**
- Multiple statements needed
- Complex logic
- Needs documentation
- Reused multiple times
- Debugging required

---

## Additional Resources

**Related Topics:**
- List comprehensions (often cleaner than `map()` and `filter()`)
- Generator expressions
- Functional programming in Python
- The `functools` module
- Higher-order functions

**Next Steps:**
- Practice with `map()`, `filter()`, and `sorted()`
- Explore list comprehensions as alternatives
- Learn about closures and function factories
- Study functional programming principles

---

*This guide is part of the Python Programming for Beginners course materials.*
