from config.config import BASE_URL


def test_get_users_headers_and_response_time(api_client):
    response = api_client.get(f"{BASE_URL}/users")

    # Status code validation
    assert response.status_code == 200

    # Response header validation
    assert "content-type" in response.headers
    assert response.headers["content-type"].startswith("application/json")

    # Response time validation
    assert response.elapsed.total_seconds() < 2

    # Response payload validation
    data = response.json()
    assert "users" in data