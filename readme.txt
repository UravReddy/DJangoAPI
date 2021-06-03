URLS

# Obtain access token from 
http://127.0.0.1:8000/api/token/

{
    "username": "superusername"
    "password": "superuserpassword"
}


#Adding the access token to requests

# ADD TO HEADER 
KEY = Authorization
VALUE = Bearer accesstoken




# Get all active clients
http://127.0.0.1:8000/FilterClients




#Get Client by id  with client id at the end of url
http://127.0.0.1:8000/FilterClients/1




#Put to client has to be done in raw json

url = http://127.0.0.1:8000/FilterClients/1

json = 
{
    "id": 1,
    "clientName": "Urav",
    "clientCountry": "South Africa"
}

#Get all active projects
http://127.0.0.1:8000/projects/


#Get project by id with project id at the end of url
http://127.0.0.1:8000/projects/1

#Put to client has to be done in raw json

url = http://127.0.0.1:8000/projects/1

json = 

{
    "id": 1,
    "projectName": "Urav",
    "projectLanguage": "English",
    "projectClient": 1
}