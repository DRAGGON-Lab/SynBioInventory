"""FastAPI app entrypoint for SynBioInventory backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.services.inventory_service import InventoryService
from app.services.synbiohub_client import SynBioHubClient

_synbiohub_client = SynBioHubClient(base_url=settings.base_url, use_stub=settings.use_stub)
_inventory_service = InventoryService(_synbiohub_client)


def get_synbiohub_client() -> SynBioHubClient:
    return _synbiohub_client


def get_inventory_service() -> InventoryService:
    return _inventory_service


app = FastAPI(title="SynBioInventory API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api import routes_auth, routes_collections, routes_inventory  # noqa: E402

app.include_router(routes_auth.router)
app.include_router(routes_collections.router)
app.include_router(routes_inventory.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
