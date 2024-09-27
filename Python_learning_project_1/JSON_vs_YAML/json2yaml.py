import json
import os
import sys
import yaml

source_content = ""
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
if len(sys.argv) > 2: #checking if the arguments list is greater than 2, then the yaml file name has been specified, there is a yaml that is expected to be made

    if os.path.exists(sys.argv[2]): #check if there is and 3rd argument. Names yaml if there is it prints error, theres no need to name a yaml
        print(f"ERROR: THE FILE {sys.argv[2]} already exists, CHOOSE A DIFFERENT FILE NAME")

# 2.2 Check the target file doesn't already exist
    else: #if isnt a file that file w the name of the 3rd arg then it opens one, "w" means its writng to said file
        with open(sys.argv[2], "w") as yamal_file:
            yamal_file.write(yaml_data) #fills the yaml fill w data from original json file

# 2.3 If previous conditions not met, then save YAML file
else:
    print(yaml_data)