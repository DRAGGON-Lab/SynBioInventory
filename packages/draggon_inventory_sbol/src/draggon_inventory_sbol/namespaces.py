"""Namespace and controlled vocabulary constants for SynBioInventory."""

from __future__ import annotations

DRAGGON_NS = "https://draggon.org/ns/inventory#"
SBOL_NS = "http://sbols.org/v2#"
RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

INVENTORY_KIND_PREDICATE = f"{DRAGGON_NS}inventory_kind"
STORED_AT_PREDICATE = f"{DRAGGON_NS}stored_at"
BARCODE_PREDICATE = f"{DRAGGON_NS}barcode"
LOT_ID_PREDICATE = f"{DRAGGON_NS}lot_id"
NOTES_PREDICATE = f"{DRAGGON_NS}notes"
STORAGE_KIND_PREDICATE = f"{DRAGGON_NS}storage_kind"
PARENT_STORAGE_PREDICATE = f"{DRAGGON_NS}parent_storage"

EXTRACTED_PLASMID = "ExtractedPlasmid"
BACTERIAL_STOCK = "BacterialStock"
SOLID_MEDIA_PLATE = "SolidMediaPlate"

FRIDGE_MINUS_80C = "FridgeMinus80C"
FRIDGE_MINUS_20C = "FridgeMinus20C"
FRIDGE_4C = "Fridge4C"
SHELF = "Shelf"
BOX = "Box"
SLOT = "Slot"
