"""Namespace and controlled vocabulary constants for SynBioInventory SBOL metadata."""

from __future__ import annotations

from typing import Final

DRAGGON_NS: Final[str] = "https://draggon.org/ns/inventory#"

# Extension property IRIs
PROP_INVENTORY_KIND: Final[str] = f"{DRAGGON_NS}inventory_kind"
PROP_STORED_AT: Final[str] = f"{DRAGGON_NS}stored_at"
PROP_STORAGE_KIND: Final[str] = f"{DRAGGON_NS}storage_kind"
PROP_BARCODE: Final[str] = f"{DRAGGON_NS}barcode"
PROP_LOT_ID: Final[str] = f"{DRAGGON_NS}lot_id"
PROP_NOTES: Final[str] = f"{DRAGGON_NS}notes"

# Controlled implementation kinds
KIND_EXTRACTED_PLASMID: Final[str] = f"{DRAGGON_NS}ExtractedPlasmid"
KIND_BACTERIAL_STOCK: Final[str] = f"{DRAGGON_NS}BacterialStock"
KIND_SOLID_MEDIA_PLATE: Final[str] = f"{DRAGGON_NS}SolidMediaPlate"

# Controlled storage kinds
STORAGE_FRIDGE_MINUS_80C: Final[str] = f"{DRAGGON_NS}FridgeMinus80C"
STORAGE_FRIDGE_MINUS_20C: Final[str] = f"{DRAGGON_NS}FridgeMinus20C"
STORAGE_FRIDGE_4C: Final[str] = f"{DRAGGON_NS}Fridge4C"
STORAGE_SHELF: Final[str] = f"{DRAGGON_NS}Shelf"
STORAGE_BOX: Final[str] = f"{DRAGGON_NS}Box"
STORAGE_SLOT: Final[str] = f"{DRAGGON_NS}Slot"

SBOL_IMPLEMENTATION: Final[str] = "http://sbols.org/v2#Implementation"
SBOL_COLLECTION: Final[str] = "http://sbols.org/v2#Collection"
