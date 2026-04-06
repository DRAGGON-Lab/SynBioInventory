"""Validation rules for SynBioInventory placement constraints."""

from __future__ import annotations

from .schema import InventoryImplementation, InventoryKind, StorageKind

_ALLOWED_TOP_LEVEL_PLACEMENT: dict[InventoryKind, StorageKind] = {
    InventoryKind.EXTRACTED_PLASMID: StorageKind.FRIDGE_MINUS_20C,
    InventoryKind.BACTERIAL_STOCK: StorageKind.FRIDGE_MINUS_80C,
    InventoryKind.SOLID_MEDIA_PLATE: StorageKind.FRIDGE_4C,
}


class PlacementValidationError(ValueError):
    """Raised when an implementation is placed in an unsupported location."""


def validate_placement(
    implementation: InventoryImplementation,
    top_level_storage_kind: StorageKind,
) -> None:
    """Ensure the implementation kind is allowed beneath the selected top-level storage node."""

    expected = _ALLOWED_TOP_LEVEL_PLACEMENT[implementation.inventory_kind]
    if top_level_storage_kind != expected:
        raise PlacementValidationError(
            f"{implementation.inventory_kind} must be placed under {expected}, "
            f"got {top_level_storage_kind}"
        )
