"""Core domain schema objects for SynBioInventory SBOL representations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class StorageCollection:
    """Storage node modeled as an SBOL Collection with extension properties."""

    uri: str
    storage_kind: str
    parent_uri: Optional[str] = None
    label: Optional[str] = None


@dataclass(slots=True)
class InventoryImplementation:
    """Physical inventory implementation modeled as an SBOL Implementation."""

    uri: str
    inventory_kind: str
    stored_at: str
    barcode: Optional[str] = None
    lot_id: Optional[str] = None
    notes: Optional[str] = None
    built_uri: Optional[str] = None
