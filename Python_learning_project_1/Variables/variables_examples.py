#Set a variable with a number value
bananas = 25
#Set a variable a=with a decimal value
Weight = 70.5
#Set a variable with a string value
day = "thursday"
a = 10       # a is an integer
print(type(a))  # Output: <class 'int'>

a = "Hello"  # Now a is a string
print(type(a))  # Output: <class 'str'>

a= 21
print(id(a)) #ID when a=6  - 140721894771288
             #ID when a =21 -140721894771768




# values
a = 5
b = 1

# 1. Greater than (>)
print(f"Is {a} greater than {b}? ->", a > b)  # Output: False

# 2. Less than (<)
print(f"Is {a} less than {b}? ->", a < b)  # Output: True

# 3. Equal to (==)
print(f"Is {a} equal to {b}? ->", a == b)  # Output: False

# 4. Not equal to (!=)
print(f"Is {a} not equal to {b}? ->", a != b)  # Output: True

# 5. Greater than or equal to (>=)
print(f"Is {a} greater than or equal to {b}? ->", a >= b)  # Output: False

# 6. Less than or equal to (<=)
print(f"Is {a} less than or equal to {b}? ->", a <= b)  # Output: True

z = bool(None)
print(z)


x = None

if x is None:
    print("x is None")
else:
    print("x is not None")

# find out if 'hi' is made up of letters only (use one of the strings methods) - print the boolean to the screen
hi = "Hello world!"
print(hi.startswith("H"))


