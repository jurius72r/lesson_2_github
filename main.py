import requests
r = requests.get("https://avito.ru")
print(r.status_code)