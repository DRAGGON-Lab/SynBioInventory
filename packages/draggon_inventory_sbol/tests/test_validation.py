from draggon_inventory_sbol import (
    PlacementValidationError,
    StorageKind,
    make_bacterial_stock,
    make_extracted_plasmid,
    make_solid_media_plate,
    validate_placement,
)


def test_extracted_plasmid_requires_minus_20c() -> None:
    impl = make_extracted_plasmid(uri="urn:test:impl1", stored_at="urn:test:slot")
    validate_placement(impl, StorageKind.FRIDGE_MINUS_20C)


def test_bacterial_stock_rejects_minus_20c() -> None:
    impl = make_bacterial_stock(uri="urn:test:impl2", stored_at="urn:test:slot")
    try:
        validate_placement(impl, StorageKind.FRIDGE_MINUS_20C)
    except PlacementValidationError:
        return
    raise AssertionError("Expected PlacementValidationError")


def test_solid_media_plate_requires_4c() -> None:
    impl = make_solid_media_plate(uri="urn:test:impl3", stored_at="urn:test:slot")
    validate_placement(impl, StorageKind.FRIDGE_4C)
