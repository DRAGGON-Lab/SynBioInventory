"""Factory helpers for creating inventory implementations."""

from __future__ import annotations

from .schema import InventoryImplementation, InventoryKind


def _make_inventory(
    inventory_kind: InventoryKind,
    *,
    uri: str,
    stored_at: str,
    built_uri: str | None = None,
    barcode: str | None = None,
    lot_id: str | None = None,
    notes: str | None = None,
    name: str | None = None,
) -> InventoryImplementation:
    return InventoryImplementation(
        uri=uri,
        inventory_kind=inventory_kind,
        stored_at=stored_at,
        built_uri=built_uri,
        barcode=barcode,
        lot_id=lot_id,
        notes=notes,
        name=name,
    )


def make_extracted_plasmid(**kwargs: str | None) -> InventoryImplementation:
    """Create an ExtractedPlasmid implementation object."""

    return _make_inventory(InventoryKind.EXTRACTED_PLASMID, **kwargs)


def make_bacterial_stock(**kwargs: str | None) -> InventoryImplementation:
    """Create a BacterialStock implementation object."""

    return _make_inventory(InventoryKind.BACTERIAL_STOCK, **kwargs)


def make_solid_media_plate(**kwargs: str | None) -> InventoryImplementation:
    """Create a SolidMediaPlate implementation object."""

    return _make_inventory(InventoryKind.SOLID_MEDIA_PLATE, **kwargs)
