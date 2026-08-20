from config.config import BASE_URL
from utils.test_data_loader import load_test_data


test_data = load_test_data("test_data/users.json")


def test_create_user(api_client):

    payload = test_data["valid_user"]

    response = api_client.post(
        f"{BASE_URL}/users",
        data=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["age"] == payload["age"]
    assert "id" in data