import json
#Use with to open a file bc if the file in manually opened, you may forget to close, with automatically closes the file
with open("servers.json", "r") as file:   #opens the servers.json file in read mode "w" if you want to edit the file opened and it is assigned to the variable file
    servers = json.load(file)             #this parses the JSON content into a dictionary named servers

print({type(servers)})                    #this prints the type of the server
#print(servers)

for server_key, server_value in servers.items():
    print(server_key, server_value)
