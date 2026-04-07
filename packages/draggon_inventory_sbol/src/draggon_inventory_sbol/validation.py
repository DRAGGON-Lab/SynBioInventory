"""Validation rules for inventory placement constraints."""

from draggon_inventory_sbol.schema import InventoryImplementation, StorageCollection

_ALLOWED_PLACEMENT = {
    "ExtractedPlasmid": "FridgeMinus20C",
    "BacterialStock": "FridgeMinus80C",
    "SolidMediaPlate": "Fridge4C",
}


class PlacementValidationError(ValueError):
    """Raised when inventory placement violates domain policy."""


def validate_placement(
    implementation: InventoryImplementation, destination: StorageCollection
) -> None:
    """Validate implementation placement under the selected storage collection."""
    required_storage = _ALLOWED_PLACEMENT.get(implementation.inventory_kind)
    if required_storage is None:
        raise PlacementValidationError(
            f"Unsupported implementation type: {implementation.inventory_kind}"
        )
    if destination.storage_kind != required_storage:
        raise PlacementValidationError(
            f"{implementation.inventory_kind} must be placed under {required_storage}"
        )
