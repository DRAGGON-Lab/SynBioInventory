from app.services.synbiohub_client import SynBioHubClient


def test_subcollection_navigation_behavior() -> None:
    client = SynBioHubClient()
    roots = client.get_root_collections()
    assert len(roots) == 3

    parent_uri = "https://example.org/storage/fridge-80"
    sub = client.get_subcollections(parent_uri)
    assert len(sub) == 1
    assert sub[0]["storage_kind"] == "Shelf"

    leaf_uri = "https://example.org/storage/fridge-80/shelf-a/box-1/slot-a1"
    assert client.get_top_level_storage_kind(leaf_uri) == "FridgeMinus80C"
