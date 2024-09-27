import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1: #the first if checks if anything has been parsed
    # Opening the file
    if os.path.exists(sys.argv[1]): #checking that the first item, argv is the list of the argument, does it exist
        source_file = open(sys.argv[1], "r") #if it exists then itll open the json file
        source_content = json.load(source_file) # #.load used to parse it and make it into a dictionary. source content is the dict version of the json file
        source_file.close()  #the code is manually opening the file so it must manually close it
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

# 1. Convert the JSON to YAML - use yaml library

yaml_data = yaml.dump(source_content)

# 2. Save the YAML into a new file with the name for it received as an argument

# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
#sys.argv is a list of the 3 arguments
if len(sys.argv) > 2: #checking if the arguments list is greater than 2, then the yaml file name has been specified

 if os.path.exists(sys.argv[2]): #check if there is a names yaml find at position 3 of the argument, if there is it prints error
    print(f"ERROR: THE FILE {sys.argv[2]} already exists, CHOOSE A DIFFERENT FILE NAME")

# 2.2 Check the target file doesn't already exist
 else:
    with open(sys.argv[2], "w") as yamal_file:
        yamal_file.write(yaml_data)

# 2.3 If previous conditions not met, then save YAML file
else:
    print(yaml_data)