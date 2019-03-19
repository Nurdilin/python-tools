import requests
import json
import string

r = requests.get('http://ip.addr.es')
print("Response object:",r)
#print("\n")
print("Status Code:", r.status_code)
#print("Response text:",r.text)
#print("Response text json:", r.json())
#r.status_code - Returns the response code
#r.json() - Converts the response to .json format
#r.text - Returns the response data for the query
#r.content- Includes the HTML and XML tags in the response content
#r.url - Defines the Web URL of the request made

#get_payload = {'q': 'chetan'}
#r = requests.get('https://github.com/search', params=get_payload)
#print("Response object:",r)
#print("Response text:",r.text)
#print("Request URL:",r.url)
#print("Response text json:", r.json())


post_payload = {'key1': 'value1'} 
try:
    r = requests.post('http://httpbin.org/post', data=post_payload)
except requests.exceptions.RequestException as e:
    print("Error Repsonse:", e.message)    

#print("Response object:",r)
#print("Response text:",r.text)
#print("Request URL:",r.url)
#print("Response text json:", r.json())




