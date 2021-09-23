import requests
import random

BASE_URL = 'https://favqs.com/api/'
create_random_number = random.randint(0, 10000)
update_random_number = random.randint(0, 10000)
create_user_data = {
    "user": {
        "login": f'aurelius{create_random_number}',
        "email": f'aurelius{create_random_number}@gmail.com',
        "password": "Pa55word"
    }
}

update_user_data = {
    "user": {
        "login": f'aurelius{update_random_number}',
        "email": f'aurelius{update_random_number}@gmail.com',
    }
}

create_session_data = {
    "user": {
        "login": f'aurelius{create_random_number}',
        "password": "Pa55word",
    }
}

create_user_data_json = create_user_data
update_user_data_json = update_user_data
create_session_data_json = create_session_data

token = "7464a935a833b06c98accde18a24f378"
headers = {'Authorization': f'Token token="{token}"'}


def email_login_check(act_data, expec_data):
    print(act_data)
    print(expec_data)
    assert act_data == expec_data, "Login or email is not correct"


def create_user():
    create_user_request = requests.post(f'{BASE_URL}users',
                                        json=create_user_data_json,
                                        headers=headers)
    user_token = create_user_request.json()['User-Token']
    headers_session_create = {'Authorization': f'Token token="{token}"',
                              'User-Token': f'{user_token}'
                              }
    post_session_create = requests.post(f'{BASE_URL}session',
                                        json=create_session_data_json,
                                        headers=headers_session_create)
    session_token = post_session_create.json()['User-Token']
    global headers_get_user
    headers_get_user = {'Authorization': f'Token token="{token}"',
                        'User-Token': f'{session_token}'}
    get_user_request = requests.get(f'{BASE_URL}users/{create_user_data_json["user"]["login"]}',
                                    headers=headers_get_user)
    return get_user_request


def update_user():
    url = f'{BASE_URL}users/{create_session_data_json["user"]["login"]}'
    update_user_request = requests.put(url,
                                       json=update_user_data_json,
                                       headers=headers_get_user)
    get_user_request = requests.get(f'{BASE_URL}users/{update_user_data_json["user"]["login"]}',
                                    headers=headers_get_user)
    return get_user_request
