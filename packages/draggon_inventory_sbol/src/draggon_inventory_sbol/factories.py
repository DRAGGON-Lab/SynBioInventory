"""Factory helpers for SynBioInventory inventory objects."""

from draggon_inventory_sbol.schema import InventoryImplementation


def _make_impl(
    *,
    uri: str,
    inventory_kind: str,
    stored_at: str,
    barcode: str | None = None,
    lot_id: str | None = None,
    notes: str | None = None,
    built_uri: str | None = None,
) -> InventoryImplementation:
    return InventoryImplementation(
        uri=uri,
        inventory_kind=inventory_kind,
        stored_at=stored_at,
        barcode=barcode,
        lot_id=lot_id,
        notes=notes,
        built_uri=built_uri,
    )


def make_extracted_plasmid(
    *,
    uri: str,
    stored_at: str,
    barcode: str | None = None,
    lot_id: str | None = None,
    notes: str | None = None,
    built_uri: str | None = None,
) -> InventoryImplementation:
    return _make_impl(
        uri=uri,
        inventory_kind="ExtractedPlasmid",
        stored_at=stored_at,
        barcode=barcode,
        lot_id=lot_id,
        notes=notes,
        built_uri=built_uri,
    )


def make_bacterial_stock(
    *,
    uri: str,
    stored_at: str,
    barcode: str | None = None,
    lot_id: str | None = None,
    notes: str | None = None,
    built_uri: str | None = None,
) -> InventoryImplementation:
    return _make_impl(
        uri=uri,
        inventory_kind="BacterialStock",
        stored_at=stored_at,
        barcode=barcode,
        lot_id=lot_id,
        notes=notes,
        built_uri=built_uri,
    )


def make_solid_media_plate(
    *,
    uri: str,
    stored_at: str,
    barcode: str | None = None,
    lot_id: str | None = None,
    notes: str | None = None,
    built_uri: str | None = None,
) -> InventoryImplementation:
    return _make_impl(
        uri=uri,
        inventory_kind="SolidMediaPlate",
        stored_at=stored_at,
        barcode=barcode,
        lot_id=lot_id,
        notes=notes,
        built_uri=built_uri,
    )
