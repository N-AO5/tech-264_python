from math_operations import *  #This will import all function from the math_operation module (just a single file) unlike a library which is set of modules
# To import just the add function - from math_operations import add

# Mini-calculator
print(["1 = Add", "2 = Subtract", "3 = Multiply", "4 = Divide"])
user_input = input("Enter a number for which operation you'd like to use (1-4):  ")


first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = subtract(first_num, second_num)
print(f"{first_num} - {second_num} = {result}")

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = multiply(first_num, second_num)
print(f"{first_num} * {second_num} = {result}")

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = divide(first_num, second_num)
print(f"{first_num} / {second_num} = {result}")