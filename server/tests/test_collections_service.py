from app.services.synbiohub_client import SynBioHubClient


def test_collection_navigation_stub_returns_tree() -> None:
    client = SynBioHubClient(base_url="https://stub", use_stub=True)

    roots = client.get_root_collections("token")
    assert len(roots) >= 3

    shelf_level = client.get_subcollections("token", "https://stub.synbiohub.org/collections/fridge-80")
    assert shelf_level and shelf_level[0]["storage_kind"] == "Shelf"

    box_level = client.get_subcollections("token", shelf_level[0]["uri"])
    assert box_level and box_level[0]["storage_kind"] == "Box"

    slot_level = client.get_subcollections("token", box_level[0]["uri"])
    assert slot_level and slot_level[0]["has_subcollections"] is False
