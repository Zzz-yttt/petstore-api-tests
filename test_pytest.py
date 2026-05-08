import requests

def test_get_pet():
    url = "https://petstore.swagger.io/v2/pet/1001"
    resp = requests.get(url)
    assert resp.status_code == 200
    assert resp.json()["id"] == 1001

def test_create_pet():
    url = "https://petstore.swagger.io/v2/pet"
    data = {"id": 3001, "name": "pytest_cat", "status": "available"}
    resp = requests.post(url, json=data)
    assert resp.status_code == 200
    assert resp.json()["name"] == "pytest_cat"