import requests

headers ={}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIyNTU5NTgxLCJqdGkiOiIyN2NhMDYxZjlkY2Q0ZjBlYWFhMTEyMzE5YTUwZjI2YiIsInVzZXJfaWQiOjF9.LtV7nrAqfOSYomq9B7if_Bz63B7JE3gQ_XADEd8_SYA'

r = requests.get('http://127.0.0.1:8000/FilterClients', headers=headers)

print(r.text)