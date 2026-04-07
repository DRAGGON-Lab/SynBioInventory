from pydantic import BaseModel


class CollectionSummary(BaseModel):
    uri: str
    display_id: str
    name: str
    description: str | None = None
    has_subcollections: bool = False
