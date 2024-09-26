from math_operations import *  #This will import all function from the math_operation module (just a single file) unlike a library which is set of modules
# To import just the add function - from math_operations import add


# Mini-calculator

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")
