import requests

response = requests.get("https://api.github.com")
response.content


type(response.content)