import requests
print ("Request URL: https://avito.ru")
r = requests.get("https://avito.ru")
print ("Getting status code from: https://avito.ru")
print ("Status code is: ", r.status_code)

