#import this   #an easter egg, it's called PEP 20 python enhance proposals. These are here to help you improve your code
              #theres only 19, so you can come up w your own last own

#import random
#print(random.random())  #prints between 0-1. ".random()" is b
#print(random.randrange(1, 2))

#from random import random #you can impoort from the random modules using the random(), so you dont have to do random.random()
#print(random())

#import math    #inmprt from math module
#num_float = 23.66  #set the variable
#print(math.ceil(num_float))
#print(math.floor(num_float))
#print(math.pi)
# gives us remainder of the 2 values# 5 can't go into 1, so the remainder is 1print(f"Remainder from 1/5: {math.remainder(1, 5)}")


#import os

# returns our current working director
#working_directory = os.getcwd()
#print(f"Current working directory: {working_directory}") #gets the current working direc
#username = os.environ.get('USERNAME') or os.environ.get('USER') #checks for the username from linux and if it can't find, then it checks windows
#print(f"The current user is: {username}") #username found from the enivironment variable
#cpu_cores = os.cpu_count()
#print(f'Total CPU cores: {cpu_cores}')
# change directory - must exist
# os.chdir("<folder_name>")
# make a new directory
# os.mkdir("<folder_name>")


#import datetime  # gives us today's date
#print(f"Today's date: {datetime.date.today()}")


#import datetime  # gives us today's date AND time
#print(f"Today's date: {datetime.datetime.now()}")


# find out built in functions, you dont have to import
#import builtins

#for name in dir(builtins):
#    if name[0].islower():
#        print(name)


#use PIP to install libraries and modules on a command line