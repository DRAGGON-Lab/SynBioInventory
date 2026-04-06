from pydantic import BaseModel


class CollectionNode(BaseModel):
    uri: str
    display_id: str
    name: str
    description: str | None = None
    has_subcollections: bool = False
    storage_kind: str


class CollectionListResponse(BaseModel):
    items: list[CollectionNode]
