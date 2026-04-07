import pytest

from draggon_inventory_sbol import (
    PlacementValidationError,
    StorageCollection,
    make_bacterial_stock,
    make_extracted_plasmid,
    make_solid_media_plate,
    validate_placement,
)


@pytest.mark.parametrize(
    ("factory", "storage_kind"),
    [
        (make_extracted_plasmid, "FridgeMinus20C"),
        (make_bacterial_stock, "FridgeMinus80C"),
        (make_solid_media_plate, "Fridge4C"),
    ],
)
def test_valid_placements(factory, storage_kind: str) -> None:
    impl = factory(uri="https://example.org/item", stored_at="https://example.org/slot")
    storage = StorageCollection(uri="https://example.org/slot", storage_kind=storage_kind)
    validate_placement(impl, storage)


def test_invalid_placement_raises() -> None:
    impl = make_bacterial_stock(uri="https://example.org/item", stored_at="https://example.org/slot")
    storage = StorageCollection(uri="https://example.org/slot", storage_kind="FridgeMinus20C")
    with pytest.raises(PlacementValidationError):
        validate_placement(impl, storage)
