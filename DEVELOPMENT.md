# Development

## Purpose

This file describes how to set up local development for SynBioInventory and how to approach the codebase during the early scaffold phase.

## Development goals

The initial development goals are:

- make the repository runnable locally,
- scaffold package, backend, and frontend cleanly,
- support development without a live SynBioHub instance,
- make the first end-to-end happy path testable early.

## Local stack

Planned local components:

- Python package for SBOL inventory logic
- FastAPI backend
- React TypeScript frontend
- Docker Compose orchestration

## Recommended setup steps

1. clone the repository
2. create environment files from examples
3. run backend and frontend in stub mode
4. verify login, collection browsing, and create flow against mock data
5. begin replacing stubs with real integration points

## Environment variables

Suggested root `.env.example` entries:

```env
SYNBIOHUB_BASE_URL=https://your-synbiohub-instance.org
SYNBIOHUB_USE_STUB=true
BACKEND_PORT=8000
FRONTEND_PORT=3000
MAX_UPLOAD_MB=10
```

## Working agreements

### Keep domain logic isolated
If a function is about SBOL object creation or validation, it should live in the Python package, not in the web layer.

### Keep SynBioHub logic behind a service layer
Direct HTTP calls to SynBioHub should not be scattered across route handlers.

### Prefer small, testable modules
Avoid giant files for routes, services, or components.

### Build the happy path first
Optimize for a working create-and-attach flow before adding extra polish.

## Suggested first implementation order

1. repository scaffold
2. package namespaces and factories
3. placement validation tests
4. backend stub auth and collection routes
5. frontend login and collection browser
6. create inventory endpoint in stub mode
7. image upload and success flow
8. real SynBioHub integration testing

## Testing priorities

### Package tests
- object factories create expected annotations
- placement validation behaves correctly
- serialization produces valid outputs

### Backend tests
- auth happy path in stub mode
- root and subcollection routes
- inventory create happy path
- invalid placement returns proper error

### Frontend tests
- collection selection behavior
- review page renders chosen metadata and images
- submit flow handles success response

## Code review checklist

- does the code respect package/backend/frontend boundaries?
- does the code introduce unnecessary coupling?
- are error states visible to users?
- are TODOs clearly marked when live SynBioHub testing is required?
- does the flow still work on a phone-sized viewport?

## Suggested first approach for implementation

import math
import sbol2 as sbol
from sbol2 import Config

# -----------------------------------------------------------------------------
# Namespace and RDF URIs
# -----------------------------------------------------------------------------

EX = "https://draggon.org/ns/inventory#"

SBOL_COLLECTION = "http://sbols.org/v2#Collection"
SBOL_IMPLEMENTATION = "http://sbols.org/v2#Implementation"
SBOL_COMPONENT_DEFINITION = "http://sbols.org/v2#ComponentDefinition"
SBOL_MODULE_DEFINITION = "http://sbols.org/v2#ModuleDefinition"

# -----------------------------------------------------------------------------
# Controlled terms for item kinds
# -----------------------------------------------------------------------------

EXTRACTED_PLASMID = EX + "ExtractedPlasmid"
BACTERIAL_STOCK = EX + "BacterialStock"
SOLID_MEDIA_PLATE = EX + "SolidMediaPlate"

# -----------------------------------------------------------------------------
# Controlled terms for storage kinds
# -----------------------------------------------------------------------------

FRIDGE_MINUS_80 = EX + "FridgeMinus80C"
FRIDGE_MINUS_20 = EX + "FridgeMinus20C"
FRIDGE_4C       = EX + "Fridge4C"       # added because SolidMediaPlate needs it
SHELF           = EX + "Shelf"
BOX             = EX + "Box"
SLOT            = EX + "Slot"

# -----------------------------------------------------------------------------
# Core override: all Implementations become InventoryImplementation
# -----------------------------------------------------------------------------

class InventoryImplementation(sbol.Implementation):
    """
    SBOL core type remains Implementation.
    Domain semantics are captured with extension properties.
    """

    def __init__(self, uri="example"):
        super().__init__(uri=uri)

        # Required domain type:
        #   ExtractedPlasmid | BacterialStock | SolidMediaPlate
        self.inventory_kind = sbol.URIProperty(
            self, EX + "inventoryKind", 1, 1, []
        )

        # Direct pointer to the leaf storage Collection (usually a Slot)
        self.stored_at = sbol.ReferencedObject(
            self, EX + "storedAt", SBOL_COLLECTION, 0, 1, []
        )

        # Optional operational metadata
        self.barcode = sbol.TextProperty(
            self, EX + "barcode", 0, 1, []
        )
        self.lot_id = sbol.TextProperty(
            self, EX + "lotId", 0, 1, []
        )
        self.notes = sbol.TextProperty(
            self, EX + "notes", 0, 1, []
        )
        self.freeze_date = sbol.DateTimeProperty(
            self, EX + "freezeDate", 0, 1, []
        )


# -----------------------------------------------------------------------------
# Core override: all Collections become StorageCollection
# -----------------------------------------------------------------------------

class StorageCollection(sbol.Collection):
    """
    SBOL core type remains Collection.
    Domain semantics are captured with extension properties.
    """

    def __init__(self, uri="example"):
        super().__init__(uri=uri)

        # Required domain type:
        #   FridgeMinus80C | FridgeMinus20C | Fridge4C | Shelf | Box | Slot
        self.storage_kind = sbol.URIProperty(
            self, EX + "storageKind", 1, 1, []
        )

        # Optional reverse pointer to the parent Collection
        self.parent_storage = sbol.ReferencedObject(
            self, EX + "parentStorage", SBOL_COLLECTION, 0, 1, []
        )

        # Optional metadata
        self.temperature_c = sbol.IntProperty(
            self, EX + "temperatureC", 0, 1, []
        )
        self.label = sbol.TextProperty(
            self, EX + "label", 0, 1, []
        )

        # For Slot or Box coordinates
        self.row = sbol.TextProperty(
            self, EX + "row", 0, 1, []
        )
        self.column = sbol.TextProperty(
            self, EX + "column", 0, 1, []
        )

        # Which item kinds are allowed here?
        self.allowed_item_kinds = sbol.URIProperty(
            self, EX + "allowedItemKind", 0, math.inf, []
        )


