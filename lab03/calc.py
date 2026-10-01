def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a, operation, b = input().split()

a = float(a)
b = float(b)

if operation == "+":
    print(add(a, b))
elif operation == "-":
    print(subtract(a, b))
elif operation == "*":
    print(multiply(a, b))
elif operation == "/":
    if b != 0:
        print(divide(a, b))
    else:
        print("Cannot divide by zero")
else:
    print("Unknown operation")

