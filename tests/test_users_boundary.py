import pytest

from config.config import BASE_URL


@pytest.mark.parametrize(
    "age, expected_status",
    [
        (17, 422),
        (18, 201),
        (19, 201),
        (99, 201),
        (100, 201),
        (101, 422)
    ]
)
def test_user_age_boundaries(api_client, age, expected_status):

    payload = {
        "name": "Boundary User",
        "email": f"boundary{age}@example.com",
        "age": age
    }

    response = api_client.post(
        f"{BASE_URL}/users",
        data=payload
    )

    assert response.status_code == expected_status