import os
import sys
import json

import yaml

if len(sys.argv) > 1:
    # Check if the file exists
    if os.path.exists(sys.argv[1]):
        # Open the file for reading
        file = open(sys.argv[1], "r")
        try:
            # Parse the JSON file - if it loads, then the file contains valid JSON
            yaml.safe_load(file)
            print("YAML file is valid!")
        except yaml.YAMLError as exc:
            print("ERROR: The file contains invalid YAML.")
        finally:
            file.close()
    else:
        # Alert the user that the specified file does not exist
        print(f"ERROR: File '{sys.argv[1]}' not found")
else:
    print("ERROR: No YAML file was specified to check")
    print(f"Usage: {sys.argv[0]} <YAML filename>")
