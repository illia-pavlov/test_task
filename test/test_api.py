from main import create_user, update_user, create_user_data_json, update_user_data_json

def test_email_login_check():
    get_user_request = create_user()
    actual_login = get_user_request.json()['login']
    actual_email = get_user_request.json()['account_details']['email']
    actual_user_data_json = {
        "user": {
            "login": f'{actual_login}',
            "email": f'{actual_email}',
            "password": "Pa55word"
        }
    }
    assert actual_user_data_json == create_user_data_json, "Login or email is not correct"


def test_email_login_after_update_check():
    get_user_request = update_user()
    actual_login = get_user_request.json()['login']
    actual_email = get_user_request.json()['account_details']['email']
    actual_user_data_json = {
        "user": {
            "login": f'{actual_login}',
            "email": f'{actual_email}'
        }
    }
    assert actual_user_data_json == update_user_data_json, "Login or email is not correct"
