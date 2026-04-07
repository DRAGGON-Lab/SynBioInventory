from fastapi.testclient import TestClient

from app.main import app


def test_inventory_create_happy_path() -> None:
    client = TestClient(app)

    response = client.post(
        "/api/inventory/create",
        data={
            "destination_collection_uri": "https://example-synbiohub.org/public/FridgeMinus80C/ShelfA/Box1/SlotA1",
            "destination_storage_kind": "FridgeMinus80C",
            "implementation_type": "BacterialStock",
            "object_uri": "bact_stock_001",
            "barcode": "BC-001",
        },
        files=[("images", ("tube.jpg", b"fakebytes", "image/jpeg"))],
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["implementation_type"] == "BacterialStock"
    assert payload["attached_images"] == 1
    assert payload["created_uri"].endswith("bact_stock_001")
