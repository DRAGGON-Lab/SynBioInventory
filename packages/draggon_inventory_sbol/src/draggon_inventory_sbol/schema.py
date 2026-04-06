"""Domain schema models used for SBOL-like inventory object generation."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class InventoryKind(StrEnum):
    """Supported MVP implementation kinds."""

    EXTRACTED_PLASMID = "ExtractedPlasmid"
    BACTERIAL_STOCK = "BacterialStock"
    SOLID_MEDIA_PLATE = "SolidMediaPlate"


class StorageKind(StrEnum):
    """Supported MVP storage hierarchy node kinds."""

    FRIDGE_MINUS_80C = "FridgeMinus80C"
    FRIDGE_MINUS_20C = "FridgeMinus20C"
    FRIDGE_4C = "Fridge4C"
    SHELF = "Shelf"
    BOX = "Box"
    SLOT = "Slot"


@dataclass(slots=True)
class StorageCollection:
    """Collection-shaped storage node represented in SBOL as a Collection."""

    uri: str
    storage_kind: StorageKind
    name: str | None = None
    parent_uri: str | None = None


@dataclass(slots=True)
class InventoryImplementation:
    """Implementation-shaped inventory object represented in SBOL as an Implementation."""

    uri: str
    inventory_kind: InventoryKind
    stored_at: str
    built_uri: str | None = None
    barcode: str | None = None
    lot_id: str | None = None
    notes: str | None = None
    name: str | None = None
