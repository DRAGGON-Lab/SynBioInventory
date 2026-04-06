from pydantic import BaseModel


class InventoryTypeOption(BaseModel):
    key: str
    label: str


class InventoryCreateResponse(BaseModel):
    created_uri: str
    destination_collection_uri: str
    implementation_type: str
    attached_images: int
    message: str
