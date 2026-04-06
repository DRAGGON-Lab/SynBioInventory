from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_auth import router as auth_router
from app.api.routes_collections import router as collections_router
from app.api.routes_inventory import router as inventory_router
from app.config import settings

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(collections_router)
app.include_router(inventory_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
