from config.config import BASE_URL


def test_update_user(api_client):

    user_id = 1

    payload = {
        "name": "Updated Rahul",
        "email": "updated.rahul@example.com",
        "age": 30
    }

    response = api_client.put(
        f"{BASE_URL}/users/{user_id}",
        data=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["age"] == payload["age"]


def test_update_nonexistent_user(api_client):

    user_id = 999

    payload = {
        "name": "Unknown User",
        "email": "unknown@example.com",
        "age": 25
    }

    response = api_client.put(
        f"{BASE_URL}/users/{user_id}",
        data=payload
    )

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "User not found"