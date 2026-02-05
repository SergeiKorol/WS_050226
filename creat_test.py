import requests
def create_test():
    body = {"title" : "generated", "completed" : False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    assert response.status_code == 200

    response1 = requests.delete("https://todo-app-sky.herokuapp.com/{id}")

    assert response1.status_code == 404
    