from config.config import BASE_URL


def test_get_users(api_client):
    response = api_client.get(f"{BASE_URL}/users")

    assert response.status_code == 200

    data = response.json()

    assert "users" in data
    assert len(data["users"]) > 0