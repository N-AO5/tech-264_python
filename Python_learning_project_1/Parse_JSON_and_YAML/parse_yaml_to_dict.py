import yaml
#Use with to open a file bc if the file in manually opened, you may forget to close, with automatically closes the file
with open("valid.yaml", "r") as file:   #opens the valid.json file in read mode "w" if you want to edit the file opened and it is assigned to the variable file
    servers = yaml.safe_load(file)           #this parses the yaml content into a dictionary named servers
                                        #recent PyYaml uses safe.load if you dont want to use custom tags or objects
print({type(servers)})                    #this prints the type of the server
#print(servers)


