"""Domain-specific factory functions for SynBioInventory implementation kinds."""

from __future__ import annotations

from .schema import InventoryImplementation


def _make_inventory(
    *,
    uri: str,
    name: str,
    stored_at: str,
    inventory_kind: str,
    built_uri: str | None = None,
    barcode: str | None = None,
    lot_id: str | None = None,
    notes: str | None = None,
) -> InventoryImplementation:
    return InventoryImplementation(
        uri=uri,
        name=name,
        inventory_kind=inventory_kind,
        stored_at=stored_at,
        built_uri=built_uri,
        barcode=barcode,
        lot_id=lot_id,
        notes=notes,
    )


def make_extracted_plasmid(
    *,
    uri: str,
    name: str,
    stored_at: str,
    built_uri: str | None = None,
    barcode: str | None = None,
    lot_id: str | None = None,
    notes: str | None = None,
) -> InventoryImplementation:
    """Construct an ExtractedPlasmid inventory implementation."""

    return _make_inventory(
        uri=uri,
        name=name,
        stored_at=stored_at,
        inventory_kind="ExtractedPlasmid",
        built_uri=built_uri,
        barcode=barcode,
        lot_id=lot_id,
        notes=notes,
    )


def make_bacterial_stock(
    *,
    uri: str,
    name: str,
    stored_at: str,
    built_uri: str | None = None,
    barcode: str | None = None,
    lot_id: str | None = None,
    notes: str | None = None,
) -> InventoryImplementation:
    """Construct a BacterialStock inventory implementation."""

    return _make_inventory(
        uri=uri,
        name=name,
        stored_at=stored_at,
        inventory_kind="BacterialStock",
        built_uri=built_uri,
        barcode=barcode,
        lot_id=lot_id,
        notes=notes,
    )


def make_solid_media_plate(
    *,
    uri: str,
    name: str,
    stored_at: str,
    built_uri: str | None = None,
    barcode: str | None = None,
    lot_id: str | None = None,
    notes: str | None = None,
) -> InventoryImplementation:
    """Construct a SolidMediaPlate inventory implementation."""

    return _make_inventory(
        uri=uri,
        name=name,
        stored_at=stored_at,
        inventory_kind="SolidMediaPlate",
        built_uri=built_uri,
        barcode=barcode,
        lot_id=lot_id,
        notes=notes,
    )
