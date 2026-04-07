"""Namespace constants for SynBioInventory SBOL extension terms."""

from rdflib import Namespace

SBOL2 = Namespace("http://sbols.org/v2#")
DRAGGON = Namespace("https://draggon.org/ns/inventory#")

INVENTORY_KINDS = {
    "ExtractedPlasmid": DRAGGON.ExtractedPlasmid,
    "BacterialStock": DRAGGON.BacterialStock,
    "SolidMediaPlate": DRAGGON.SolidMediaPlate,
}

STORAGE_KINDS = {
    "FridgeMinus80C": DRAGGON.FridgeMinus80C,
    "FridgeMinus20C": DRAGGON.FridgeMinus20C,
    "Fridge4C": DRAGGON.Fridge4C,
    "Shelf": DRAGGON.Shelf,
    "Box": DRAGGON.Box,
    "Slot": DRAGGON.Slot,
}
