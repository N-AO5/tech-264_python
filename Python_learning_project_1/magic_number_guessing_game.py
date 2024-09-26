# User story 1
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# Define/assign number to a variable called magic_number

magic_number = True
input_count = 0

# Ask user for input
user_guess = input("Guess a number: ")

# Check if this input matches magic_number
while magic_number and input_count < 4 :      # While the magic_number is true and the count of user inputs is less than 5
    magic_number = "2"    #set the correct magic number as 2
    if user_guess == magic_number: print("You guessed the magic number!")
    else:
     print("You guessed the wrong magic number!") # Let the user know if the response was correct or not
    user_guess = input("Guess a number: ")
    input_count += 1


