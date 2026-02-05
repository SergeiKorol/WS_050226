import requests

def create_test():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    body = {"completed":True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200
    assert response.json()['completed'] == True

    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 204

def create_test2():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    body = {"title": "modified"}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    resp = response.json()["title"]
    assert body == resp

    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 204

def create_test3():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 204

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 404