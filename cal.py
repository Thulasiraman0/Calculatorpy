# Hardcoded values (Static variables)
a = 20
b = 4

# Operation Functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error"

# Execution
print("Results:")
print(f"Add:      {add(a, b)}")
print(f"Subtract: {subtract(a, b)}")
print(f"Multiply: {multiply(a, b)}")

print(f"Divide:   {divide(a, b)}")



