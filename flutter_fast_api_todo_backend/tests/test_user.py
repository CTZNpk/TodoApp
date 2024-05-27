from .test_api import client


def test_get_current_user():
    response = client.post(
        "/signup",
        data={
            "username": "check_current_user@gmail.com",
            "password": "Password123"
        },
    )
    assert response.status_code == 200
    assert "access-token" in response.json()
    assert "token-type" in response.json()

    global access_token
    access_token = response.json()["access-token"]

    response = client.get(
        "/user/",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    json_response = response.json()

    assert response.status_code == 200
    assert json_response["email"] == "check_current_user@gmail.com"
    assert json_response["is_active"] is True


def test_deactivate_user():
    response = client.post(
        "/signup",
        data={
            "username": "check_deactivate@gmail.com",
            "password": "Password123"
        },
    )
    assert response.status_code == 200
    assert "access-token" in response.json()
    assert "token-type" in response.json()

    response = client.patch(
        "/user/disable",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert response.status_code == 200

    response = client.get(
        "/user/",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert response.status_code == 400
