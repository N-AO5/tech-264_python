def greet(name: str): #this tells you that the function only accepts strings, the argument is defined as a string
    print("Hello my name is " + name + ".")

greet(name="susan")

greet(24601) # the argument is defined as a sting so when the yellow line appears under the parameter to hint that it wants a str