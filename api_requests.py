import requests


def get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("status code:", response.status_code)
    print("Response:", response.json())


def creat_post():
    data = {"title": "my Task", "body": "Learning API", "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
    print("status code", response.status_code)
    print("Response:", response.json())


def update_post():
    data = {"title": "Updated Title", "body": "Updatednbody", "userId": 1}
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=data)
    print("status code:", response.status_code)
    print("response:", response.json())


def delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    print("status code:", response.status_code)


get_post()
creat_post()
update_post()
delete_post
