def add(a, b):
    return a + b

a, operation, b = input().split()

a = float(a)
b = float(b)

if operation == "+":
    print(add(a, b))

