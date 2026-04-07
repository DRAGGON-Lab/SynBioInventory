from fastapi import APIRouter, File, Form, HTTPException, Request, UploadFile

from app.schemas.inventory import InventoryCreateResponse, InventoryType
from app.services.inventory_service import UploadedImage
from draggon_inventory_sbol.validation import PlacementValidationError

router = APIRouter(prefix="/api/inventory", tags=["inventory"])


def _require_token(request: Request) -> str:
    session = request.app.state.session
    if not session:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return session["token"]


@router.get("/types", response_model=list[InventoryType])
def inventory_types(request: Request) -> list[InventoryType]:
    types = request.app.state.inventory_service.list_inventory_types()
    return [InventoryType(**item) for item in types]


@router.post("/create", response_model=InventoryCreateResponse)
async def create_inventory(
    request: Request,
    destination_collection_uri: str = Form(...),
    implementation_type: str = Form(...),
    name: str | None = Form(None),
    notes: str | None = Form(None),
    built_uri: str | None = Form(None),
    barcode: str | None = Form(None),
    lot_id: str | None = Form(None),
    images: list[UploadFile] = File(default=[]),
) -> InventoryCreateResponse:
    token = _require_token(request)
    collection_index = request.app.state.collection_index
    collection_meta = collection_index.get(destination_collection_uri)
    if not collection_meta:
        raise HTTPException(status_code=400, detail="Unknown destination collection URI")

    uploaded_images: list[UploadedImage] = []
    max_bytes = request.app.state.settings.max_upload_mb * 1024 * 1024
    for image in images:
        content = await image.read()
        if len(content) > max_bytes:
            raise HTTPException(status_code=400, detail=f"Image {image.filename} exceeds size limit")
        uploaded_images.append(UploadedImage(filename=image.filename or "upload.bin", content=content))

    try:
        result = request.app.state.inventory_service.create_inventory(
            token=token,
            destination_collection_uri=destination_collection_uri,
            destination_storage_kind=collection_meta.get("storage_kind") or "Slot",
            implementation_type=implementation_type,
            name=name,
            built_uri=built_uri,
            barcode=barcode,
            lot_id=lot_id,
            notes=notes,
            images=uploaded_images,
        )
    except PlacementValidationError as exc:
        raise HTTPException(
            status_code=400,
            detail={"code": "INVALID_PLACEMENT", "message": str(exc)},
        ) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return InventoryCreateResponse(**result)
