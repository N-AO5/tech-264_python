### Task 1: Working with a list 
You are now moving onto ‘collections’. Suggestion: Make a new folder inside the root project folder (or python learning folder) called ‘collections’ to store your work. 

- Write a Python script to: 

   - Create a list called 'shopping_list' with the following items: 
   - eggs 
   - bread 
   - bananas
   - biscuits 
   - milk

- Print the list to the screen 
````
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
print(shopping_list)

#output ['eggs', 'bread', 'bananas', 'biscuits', 'milk']
````
- Print the data type of 'shopping_list' 
````
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
print(type(shopping_list))  #output <class 'list'>
````

- Print the first item in the list 
````
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

print(shopping_list[0]) #output eggs
````
- Print the last item in the list 

````
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

print(shopping_list[-1]) #output milk
````
- Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item to the screen to prove it's been changed 

````
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

shopping_list[1] = "rice"

print(shopping_list)  #output ['eggs', 'rice', 'bananas', 'biscuits', 'milk']

print(shopping_list[1]) #output rice
````

- Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='), then check the length of the list (which should now have 6 rather than 5) 
````
#can insert anywhere in list
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

shopping_list.insert(0, "carrots")
print(shopping_list)  #output ['carrots', 'eggs', 'bread', 'bananas', 'biscuits', 'milk']

shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

#adds straight to the end of the list
shopping_list.append("carrots")

print(shopping_list) #output ['eggs', 'bread', 'bananas', 'biscuits', 'milk', 'carrots']

#the number of items
print(len(shopping_list)) #output 6
````

- Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods to add the two items in one go. 
    - Print the 'shopping_list' to check 'toffee' and 'coffee' have been added correctly. 
````
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

shopping_list.extend(["toffee", "coffee"])

print(shopping_list)  #output ['eggs', 'bread', 'bananas', 'biscuits', 'milk', 'toffee', 'coffee']
````

- Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.

````
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

shopping_list.remove("bananas")

print(shopping_list) # output ['eggs', 'bread', 'biscuits', 'milk']
````

- Remove the last item ('coffee') from 'shopping_list' using the pop method. Check it worked by printing 'shopping_list' 

````
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

shopping_list.pop()

print(shopping_list) # output ['eggs', 'bread', 'bananas', 'biscuits']

#pop() is popping one item of the list and it's alwasy the last one
````

### Task 2: Get name, age and DOB details from user

Write a Python script to:
- Get the user's name, age and DOB.
- Print the user's name, age and DOB to the screen 

If time, see if you can:
- prompt the user and get the input on the same line 
- see if you can print "Hi " on the one line 

````
Name = input("Enter your name: ")
Age = input("Enter your age: ")
DOB = input("Enter your date of birth: ")

#good use of f strings
print(f"Hi {Name} you are {Age} years old and your date of birth is {DOB}")

#output
Enter your name: Anjy
Enter your age: 25
Enter your date of birth: 15/12/98

Hi Anjy you are 25 years old and your date of birth is 15/12/98

````
 
### Task 3: Mix all the data about a user into a list

* Use your code from the "Task: Get name, age and DOB details from a user". 
* Mix the name, age and DOB into one list user_details_list
* Print the user's name, age and DOB from the list 

````
Name = input("Enter your name: ")
Age = input("Enter your age: ")
DOB = input("Enter your date of birth: ")

user_details_list = [Name, Age, DOB]
print(user_details_list)

#output
Enter your name: Anjy
Enter your age: 25
Enter your date of birth: 15/12/98
['Anjy', '25', '15/12/98']
````

* Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list. 
````
Name = input("Enter your name: ")
Age = input("Enter your age: ")
DOB = input("Enter your date of birth: ")

user_details_list = [Name, Age, DOB]

print(type(user_details_list[1])) 

#output
Enter your name: ffdd
Enter your age: 2424
Enter your date of birth: 546464
<class 'str'>

#The age was a string therefore as follows:
Name = input("Enter your name: ")
Age = input("Enter your age: ")
DOB = input("Enter your date of birth: ")

user_details_list = [Name, int(Age), DOB]

