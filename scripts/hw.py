import requests

response = requests.get('https://google.com/')
print(response)
print(response.status_code)
print(response.text)
