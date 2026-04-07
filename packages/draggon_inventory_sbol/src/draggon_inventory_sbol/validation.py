"""Validation helpers for inventory/storage constraints."""

from __future__ import annotations

from .schema import InventoryImplementation, StorageCollection

PLACEMENT_RULES = {
    "ExtractedPlasmid": "FridgeMinus20C",
    "BacterialStock": "FridgeMinus80C",
    "SolidMediaPlate": "Fridge4C",
}


class PlacementValidationError(ValueError):
    """Raised when an inventory implementation is placed in an invalid storage node."""


def validate_placement(
    implementation: InventoryImplementation,
    destination_collection: StorageCollection,
) -> None:
    """Validate placement of an implementation in a storage collection.

    Rules are intentionally strict for MVP to reduce ambiguity in initial dataset.
    """

    expected_storage_kind = PLACEMENT_RULES[implementation.inventory_kind]
    if destination_collection.storage_kind != expected_storage_kind:
        raise PlacementValidationError(
            f"{implementation.inventory_kind} must be placed under {expected_storage_kind}; "
            f"got {destination_collection.storage_kind}."
        )
