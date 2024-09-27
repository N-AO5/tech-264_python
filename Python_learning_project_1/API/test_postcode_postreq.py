import requests
import json

#send the api 3 postcodes and get back info from all 3
json_body = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {'Content-Type': 'application/json'}
post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
print(post_multi_req.json())

#results in dict with the info