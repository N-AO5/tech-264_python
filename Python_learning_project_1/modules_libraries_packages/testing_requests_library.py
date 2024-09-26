import requests

request_bbc = requests.get("https://www.bbc.co.uk/")  # contact the bbc library
print(request_bbc.status_code)  #find out the status code
print(request_bbc.content)  #find out the raw content from that url