# -----------------------------------------------------------------------------
# Register the override classes with the parser
# -----------------------------------------------------------------------------

Config.register_extension_class(InventoryImplementation, SBOL_IMPLEMENTATION)
Config.register_extension_class(StorageCollection, SBOL_COLLECTION)

# -----------------------------------------------------------------------------
# Factory functions for concrete storage nodes
# -----------------------------------------------------------------------------

def make_fridge_minus80(uri: str) -> StorageCollection:
    x = StorageCollection(uri)
    x.storage_kind = FRIDGE_MINUS_80
    x.temperature_c = -80
    x.allowed_item_kinds = [BACTERIAL_STOCK]
    return x

def make_fridge_minus20(uri: str) -> StorageCollection:
    x = StorageCollection(uri)
    x.storage_kind = FRIDGE_MINUS_20
    x.temperature_c = -20
    x.allowed_item_kinds = [EXTRACTED_PLASMID]
    return x

def make_fridge_4c(uri: str) -> StorageCollection:
    x = StorageCollection(uri)
    x.storage_kind = FRIDGE_4C
    x.temperature_c = 4
    x.allowed_item_kinds = [SOLID_MEDIA_PLATE]
    return x

def make_shelf(uri: str, label: str = None) -> StorageCollection:
    x = StorageCollection(uri)
    x.storage_kind = SHELF
    if label:
        x.label = label
    return x

def make_box(uri: str, label: str = None) -> StorageCollection:
    x = StorageCollection(uri)
    x.storage_kind = BOX
    if label:
        x.label = label
    return x

def make_slot(
    uri: str,
    label: str = None,
    row: str = None,
    column: str = None,
    allowed_item_kinds=None,
) -> StorageCollection:
    x = StorageCollection(uri)
    x.storage_kind = SLOT
    if label:
        x.label = label
    if row:
        x.row = row
    if column:
        x.column = column
    if allowed_item_kinds:
        x.allowed_item_kinds = allowed_item_kinds
    return x


# -----------------------------------------------------------------------------
# Factory functions for concrete implementations
# -----------------------------------------------------------------------------

def make_extracted_plasmid(
    uri: str,
    plasmid_cd_uri,
    slot_uri=None,
    design_uri=None,
) -> InventoryImplementation:
    """
    built -> ComponentDefinition for plasmid physical prep
    wasDerivedFroms -> optional original design
    """
    x = InventoryImplementation(uri)
    x.inventory_kind = EXTRACTED_PLASMID
    x.built = plasmid_cd_uri
    if slot_uri:
        x.stored_at = slot_uri
    if design_uri:
        x.wasDerivedFroms = [design_uri]
    return x

def make_bacterial_stock(
    uri: str,
    strain_md_uri,
    slot_uri=None,
    design_uri=None,
) -> InventoryImplementation:
    """
    built -> ModuleDefinition for strain
    """
    x = InventoryImplementation(uri)
    x.inventory_kind = BACTERIAL_STOCK
    x.built = strain_md_uri
    if slot_uri:
        x.stored_at = slot_uri
    if design_uri:
        x.wasDerivedFroms = [design_uri]
    return x

def make_solid_media_plate(
    uri: str,
    plate_md_uri,
    slot_uri=None,
    design_uri=None,
) -> InventoryImplementation:
    """
    built -> ModuleDefinition for plate
    """
    x = InventoryImplementation(uri)
    x.inventory_kind = SOLID_MEDIA_PLATE
    x.built = plate_md_uri
    if slot_uri:
        x.stored_at = slot_uri
    if design_uri:
        x.wasDerivedFroms = [design_uri]
    return x


# -----------------------------------------------------------------------------
# Convenience helpers for containment
# -----------------------------------------------------------------------------

def add_child(parent: StorageCollection, child):
    """
    child can be StorageCollection or InventoryImplementation.
    Uses native Collection.members to represent containment.
    """
    parent.members.add(child.identity)
    if isinstance(child, StorageCollection):
        child.parent_storage = parent.identity

def place_item(slot: StorageCollection, item: InventoryImplementation):
    """
    Place an inventory item into a leaf Slot.
    """
    slot.members.add(item.identity)
    item.stored_at = slot.identity


# -----------------------------------------------------------------------------
# Optional validation helpers
# -----------------------------------------------------------------------------

def validate_item(item: InventoryImplementation):
    """
    Application-level semantic checks.
    """
    kind = str(item.inventory_kind)

    if kind == EXTRACTED_PLASMID:
        # expected built -> ComponentDefinition
        pass

    elif kind == BACTERIAL_STOCK:
        # expected built -> ModuleDefinition
        pass

    elif kind == SOLID_MEDIA_PLATE:
        # expected built -> ModuleDefinition
        pass

def validate_placement(item: InventoryImplementation, slot: StorageCollection):
    """
    Application-level semantic checks between item and storage node.
    """
    allowed = set(slot.allowed_item_kinds)
    if allowed and str(item.inventory_kind) not in allowed:
        raise ValueError(
            f"{item.identity} of kind {item.inventory_kind} "
            f"is not allowed in slot {slot.identity}"
        )


