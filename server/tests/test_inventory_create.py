from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_inventory_create_happy_path() -> None:
    login_resp = client.post("/api/auth/login", json={"username": "tester", "password": "secret"})
    assert login_resp.status_code == 200

    files = [("images", ("tube.jpg", BytesIO(b"fake-image").read(), "image/jpeg"))]
    data = {
        "destination_collection_uri": "https://example.org/storage/fridge-80/shelf-a/box-1/slot-a1",
        "implementation_type": "BacterialStock",
        "name": "BS001",
        "notes": "fresh glycerol stock",
    }
    resp = client.post("/api/inventory/create", data=data, files=files)

    assert resp.status_code == 200
    payload = resp.json()
    assert payload["implementation_type"] == "BacterialStock"
    assert payload["attached_images"] == 1
    assert payload["created_uri"].startswith("https://example.org/user/")
