def test_create_user(client):
    deta = {
        "username": "testuser",
        "email": "testuser@nofoobar.com",
        "password": "password",
    }
    response = client.post("/users", json=deta)
    if response.status_code != 201:
        print("Error details:", response.json())
    assert response.status_code == 201
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] == True
