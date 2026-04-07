from app.services.inventory_service import InventoryService, UploadedImage
from app.services.synbiohub_client import SynBioHubClient


def test_inventory_create_happy_path() -> None:
    service = InventoryService(SynBioHubClient(base_url="https://stub", use_stub=True))
    result = service.create_inventory(
        token="stub-token",
        destination_collection_uri="https://stub.synbiohub.org/collections/fridge-80/shelf-a/box-1/slot-a1",
        destination_storage_kind="FridgeMinus80C",
        implementation_type="BacterialStock",
        name="stock-001",
        built_uri=None,
        barcode="BC-1",
        lot_id="L1",
        notes="first stock",
        images=[UploadedImage(filename="tube.jpg", content=b"abc")],
    )

    assert result["implementation_type"] == "BacterialStock"
    assert result["attached_images"] == 1
    assert result["created_uri"].startswith("https://stub.synbiohub.org/inventory/")
