from fastapi import APIRouter, File, Form, UploadFile

from app.schemas import InventoryCreateResponse, InventoryTypeOption
from app.services.inventory_service import InventoryService
from app.services.synbiohub_client import synbiohub_client

router = APIRouter(prefix="/api/inventory", tags=["inventory"])
inventory_service = InventoryService(synbiohub_client)


@router.get("/types", response_model=list[InventoryTypeOption])
def list_inventory_types() -> list[InventoryTypeOption]:
    return [
        InventoryTypeOption(key="ExtractedPlasmid", label="Extracted Plasmid"),
        InventoryTypeOption(key="BacterialStock", label="Bacterial Stock"),
        InventoryTypeOption(key="SolidMediaPlate", label="Solid Media Plate"),
    ]


@router.post("/create", response_model=InventoryCreateResponse)
async def create_inventory(
    destination_collection_uri: str = Form(...),
    implementation_type: str = Form(...),
    name: str | None = Form(default=None),
    notes: str | None = Form(default=None),
    barcode: str | None = Form(default=None),
    lot_id: str | None = Form(default=None),
    built_uri: str | None = Form(default=None),
    images: list[UploadFile] = File(default_factory=list),
) -> InventoryCreateResponse:
    result = await inventory_service.create_inventory(
        destination_collection_uri=destination_collection_uri,
        implementation_type=implementation_type,
        images=images,
        name=name,
        notes=notes,
        barcode=barcode,
        lot_id=lot_id,
        built_uri=built_uri,
    )
    return InventoryCreateResponse(**result)
