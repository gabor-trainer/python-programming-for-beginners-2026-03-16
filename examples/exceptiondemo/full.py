
# a)
f = None
try:
    f = open("data.txt")
    content = f.read()
except FileNotFoundError:
    content = ""
finally:
    if f:
        f.close()
# b)
# Same program using "with" — file is closed automatically
try:
    with open("data.txt") as f:
        content = f.read()
except FileNotFoundError:
    content = ""
