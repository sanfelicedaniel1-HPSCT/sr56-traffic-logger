import requests

# API endpoint
url = "https://api.openf1.org/v1/car_data?driver_number=55&session_key=9159&speed>=315"

# Send GET request
response = requests.get(url)

# Print entire response payload


print(response.text)

# convert_text = int(text)

# print(convert_text)
