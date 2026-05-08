import pytest
from utils.api_client import ApiClient

def test_create_pet():
    data = {"id": 1001, "name": "framework_dog", "status": "available"}
    resp = ApiClient.post("pet", json=data)
    assert resp.status_code == 200
    assert resp.json()["name"] == "framework_dog"

def test_get_pet():
    resp = ApiClient.get("pet/1001")
    assert resp.status_code == 200
    assert resp.json()["id"] == 1001

