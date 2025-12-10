import requests

URL_API = "https://jsonplaceholder.typicode.com/"

def get_users():
    print("OBTENEINDO USERS........")

    response = requests.get(URL_API + "users")

    print(response.status_code)

    assert response.status_code == 200

    data = response.json()
    print(data)

def post_users():
    print('CREANDO USUARIOS')

    new_user = {
        "name":"Nati",
        "email" : "",
        "phone": "22323232323"
    }

    response = requests.post(URL_API + "users", new_user)
    print(response.status_code)
    data = response.json()
    print(data)

def put_user():
    print("actualizando total de usuario....")
    
    user_update = {
        "id":1,
        "name": "hola mundo"
    }

    response = requests.put(URL_API + "users/1", user_update)
    print(response.status_code)

def patch_user():
    print("actualizando total de usuario....")
    
    user_update = {
        "id":1,
        "email":"asasa@gmail.com"
    }

    response = requests.patch(URL_API + "users/1", user_update)
    print(response.status_code)

def delete_user():
    print("elimiando total de usuario....")

    response = requests.delete(URL_API + "users/1")
    print(response.status_code)

# get_users()
# post_users()
# put_user()
# patch_user()
delete_user()