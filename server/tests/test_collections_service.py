from app.services.synbiohub_client import SynBioHubClient


def test_subcollection_navigation_stub() -> None:
    client = SynBioHubClient(base_url="https://example-synbiohub.org", use_stub=True)

    roots = client.list_root_collections()
    assert any(item["display_id"] == "FridgeMinus80C" for item in roots)

    shelf = client.list_subcollections("https://example-synbiohub.org/public/FridgeMinus80C")
    assert shelf[0]["display_id"] == "ShelfA"

    box = client.list_subcollections(shelf[0]["uri"])
    assert box[0]["display_id"] == "Box1"
