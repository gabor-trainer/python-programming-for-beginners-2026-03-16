def add(x, y):
    result = x + y
    return result


def subtract(x, y):
    result = x - y
    return result


def multiply(x, y):
    result = x * y
    return result


def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    result = x / y
    return result
