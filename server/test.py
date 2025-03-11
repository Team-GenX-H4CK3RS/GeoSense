import requests

response = requests.post(
    "http://landslide.lalithadithyan.online/phone/req/30.285/78.9829", verify=False)
print(response.json())
