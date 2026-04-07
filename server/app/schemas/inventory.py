from pydantic import BaseModel, Field


class InventoryTypeSummary(BaseModel):
    key: str
    label: str


class InventoryCreateResult(BaseModel):
    created_uri: str
    destination_collection_uri: str
    implementation_type: str
    attached_images: int
    message: str
    rdf_xml_preview: str = Field(description="Shortened RDF/XML payload for transparency")
