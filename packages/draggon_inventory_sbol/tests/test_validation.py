import pytest

from draggon_inventory_sbol.factories import (
    make_bacterial_stock,
    make_extracted_plasmid,
    make_solid_media_plate,
)
from draggon_inventory_sbol.schema import StorageCollection
from draggon_inventory_sbol.validation import PlacementValidationError, validate_placement


def test_valid_placement_for_each_type() -> None:
    extracted = make_extracted_plasmid(uri="https://ex.org/i1", name="i1", stored_at="https://ex.org/c20")
    stock = make_bacterial_stock(uri="https://ex.org/i2", name="i2", stored_at="https://ex.org/c80")
    plate = make_solid_media_plate(uri="https://ex.org/i3", name="i3", stored_at="https://ex.org/c4")

    validate_placement(
        extracted,
        StorageCollection(uri="https://ex.org/c20", name="c20", storage_kind="FridgeMinus20C"),
    )
    validate_placement(
        stock,
        StorageCollection(uri="https://ex.org/c80", name="c80", storage_kind="FridgeMinus80C"),
    )
    validate_placement(
        plate,
        StorageCollection(uri="https://ex.org/c4", name="c4", storage_kind="Fridge4C"),
    )


def test_invalid_placement_raises() -> None:
    stock = make_bacterial_stock(uri="https://ex.org/i2", name="i2", stored_at="https://ex.org/c20")

    with pytest.raises(PlacementValidationError):
        validate_placement(
            stock,
            StorageCollection(uri="https://ex.org/c20", name="c20", storage_kind="FridgeMinus20C"),
        )
