from fastapi import APIRouter, HTTPException, Query, Request

from app.schemas.collections import CollectionNode

router = APIRouter(prefix="/api/collections", tags=["collections"])


def _require_token(request: Request) -> str:
    session = request.app.state.session
    if not session:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return session["token"]


@router.get("/root", response_model=list[CollectionNode])
def root_collections(request: Request) -> list[CollectionNode]:
    token = _require_token(request)
    result = request.app.state.synbiohub_client.get_root_collections(token)
    request.app.state.collection_index.update({item["uri"]: item for item in result})
    return [CollectionNode(**item) for item in result]


@router.get("/subcollections", response_model=list[CollectionNode])
def subcollections(request: Request, uri: str = Query(...)) -> list[CollectionNode]:
    token = _require_token(request)
    result = request.app.state.synbiohub_client.get_subcollections(token, uri)
    request.app.state.collection_index.update({item["uri"]: item for item in result})
    return [CollectionNode(**item) for item in result]
