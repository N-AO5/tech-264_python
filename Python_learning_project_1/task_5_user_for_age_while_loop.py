# Ask user for their age
user_prompt = True     # SET VARIABLE TO TRUE, this controls the loop

while user_prompt:            #the loop will continue as long as user_prompt is True
 age = input("What is your age? ")
 if age.isdigit():                              # this checks that the input age is all digits, if it is the user prompt is set to False
     user_prompt = False
     print(f"Your age is {age}")  # SET user_prompt TO FALSE
 else:                                                  # ADD ELSE STATEMENT HERE
    print("Please enter a valid age")        # TELL USER THE PROBLEM WITH THEIR INPUT if the input isn't all digits


