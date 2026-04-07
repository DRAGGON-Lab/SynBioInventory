from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.main import get_inventory_service
from app.schemas import InventoryCreateResult, InventoryTypeSummary
from app.services.inventory_service import CreateInventoryCommand, UploadedImage
from draggon_inventory_sbol.validation import PlacementValidationError

router = APIRouter(prefix="/api/inventory", tags=["inventory"])


@router.get("/types", response_model=list[InventoryTypeSummary])
def list_inventory_types() -> list[InventoryTypeSummary]:
    service = get_inventory_service()
    return [InventoryTypeSummary(**item) for item in service.list_types()]


@router.post("/create", response_model=InventoryCreateResult)
async def create_inventory(
    destination_collection_uri: str = Form(...),
    destination_storage_kind: str = Form(...),
    implementation_type: str = Form(...),
    object_uri: str = Form(...),
    barcode: str | None = Form(default=None),
    lot_id: str | None = Form(default=None),
    notes: str | None = Form(default=None),
    built_uri: str | None = Form(default=None),
    images: list[UploadFile] = File(default=[]),
) -> InventoryCreateResult:
    service = get_inventory_service()

    uploaded_images: list[UploadedImage] = []
    for image in images:
        uploaded_images.append(UploadedImage(filename=image.filename, content=await image.read()))

    command = CreateInventoryCommand(
        destination_collection_uri=destination_collection_uri,
        destination_storage_kind=destination_storage_kind,
        implementation_type=implementation_type,
        object_uri=object_uri,
        barcode=barcode,
        lot_id=lot_id,
        notes=notes,
        built_uri=built_uri,
    )

    try:
        result = service.create_inventory(command, uploaded_images)
    except PlacementValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return InventoryCreateResult(**result)
