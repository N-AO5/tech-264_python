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
    if b != 0:
     return a / b
    else:
        return "Cannot divide by zero!" #the if statement added bc a division by zero isn't possible
print(divide(1, 0))
 # Implement more complex operations, such as handling parentheses, exponentiation

#  More advanced operations should continue to be broken into separate functions

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

  - it is easy for humans to read - file opens in plain text
  - it is language independent - programming languages have libraries so it supports JSON
  - easy for machines to convert JSON to other data types
  

* What data types can it store/use?

  - strings
  - numbers
  - lists but must be saved within a key value pair
  - key-value pairs
  - boolean statements

* What is the JSON syntax for:
  * Name value pairs? ```` "name": "values" ````
  * Objects? ```` { "key1": "value1"} ````
  * How to separate data (key/value pairs) from one another? u2sing a comma ","
  * JSON arrays (these are like lists in python)? ```` ["item1", "item2"]

***differences between dictionaries and the JSON format***

### Task 4: Convert a Python dictionary into a JSON-formatted string and a JSON file

Research:

What is encoding vs serialising (very quick, two or three dot points to understand the difference)
Work out which one of them are you doing with the subtasks below

- Encoding is converting data from one format to another
- Serializing is converting a data structure (eg. object and lists) into a format that can be stored and transmitted but then restructured later. 
- The result is a byte stream or a string that represents the original data structure

Starting code:

````
# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

````
Subtasks:

* Convert this Python dictionary into a JSON-formatted string
* Convert this Python dictionary to a JSON file

````
# create the dictionary

import json     #import the json module
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

json_string = json.dumps(servers_dict, indent=4)  # json.dumps converts the dict to a json formatted string, the indent=4 is an argument that adds an indentation to make it more readable
print(json_string)

#output
{
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

````
Extra guidance:

* Use the json library
* Write any other code necessary to test things converted correctly
* Use Gen AI (ChatGPT or Google Gemini) to help speed up this task as much as you need to.  However what's important is that:
* You made sure you come up with a simple version of code that you understand rather than some complex code it might generate for you
* Make sure you get your head around what your code does + add your own comments to explain each part of the code

### Task 5: Convert JSON file to Python dictionary


Use Gen AI (ChatGPT or Google Gemini) to help speed up this task as much as you need to.  However what's important is that:
You made sure you come up with a simple version of code that you understand rather than some complex code it might generate for you
Make sure you get your head around what your code does + add your own comments to explain each part of the code


Steps:

Create a new file servers.json and add this JSON to it:
````
{
	"server1": {
		"hostname": "web-server-1",
		"ip_address": "192.168.1.1",
		"role": "web",
		"status": "active"
	},
	"server2": {
		"hostname": "db-server-1",
		"ip_address": "192.168.1.2",
		"role": "database",
		"status": "maintenance"
	}
}
````
Create a file called parse_json_to_dict.py and add code to it to: Steps:

* Use 'with' to open the file created above

* Parse contents the JSON file into a Python dictionary named "servers"

* Print out the type of "servers"

* Print out the dictionary record with the key "server1"

* Print out the dictionary record with the key "server2"

* Print all of the keys and values. Output should be:

Key and value: 'server1' = '{'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}'
* Record key and sub value: 'hostname' = 'web-server-1'
* Record key and sub value: 'ip_address' = '192.168.1.1'
* Record key and sub value: 'role' = 'web'
* Record key and sub value: 'status' = 'active'

Key and value: 'server2' = '{'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}'
* Record key and sub value: 'hostname' = 'db-server-1'
* Record key and sub value: 'ip_address' = '192.168.1.2'
* Record key and sub value: 'role' = 'database'
* Record key and sub value: 'status' = 'maintenance'

Extra guidance:
Use Gen AI (ChatGPT or Google Gemini) to help speed up these tasks as much as you need to

### Validate JSON folder 
see validate_json_file.py

use terminal on pycharm to cd into the direc w the see validate_json_file.py
type in terminal:  python .\validate_json_file.py .\servers.json
python. whatever direc then file you want to validate
pytho

