import requests

url = "https://idika.onrender.com/amka/lookup"

payload = {"amka": "01017012345"}

response = requests.post(url, json=payload)
print(response.json())