print(type(user_details_list[1]))

#output
Enter your name: fsdf
Enter your age: 2323
Enter your date of birth: 2242
<class 'int'>
````

* Ask the user for their height in cm and save it to the variable height 
* Save height as a float in the list, and print the height from the list. 

````
Name = input("Enter your name: ")
Age = input("Enter your age: ")
DOB = input("Enter your date of birth: ")
Height = input("Enter your height(cm): ")

user_details_list = [Name, int(Age), DOB, float(Height)]
print(user_details_list)

#output
Enter your name: Anjy
Enter your age: 25
Enter your date of birth: 12/15/98
Enter your height(cm): 178.6
['Anjy', 25, '12/15/98', 178.6]
````

### Task 4: Finish the "Stranded on a Desert Island" game

Before finishing the game below, answer these questions: 

* How are tuples similar to lists? 

***It can contain different types of data eg. strings, integers etc***

* Are tuples immutable and what does this mean? 

***Immutable means that once it is created the elements can't be changed***

* What other data types are immutable? 

***Strings, floats, integers and frozensets***

* What is a good use case for tuples? 

***The code is locked so that means the code is easier to debug also when working parallelism in your programs eg. coordinates***

What does the following piece of code do? 
``` 

essentials = ("bread", "eggs", "milk") 

print(essentials) 

print(essentials.count("bread")) 

```
***it counts the number of "bread" in the tuple, the output would be 1***
 

Objective 

Practice using tuples. 

The task 

Add your code where it says 'YOUR CODE GOES HERE' 

Starting code: 

``` 

# "Stranded on a Desert Island" game 

# Rationale: Practice tuples 

# Type of exercise: Finish the code 

print("You are stranded on a desert island. You can take only THREE items.") 

essential_item1 = input("What is an essential item you would take? ") 

essential_item2 = input("What is an essential item you would take? ") 

essential_item3 = input("What is an essential item you would take? ") 

# save the items as a tuple 

print("You are stranded on a desert island. You can take only THREE items.")

essential_item1 = input("What is an essential item you would take? ")

essential_item2 = input("What is an essential item you would take? ")

essential_item3 = input("What is an essential item you would take? ")

three_essential_items = (essential_item1, essential_item2, essential_item3)

print(f"Your essential items", three_essential_items)

#output 
You are stranded on a desert island. You can take only THREE items.
What is an essential item you would take? water filter
What is an essential item you would take? lighter
What is an essential item you would take? flare
Your essential items are ('water filter', 'lighter', 'flare')


essentials_tuple = None  # YOUR CODE GOES HERE INSTEAD OF 'None' 

# print the tuple 

print("Here are your items as a tuple:", essentials_tuple) 

print("") 

print("I lied. You can take one more item.") 

essential_item4 = input("What is one more essential item you would take? ") 

# try to add the 4th item to the tuple 

essential_item4 = input("What is one more essential item you would take? ")

three_essential_items.append(essential_item4)
#output AttributeError: 'tuple' object has no attribute 'append'
# if you can't add the 4th item, work out how to save the 4th item to the tuple 

# YOUR CODE GOES HERE 
print("You are stranded on a desert island. You can take only THREE items.")

essential_item1 = input("What is an essential item you would take? ")

essential_item2 = input("What is an essential item you would take? ")

essential_item3 = input("What is an essential item you would take? ")

three_essential_items = (essential_item1, essential_item2, essential_item3)

print(f"Your essential items are", three_essential_items)
print("I lied. You cam take one more item.")

essential_item4 = input("What is one more essential item you would take? ")

four_essential_items = three_essential_items + (essential_item4, ) # makes the essential item 4 into a tuple
four_essential_items = (essential_item1, essential_item2, essential_item3, essential_item4)   # rewrite the whole tuple includeing the new item

print(f"Your essential items are", four_essential_items)

#output
You are stranded on a desert island. You can take only THREE items.
What is an essential item you would take? water filter
What is an essential item you would take? lighter
What is an essential item you would take? flare
Your essential items are ('water filter', 'lighter', 'flare')
I lied. You cam take one more item.
What is one more essential item you would take? rope
Your essential items are ('water filter', 'lighter', 'flare', 'rope')

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple) 

``` 

