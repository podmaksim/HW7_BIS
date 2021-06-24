import requests



base_url = 'https://petstore.swagger.io/v2'


def create_user(id, name, password):
    json = {}
    json["id"] = id
    json["username"] = name
    json["password"] = password
    response = requests.post(f'{base_url}/user', json=json)
    json_response = response.json()
    return json_response


def choice_user(name):
    response = requests.get(f'{base_url}/user/{name}')
    return response.status_code


def update_user(id, name, new_name):
    json = {}
    json["id"] = id
    json["username"] = new_name
    response = requests.put(f'{base_url}/user/{name}', json=json)
    json_response = response.json()
    return json_response


def choice_new_user(new_name):
    response = requests.get(f'{base_url}/user/{new_name}')
    return response.status_code


def delete_user(new_name):
    response = requests.delete(f'{base_url}/user/{new_name}')
    return response.status_code