from pydantic import BaseModel


class InventoryType(BaseModel):
    key: str
    label: str


class InventoryCreateResponse(BaseModel):
    created_uri: str
    destination_collection_uri: str
    implementation_type: str
    attached_images: int
    message: str


class ErrorResponse(BaseModel):
    error: dict[str, str]
