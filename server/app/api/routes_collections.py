from fastapi import APIRouter, Query

from app.main import get_synbiohub_client
from app.schemas import CollectionSummary

router = APIRouter(prefix="/api/collections", tags=["collections"])


@router.get("/root", response_model=list[CollectionSummary])
def root_collections() -> list[CollectionSummary]:
    client = get_synbiohub_client()
    return [CollectionSummary(**item) for item in client.list_root_collections()]


@router.get("/subcollections", response_model=list[CollectionSummary])
def subcollections(uri: str = Query(..., description="Parent collection URI")) -> list[CollectionSummary]:
    client = get_synbiohub_client()
    return [CollectionSummary(**item) for item in client.list_subcollections(uri)]
