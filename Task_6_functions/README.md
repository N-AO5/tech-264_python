### Task 1: mini calculator using functions

Recommended: Make a 'functions' folder inside your PyCharm project for storing learning about functions. 

Create a Python file called calculator.py and complete a viable basic calculator using functions. 

MVP (each of these should be in a separate function): 

* Can add 2 numbers 
* Can subtract 2 numbers 
* Can multiply 2 numbers 
* Can divide 2 numbers 

````
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
    return a / b
print(divide(1, 2))

#output
3
-1
2
0.5


````
Taking it to the next level: 

* Implement more complex operations, such as handling parentheses, exponentiation 
* More advanced operations should continue to be broken into separate functions 

### Task 2: Re-factor your calculator to use a maths_operations module
Steps:

1. Modify your calculator script so that all arithmetic functions are moved to the python file math_operations.py
2. In your main calculator script, import math_operations so that the functions are accessed in math_operations.py
3. In your main calculator script, modify the calling of the functions so they use the math_operations module

### Task 3: Research what is JSON

Research:

* What does it stand for?

JSON stands for JavaScrips Object Notation

* What is it used for?

JSON is a format used to store and exchange data that is easy for humans to read and write but also easy for machines to understand, It is used to transmit data between a server and a web application or between parts of a programme.

* What is it written in?

It is written in a text format  using JavaScript object syntax, but it is language independent.

* Include a simple example of JSON

````
{ "name":"John", "age":30, "city":"New York"}'
````

* Advantages of using it?


* What data types can it store/use?
* What is the JSON syntax for:
  * Name value pairs?
  * Objects?
  * How to separate data (key/value pairs) from one another?
  * JSON arrays (these are like lists in python)?