### Task 5: Working with dictionaries

***A dictionary is a collection made of keys, each of which is associated with a value. Dictionaries are mutable. key-value pairs**

* Make a dictionary called "student_1" containing the following information: 
  * name: susan 
  * stream: tech 
  * completed_lessons: 4 (should be saved as an integer not a string) 
  * completed_lesson_names: value should be list of these 3 items: "variables", "data_types", "set up" 
* Explain how a dictionary saves/structures data? Example, what does each value need to be accompanied/associated with?

***Each value is associated with a key***

* Print the dictionary to the screen 
````
# A dictionary is made using curly brackets
Student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": int(4),
    "completed_lesson_names": ["variables", "data_types", "set up"]

}

print(Student_1)


# output {'name': 'susan', 'stream': 'tech', 'completed_lessons': 4, 'completed_lesson_names': ['variables', 'data_types', 'set up']}

````
* Print it's data type to the screen to check it's a dictionary 

````
print(type(Student_1)) #output <class 'dict'>

````
* Print the value for the key-value pair having the key "stream" 

````
# A dictionary is made using curly brackets
Student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": int(4),
    "completed_lesson_names": ["variables", "data_types", "set up"]

}

print(Student_1["stream"]) #output tech
````

* Print the value for 'completed_lesson_names' - check you can see the list of 3 items 
````
# A dictionary is made using curly brackets
Student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": int(4),
    "completed_lesson_names": ["variables", "data_types", "set up"]

}
print(Student_1["completed_lesson_names"])
output ['variables', 'data_types', 'set up']

````
* print the data type for the value for 'completed_lesson_names' - check it is a list 

```` #output <class 'list'>````

* Print the first element/item in the list of 'completed_lesson_names' (should output "variables") 
````
Student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": int(4),
    "completed_lesson_names": ["variables", "data_types", "set up"]
}

print(Student_1["completed_lesson_names"][0])

#output variables
````

* Change the value of "completed_lessons" to 3 (an integer not string). Make sure you change was successful by printing your dictionary to the screen again. 

````
Student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": int(4),
    "completed_lesson_names": ["variables", "data_types", "set up"]
}

Student_1["completed_lessons"] = 3
print(Student_1)

#output {'name': 'susan', 'stream': 'tech', 'completed_lessons': 3, 'completed_lesson_names': ['variables', 'data_types', 'set up']}

````
* Delete "data_types" from the list under the key 'completed_lesson_names' 

````
Student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": int(4),
    "completed_lesson_names": ["variables", "data_types", "set up"]
}

Student_1["completed_lesson_names"].remove("data_types")
print(Student_1)

#output {'name': 'susan', 'stream': 'tech', 'completed_lessons': 4, 'completed_lesson_names': ['variables', 'set up']}

````
* Use the keys() method on your dictionary to list all the keys 

### Task 6: Using sets

Objective 

Practice creating sets, adding and removing elements, and understanding the properties of sets. 

The task 

* Explain 2 main ways that sets are different to lists and tuples 

***Sets are unordered, unlike lists and tuple. Sets are mutable unlike tuples. Sets cannot have duplicated items***

* Create a set named 'fruits' containing "apple", "banana", and "cherry".
* Print the set 'fruits' 

````
fruits_set = { "apple", "banana", "cherry"}

print(fruits_set)

#output {'banana', 'apple', 'cherry'}

````

* Add "orange" to the fruits set using one of the set's methods. 
* Print the set 'fruits' - check it's added 

````
fruits_set = { "apple", "banana", "cherry"}
fruits_set.add("orange")
print(fruits_set)

#outcome {'cherry', 'orange', 'apple', 'banana'}

````
* Remove "banana" from the fruits set using one of the set's methods. 
* Print the set 'fruits' - check it's removed 

````
fruits_set = { "apple", "banana", "cherry"}
fruits_set.remove("banana")

#can also use .discard("banana")
print(fruits_set)

#outcome {'apple', 'cherry'}
````

* Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen? 

***the set does not print out two separate apples because sets do not have duplicates***

* Print the final fruits set. 
````
fruits_set = { "apple", "banana", "cherry"}
fruits_set.add("apple")
print(fruits_set)

#outcome {'cherry', 'banana', 'apple'}
````

* Print the 2nd item in the set. If there is any problem doing this, explain. 
 
***sets do not have a set order, they don't have indexing so there is no second item***

### Task 7: Using frozen sets

Objective 

Understand the concept and usage of immutable sets (frozen sets). 

The task
* Create a frozen set named frozen_set containing elements "hello", "world".

````
set = {"hello", "world"}
frozen_set = frozenset(set)

print(frozen_set) #output frozenset({'world', 'hello'})
````

* Try to add "!" to frozen_set. What happens? 

***the "!" isn't added to the frozen set***

* Create a normal set named normal_set containing elements "let's", "learn". 
* Try to add frozen_set to normal_set. Why does it work? Explain. 

***the frozen set is added as a separate element within the normal set***

* Print normal_set. 

````
set = {"hello", "world"}
frozen_set = frozenset(set)

normal_set = {"let's", "learn"}
normal_set.add(frozen_set)

print(normal_set)

#outcome {frozenset({'world', 'hello'}), "let's", 'learn'}
````

* Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items. 

***the frozen set moves around with th normal st as the order rearranges in the normal set but the order of the items in the frozen set remain the same***

* What makes a frozen set different to a normal set? Explain.

***the order of the items within the frozen set remain the same***

***lists and dictionaries are used the most, the rest are used for specific requirements***

### If time task 1: Waiter helper
Rationale: To practice lists
Script should act like a waiter at a restaurant taking orders

level 1

Greet the user

Print a list of starters

Take an input for the user for their starter

Print a list of mains

Take an input for the user for their main course

Print a list of desserts

Take an input for the user for their dessert

Print all the user's choices
````
print("Hello, what would you like as a starter?")
starter_list = ["cheese platter", "tomato soup", "bread and hummus"]
print(starter_list)
user_input_1 = input("what would you like to start with? ")

mains_list = ["burrito", "lasagne", "roast"]
print(mains_list)
user_input_2 = input("what would you like as a main? ")

dessert_list = ["carrot cake", "apple crumble", "eton mess"]
print(dessert_list)
user_input_3 = input("what would you like for dessert? ")

print (user_input_3, user_input_2,  user_input_1)

#output 
Hello, what would you like as a starter?
['cheese platter', 'tomato soup', 'bread and hummus']
what would you like to start with? cheese platter
['burrito', 'lasagne', 'roast']
what would you like as a main? roast
['carrot cake', 'apple crumble', 'eton mess']
what would you like for dessert? carrot cake
carrot cake roast cheese platter
````

# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'

# level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.

# level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.
````

### If time task 2: Write a "Hero story" python script 

Summary 

* Write a Python script to write a 'Hero story' 

Purpose 

* Practice what you've learnt about Python dictionaries 

The task 

First part 

* Define a dictionary called story1. It should have the following keys: 
* 'start', 'middle' and 'end' 
* Print the entire dictionary 
* Print the type of your dictionary 
* Print only the keys 
* Print only the values 
* Print the individual values using the keys (individually, lots of print commands) 
* Now, let's add a new key:value pair: 
* 'hero': yourSuperHero

Hints: 

* THE MORE CREATIVE THE BETTER 

If time 

Improve the program. For example, can you make it a "Choose your own adventure" story? 

### If time task 3: Password manager

````
# Create a program that is a mini password manager
# You will practice using dictionaries

# First, setup the ability for one user to login to the account manager using a username + password

# Once logged in, they should be able to store a usernames and passwords for different 
#  accounts so they don't need to remember all their passwords
#  For example, for Facebook, email account, etc

# Once the storage is setup, add the ability to add new users to the account manager
#  (they will each need a username + password)

# Add the ability to retrieve the username and password for a specific account
#  if they input the account name e.g. hotmail

# If time - Can you make it so you need to enter the user's password before they can change it to something else?

````
