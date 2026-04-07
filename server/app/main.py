from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_auth import router as auth_router
from app.api.routes_collections import router as collections_router
from app.api.routes_inventory import router as inventory_router
from app.config import settings
from app.services.inventory_service import InventoryService
from app.services.synbiohub_client import SynBioHubClient


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.state.settings = settings
    app.state.synbiohub_client = SynBioHubClient(
        base_url=settings.synbiohub_base_url,
        use_stub=settings.synbiohub_use_stub,
    )
    app.state.inventory_service = InventoryService(app.state.synbiohub_client)
    app.state.session = None
    app.state.collection_index = {}

    app.include_router(auth_router)
    app.include_router(collections_router)
    app.include_router(inventory_router)

    @app.get("/healthz")
    def healthz() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
