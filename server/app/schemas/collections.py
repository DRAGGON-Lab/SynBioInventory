from pydantic import BaseModel


class CollectionNode(BaseModel):
    uri: str
    display_id: str
    name: str
    description: str | None = None
    has_subcollections: bool
    storage_kind: str | None = None
