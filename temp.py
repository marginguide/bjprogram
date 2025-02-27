import requests
response = requests.get("https://api64.ipify.org?format=json")
external_ip = response.json()["ip"]
print(external_ip)