from fastapi import APIRouter, Query

from app.schemas import CollectionListResponse, CollectionNode
from app.services.synbiohub_client import synbiohub_client

router = APIRouter(prefix="/api/collections", tags=["collections"])


@router.get("/root", response_model=CollectionListResponse)
def get_root_collections() -> CollectionListResponse:
    return CollectionListResponse(items=[CollectionNode(**item) for item in synbiohub_client.get_root_collections()])


@router.get("/subcollections", response_model=CollectionListResponse)
def get_subcollections(uri: str = Query(...)) -> CollectionListResponse:
    return CollectionListResponse(items=[CollectionNode(**item) for item in synbiohub_client.get_subcollections(uri)])
