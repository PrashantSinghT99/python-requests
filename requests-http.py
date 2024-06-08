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
    "email": "PostTest1234567@example.com",
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
    "email": "PutTestupdated2345@example.com",
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
put_request(id)
delete_request(id)