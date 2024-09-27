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
print(type(servers_dict)) #check that the server-dict is acc a dict
print(servers_dict) #print the dict to see the difference in the dict format and the str format

json_string = json.dumps(servers_dict, indent=4)  # json.dumps converts the dict to a json formatted string, the indent=4 is an argument that adds an indentation to make it more readable and adds more space inbetween each line of code
print(json_string) #check that the json_string is acc a dict
print(type(json_string))

with open('servers.json', 'w') as json_file:
    json.dump(servers_dict, json_file, indent=4)
    print("\nJSON file 'servers.json' created.")