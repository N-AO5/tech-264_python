import requests
#using the get method to get a point for this api, the last bit is the post code
#it saves what is learns as variable post_code_req
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req)

print(f"Status code: {post_codes_req.status_code}")  #everything was retuend okay
print(f"Headers: {post_codes_req.headers}") #all the headers
print(f"Content: {post_codes_req.content}") # a dict full of content of the headings
print(f"JSON: {post_codes_req.json()}")
print(f"Data type of JSON: {type(post_codes_req.json())}")

#extract the region involved
#make a dict of the 'result' part into another dict variable
data_dict = post_codes_req.json()['result']
print(f"Region: {data_dict['region']}")

#post req to get info from multiple post codes
