from config.config import BASE_URL


def test_delete_user(api_client):

    # Create a user specifically for this test
    payload = {
        "name": "Delete Test User",
        "email": "delete.test@example.com",
        "age": 25
    }

    create_response = api_client.post(
        f"{BASE_URL}/users",
        data=payload
    )

    assert create_response.status_code == 201

    created_user = create_response.json()
    user_id = created_user["id"]

    # Delete the newly created user
    response = api_client.delete(
        f"{BASE_URL}/users/{user_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "User deleted successfully"
    assert data["user"]["id"] == user_id


def test_delete_nonexistent_user(api_client):

    user_id = 999

    response = api_client.delete(
        f"{BASE_URL}/users/{user_id}"
    )

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "User not found"