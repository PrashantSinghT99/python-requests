import requests
import random
import string
import json
import os
from dotenv import load_dotenv

#PRE-REQUISITES
load_dotenv()
#base url
domain="https://gorest.co.in"
#auth token
token = os.getenv('TOKEN')
auth_token=f"Bearer {token}"

if not auth_token:
    raise ValueError("No authentication token found. Please set the TOKEN environment variable.")

#helpers


def generate_random_email(domain="example.com"):
    """Generate a random email address."""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@{domain}"


#GET

def get_request():
    url=domain+"/public/v2/users/"
    print("Sending a GET request at",url)
    headers={"Authorization": auth_token}
    response=requests.get(url,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_string=json.dumps(json_data,indent=4)
    print("json response body from GET:",json_string)

#POST

def post_request():

    url=domain+"/public/v2/users"
    print("Sending a POST request at",url)
    headers={"Authorization":auth_token}
    data={
    "name": "Post Test1234567",
    "email": generate_random_email(),
    "gender": "male",
    "status": "inactive"
    }
    response=requests.post(url,json=data,headers=headers)
    assert response.status_code == 201
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json response body from POST:",json_str)
    user_id=json_data["id"]
    assert "name" in json_data
    assert "email" in json_data
    assert "gender" in json_data
    assert "status" in json_data
    assert json_data["name"] == data["name"]
    print("User id from POST response",user_id)
    return user_id
 
#PUT

def put_request(post_id):

    url=domain+f"/public/v2/users/{post_id}"
    print("Sending a PUT request at",url," To Update User",post_id)
    headers={"Authorization":auth_token}
    data={
    "name": "PutTestupdated2345",
    "email": generate_random_email(),
    "gender": "male",
    "status": "active"
    }
    response=requests.put(url,json=data,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json response body from PUT:",json_str)
    assert json_data["id"]== post_id
    assert json_data["name"]==data["name"]
    assert json_data["email"]==data["email"]
    assert json_data["status"]==data["status"]


#DELETE

def delete_request(id):
    url=domain+f"/public/v2/users/{id}"
    print("Delete request",url)
    headers={"Authorization":auth_token}    
    response=requests.delete(url,headers=headers)
    assert response.status_code == 204
    print("DELETED user:",id)
    
    
#calls
get_request()
id=post_request()
# Update the user
if id:
   put_request(id)
# Delete the user
if id:
    delete_request(id)