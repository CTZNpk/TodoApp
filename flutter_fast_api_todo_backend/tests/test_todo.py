from .test_api import client


def test_sign_in_and_create_todo():
    response = client.post("/signup",
                           data={
                               "username": "create_todo@gmail.com",
                               "password": "Password123"
                           })
    assert response.status_code == 200
    assert "access-token" in response.json()
    assert "token-type" in response.json()

    token = response.json()["access-token"]

    response = client.post(
        "/todo/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "description": "This is a new todo and i will do it daily",
            "title": "Good Todo",
            "is_daily": True,
        },
    )

    print(response.json())
    assert response.status_code == 200
    assert response.json()["detail"] == "Todo Created Successfully"
    assert response.json()["todo"]["title"] == "Good Todo"
    assert (response.json()["todo"]["description"] ==
            "This is a new todo and i will do it daily")
    assert response.json()["todo"]["is_daily"] is True
    assert response.json()["todo"]["deadline_time"] is None
    assert "created_time" in response.json()["todo"]
    assert response.json()["todo"]["is_done"] is False
    assert response.json()["todo"]["user_email"] == "create_todo@gmail.com"
