def division(a : int = 4, b : int = 6) ->float: #the arrow tells you the return should be a float #you can also use --> int| float for both an int and float
    return a/b  #the definition above defines the argument to have a default value of =6 or =4
a: int = 4  #defines the variables as an int too
b: int = 6
print(division(a, b ))