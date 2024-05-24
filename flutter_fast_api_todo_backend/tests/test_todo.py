from .test_api import client

access_token = None


def test_login_and_create_todo():
    response = client.post("/signup",
                           data={
                               "username": "create_todo@gmail.com",
                               "password": "Password123"
                           })
    assert response.status_code == 200
    assert "access-token" in response.json()
    assert "token-type" in response.json()

    global access_token
    access_token = response.json()["access-token"]

    response = client.post(
        "/todo/",
        headers={"Authorization": f"Bearer {access_token}"},
        json={
            "description": "This is a new todo and i will do it daily",
            "title": "Good Todo",
            "is_daily": True,
        },
    )

    json_response = response.json()

    assert response.status_code == 200
    assert json_response["detail"] == "Todo Created Successfully"
    assert json_response["todo"]["title"] == "Good Todo"
    assert (json_response["todo"]["description"] ==
            "This is a new todo and i will do it daily")
    assert json_response["todo"]["is_daily"] is True
    assert json_response["todo"]["deadline_time"] is None
    assert "created_time" in json_response["todo"]
    assert json_response["todo"]["is_done"] is False
    assert json_response["todo"]["user_email"] == "create_todo@gmail.com"
    assert json_response["todo"]["todo_id"] == 1


def test_get_user_todo():
    response = client.get(
        "/todo/",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert response.status_code == 200

    json_response = response.json()
    assert json_response[0]["title"] == "Good Todo"
    assert (json_response[0]["description"] ==
            "This is a new todo and i will do it daily")
    assert json_response[0]["is_daily"] is True
    assert json_response[0]["deadline_time"] is None
    assert "created_time" in json_response[0]
    assert json_response[0]["is_done"] is False
    assert json_response[0]["user_email"] == "create_todo@gmail.com"


def test_todo_done():
    response = client.patch(
        "/todo/1/done",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    json_response = response.json()

    assert response.status_code == 200
    assert json_response["detail"] == "Todo Updated Successfully"
    assert json_response["todo"]["is_done"] is True


def test_todo_update():
    response = client.patch(
        "/todo/1",
        headers={"Authorization": f"Bearer {access_token}"},
        json={
            "description": "Home work to do",
            "title": "homework",
            "is_daily": False,
            "is_done": False,
        },
    )

    json_response = response.json()

    assert response.status_code == 200
    assert json_response["detail"] == "Todo Updated Successfully"
    assert json_response["todo"]["is_done"] is False
    assert json_response["todo"]["title"] == "homework"
    assert json_response["todo"]["description"] == "Home work to do"
    assert json_response["todo"]["is_daily"] is False


def test_todo_delete():
    response = client.delete(
        "/todo/1",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert response.status_code == 204
