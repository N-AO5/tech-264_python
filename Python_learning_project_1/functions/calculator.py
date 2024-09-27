def add(a: int, b: int) -> int:
    return a + b
print(add(1, 2))

def subtract(a: int, b: int) -> int:
    return a - b
print(subtract(1, 2))

def multiply(a: int, b: int) -> int:
    return a * b
print(multiply(1, 2))

def divide(a: int, b: int) -> float:
    if b != 0:
     return a / b
    else:
        return "Cannot divide by zero!" #the if statement added bc a division by zero isn't possible
print(divide(1, 0))
 # Implement more complex operations, such as handling parentheses, exponentiation

#  More advanced operations should continue to be broken into separate functions
