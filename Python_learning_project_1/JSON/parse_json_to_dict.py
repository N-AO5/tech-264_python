import json
with open("servers.json", "r") as file:   #opens the servers.json file in read mode and it is assigned to the variable file
    servers = json.load(file)             #this parses the JSON content into a dictionary named servers

print({type(servers)})                    #this prints the type of the server
