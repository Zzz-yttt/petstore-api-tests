import requests

url = "https://petstore.swagger.io/v2/pet/1001"

try:
    response = requests.get(url, timeout=10)
    print("状态码:", response.status_code)
    print("返回的 JSON 数据:", response.json())
except Exception as e:
    print("请求出错啦！错误信息:", e)


# POST 创建宠物
post_url = "https://petstore.swagger.io/v2/pet"
new_pet = {"id": 2001, "name": "pytest_dog", "status": "available"}
post_resp = requests.post(post_url, json=new_pet)
print("POST 状态码:", post_resp.status_code)

# PUT 修改宠物
put_url = "https://petstore.swagger.io/v2/pet"
updated_pet = {"id": 2001, "name": "pytest_dog_updated", "status": "sold"}
put_resp = requests.put(put_url, json=updated_pet)
print("PUT 状态码:", put_resp.status_code)

# DELETE 删除宠物
del_url = "https://petstore.swagger.io/v2/pet/2001"
del_resp = requests.delete(del_url)
print("DELETE 状态码:", del_resp.status_code)