import pytest

from config.config import BASE_URL


@pytest.mark.parametrize(
    "payload",
    [
        {
            "email": "test@example.com",
            "age": 25
        },
        {
            "name": "Test User",
            "age": 25
        },
        {
            "name": "Test User",
            "email": "invalid-email",
            "age": 25
        },
        {
            "name": "Test User",
            "email": "test@example.com"
        },
        {
            "name": "Test User",
            "email": "test@example.com",
            "age": "twenty-five"
        }
    ]
)
def test_create_user_invalid_data(api_client, payload):

    response = api_client.post(
        f"{BASE_URL}/users",
        data=payload
    )

    assert response.status_code == 422