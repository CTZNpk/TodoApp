from tests.test_api import client


def test_correct_sign_up():
    response = client.post("/signup",
                           data={
                               "username": "haider1@gmail.com",
                               "password": "Password123"
                           })
    assert response.status_code == 200
    assert "access-token" in response.json()
    assert "token-type" in response.json()
    assert response.json()["user"]["email"] == "haider1@gmail.com"


def test_invalid_email_format_1():
    response = client.post("/signup",
                           data={
                               "username": "haider1",
                               "password": "Password123"
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect Email Format"


def test_invalid_email_format_2():

    response = client.post("/signup",
                           data={
                               "username": "haider1@gmail",
                               "password": "Password123"
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect Email Format"


def test_invalid_email_format_3():

    response = client.post("/signup",
                           data={
                               "username": "haider1@gmail.",
                               "password": "Password123"
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect Email Format"


def test_invalid_email_format_4():
    response = client.post("/signup",
                           data={
                               "username": "@haider1.",
                               "password": "Password123"
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect Email Format"


def test_invalid_email_format_5():

    response = client.post("/signup",
                           data={
                               "username": "@g.com",
                               "password": "Password123"
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect Email Format"


def test_invalid_email_format_6():
    response = client.post("/signup",
                           data={
                               "username": "",
                               "password": "Password123"
                           })
    assert response.status_code == 422


def test_invalid_email_format_7():

    response = client.post("/signup",
                           data={
                               "username": "@g.com",
                               "password": "Password123"
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect Email Format"


def test_invalid_password_format_1():
    response = client.post("/signup",
                           data={
                               "username": "haider1@gmail.com",
                               "password": "assword123"
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect Password Format"


def test_invalid_password_format_2():
    response = client.post("/signup",
                           data={
                               "username": "haider1@gmail.com",
                               "password": "password"
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect Password Format"


def test_invalid_password_format_3():
    response = client.post("/signup",
                           data={
                               "username": "haider1@gmail.com",
                               "password": "Password"
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect Password Format"


def test_invalid_password_format_4():

    response = client.post("/signup",
                           data={
                               "username": "haider1@gmail.com",
                               "password": ""
                           })
    assert response.status_code == 422


def test_invalid_password_format_5():
    response = client.post("/signup",
                           data={
                               "username": "haider31@gmail.com",
                               "password": "Pas12"
                           })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect Password Format"


def test_user_already_exists():
    response = client.post("/signup",
                           data={
                               "username": "haider2@gmail.com",
                               "password": "Pass123"
                           })
    assert response.status_code == 200

    response = client.post("/signup",
                           data={
                               "username": "haider2@gmail.com",
                               "password": "Pass123"
                           })

    assert response.status_code == 400


def test_login_user():
    response = client.post("/signup",
                           data={
                               "username": "haider3@gmail.com",
                               "password": "Pass123"
                           })
    assert response.status_code == 200
    response = client.post("/login",
                           data={
                               "username": "haider3@gmail.com",
                               "password": "Pass123"
                           })
    assert response.status_code == 200
    assert response.json()
    assert "access-token" in response.json()
    assert "token-type" in response.json()
    assert response.json()["user"]["email"] == "haider3@gmail.com"


def invalid_login_user_does_not_exist():
    response = client.post("/login",
                           data={
                               "username": "tester@gmail.com",
                               "password": "Pass123"
                           })
    assert response.status_code == 404


def invalid_login_user_wrong_password():
    response = client.post("/signup",
                           data={
                               "username": "login_user@gmail.com",
                               "password": "Pass123"
                           })
    assert response.status_code == 200
    response = client.post("/login",
                           data={
                               "username": "login_user@gmail.com",
                               "password": "Pass1233"
                           })
    assert response.status_code == 404
