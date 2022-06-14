## User Manager API
This is a REST API built using Djnago and Django Rest Framework. 
It has a database which hold user and a user_child information table. You can view, create, update, delete user and user_child. A user_child can not exist without a parent(user).

## Installation Instruction
You need python and pip installed on your system. 
Run the following command in your terminal:
pip install -r requirements.txt

Go to the project directory in your teminal and run the following command:
python manage.py runserver

This will start the development server at http://127.0.0.1:8000/

## API Endpoints
- GET
![GET REQUEST USERS](https://user-images.githubusercontent.com/35129264/173423648-cc18c4e4-634b-4b3e-97d7-786261b71334.png)
You can get all the existing users in the database using http://127.0.0.1:8000/users/

![GET REQUEST USERS INSIDE THE BROWSER](https://user-images.githubusercontent.com/35129264/173650044-bf8f690a-250e-4f97-8809-d4f6dc0a179d.png)
User Data inside the browser
________________________________________________________________

![GET REQUEST USERS_CHILD](https://user-images.githubusercontent.com/35129264/173423995-6e92b0cd-dfb2-4951-96a2-71f5a3416813.png)
You can get all the existing child under all parents using http://127.0.0.1:8000/users-child/

![GET REQUEST USERS_CHILD INSIDE THE BROWSER](https://user-images.githubusercontent.com/35129264/173652021-97e19617-3def-4f95-afbb-325e054edd1b.png)
User_child Data inside the browser

You can also get an specific user or user_child data using their ID
![image](https://user-images.githubusercontent.com/35129264/173656421-8ce1628c-ea34-4c0b-99dc-7cc9c6f9cbc8.png)
http://127.0.0.1:8000/users/{ID}    Replace ID with a valid ID to get a specific user

![image](https://user-images.githubusercontent.com/35129264/173653643-020b7201-523a-4882-9ffa-160cf68df0ab.png)
http://127.0.0.1:8000/users-child/{ID}  Replace ID with a valid ID to get a specific user_child

Data Can be updated through these webpages as well by putting a valid json data inside the content field

- POST
![POST REQUEST USERS](https://user-images.githubusercontent.com/35129264/173424423-bd314093-a6cb-44dc-aacb-d8793abebfb6.png)
You can add new user using http://127.0.0.1:8000/users/ and sending a POST request with a JSON data in the body in following format:
{
    "id": 1,
    "first_name": "Nobita",
    "last_name": "Monsur",
    "street_address": "Kanchan",
    "city_address": "Gazirampur",
    "state_address": "Sholakia",
    "zip_code": "8457"
}
________________________________________________________________

![POST REQUEST USERS_CHILD](https://user-images.githubusercontent.com/35129264/173424896-dcf45df2-ed2d-4059-bd8a-8ab3565b59af.png)
You can add new user_child using http://127.0.0.1:8000/users-child/ and sending a POST request with a JSON data in the body in following format:
{
    "parent": 1,
    "child_first_name": "Shonir",
    "child_last_name": "Akhra"
}

*You must provide an existing id from the users Table in side the parent parameter to create a new user_child

- PUT
![PUT REQUEST USER](https://user-images.githubusercontent.com/35129264/173425413-48a8fdcc-dd6b-4566-8f04-759f455124f5.png)
You can update existing user information using http://127.0.0.1:8000/users/{id} [specify the id number of the user you want to update in {id}], and send a PUT request with a JSON data in the body in following format:
{
            "first_name": "Narshingam",
            "last_name": "Kontaki",
            "street_address": "Kanthakier",
            "city_address": "Kilmany",
            "state_address": "korotia",
            "zip_code": "4875"
}
________________________________________________________________

![PUT REQUEST USER_CHILD](https://user-images.githubusercontent.com/35129264/173427067-c81d8fa8-071f-4360-94db-7b7019830ad8.png)
You can update existing user_child information using http://127.0.0.1:8000/users-child/{id} [specify the id number of the user_child you want to update in {id}], and send a PUT request with a JSON data in the body in following format:
{
    "parent": 1,
    "child_first_name": "Intesar",
    "child_last_name": "Ali"
}

- DELETE
![image](https://user-images.githubusercontent.com/35129264/173427883-78b28710-cdb7-48d5-a367-31afe1c5287b.png)
You can delete any user information from the database using http://127.0.0.1:8000/users/{id} [specify the id number of the user you want to Delete in {id}], and send a DELETE Request

________________________________________________________________

![DELETE REQUEST USER](https://user-images.githubusercontent.com/35129264/173427384-9877e8b9-dd7f-4768-97ab-2c84cb921621.png)
You can delete any user_child information from the database using http://127.0.0.1:8000/users-child/{id} [specify the id number of the user_child you want to Delete in {id}], and send a DELETE Request

## Admin Panel
Alternatively you can use this admin panel to interact with the database directly. Visit this link to access the admin panel http://127.0.0.1:8000/admin/
![Admin Panel](https://user-images.githubusercontent.com/35129264/173641663-8edbf521-5b47-4089-899c-61c3735ac7ab.png)
