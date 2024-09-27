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

json_string = json.dumps(servers_dict, indent=4)  # json.dumps converts the dict to a json formatted string, the indent=4 is an argument that adds an indentation to make it more readable
print(json_string)
