"""Core domain schema for SBOL-backed inventory entities.

This module intentionally avoids hard-coupling to a specific SBOL library in order
to keep scaffolding lightweight and highly testable for MVP iterations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from . import namespaces as ns

ImplementationKind = Literal["ExtractedPlasmid", "BacterialStock", "SolidMediaPlate"]
StorageKind = Literal[
    "FridgeMinus80C",
    "FridgeMinus20C",
    "Fridge4C",
    "Shelf",
    "Box",
    "Slot",
]

KIND_TO_URI = {
    "ExtractedPlasmid": ns.KIND_EXTRACTED_PLASMID,
    "BacterialStock": ns.KIND_BACTERIAL_STOCK,
    "SolidMediaPlate": ns.KIND_SOLID_MEDIA_PLATE,
}

STORAGE_TO_URI = {
    "FridgeMinus80C": ns.STORAGE_FRIDGE_MINUS_80C,
    "FridgeMinus20C": ns.STORAGE_FRIDGE_MINUS_20C,
    "Fridge4C": ns.STORAGE_FRIDGE_4C,
    "Shelf": ns.STORAGE_SHELF,
    "Box": ns.STORAGE_BOX,
    "Slot": ns.STORAGE_SLOT,
}


@dataclass(slots=True)
class InventoryImplementation:
    """SBOL Implementation-like inventory model with extension properties."""

    uri: str
    name: str
    inventory_kind: ImplementationKind
    stored_at: str
    built_uri: str | None = None
    barcode: str | None = None
    lot_id: str | None = None
    notes: str | None = None


@dataclass(slots=True)
class StorageCollection:
    """SBOL Collection-like storage model with extension properties."""

    uri: str
    name: str
    storage_kind: StorageKind
    parent_uri: str | None = None
