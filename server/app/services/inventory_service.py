"""Inventory creation orchestration service."""

from __future__ import annotations

from uuid import uuid4

from draggon_inventory_sbol import (
    InventoryKind,
    StorageKind,
    make_bacterial_stock,
    make_extracted_plasmid,
    make_solid_media_plate,
    serialize_inventory_to_rdf_xml,
    validate_placement,
)
from fastapi import HTTPException, UploadFile

from app.services.synbiohub_client import SynBioHubClient


class InventoryService:
    def __init__(self, synbiohub: SynBioHubClient) -> None:
        self.synbiohub = synbiohub

    def _build_implementation(self, implementation_type: str, **kwargs: str | None):
        if implementation_type == InventoryKind.EXTRACTED_PLASMID:
            return make_extracted_plasmid(**kwargs)
        if implementation_type == InventoryKind.BACTERIAL_STOCK:
            return make_bacterial_stock(**kwargs)
        if implementation_type == InventoryKind.SOLID_MEDIA_PLATE:
            return make_solid_media_plate(**kwargs)
        raise HTTPException(status_code=400, detail=f"Unsupported implementation type: {implementation_type}")

    async def create_inventory(
        self,
        destination_collection_uri: str,
        implementation_type: str,
        images: list[UploadFile],
        *,
        name: str | None = None,
        notes: str | None = None,
        barcode: str | None = None,
        lot_id: str | None = None,
        built_uri: str | None = None,
    ) -> dict:
        top_level = self.synbiohub.get_top_level_storage_kind(destination_collection_uri)
        if not top_level:
            raise HTTPException(status_code=400, detail="Unknown destination collection")

        implementation = self._build_implementation(
            implementation_type,
            uri=f"urn:uuid:{uuid4()}",
            stored_at=destination_collection_uri,
            built_uri=built_uri,
            barcode=barcode,
            lot_id=lot_id,
            notes=notes,
            name=name,
        )

        try:
            validate_placement(implementation, StorageKind(top_level))
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

        sbol_xml = serialize_inventory_to_rdf_xml(implementation)
        created_uri = self.synbiohub.submit_sbol_document(sbol_xml, name)

        attached_images = 0
        for image in images:
            content = await image.read()
            self.synbiohub.attach_image(created_uri, image.filename or "image.bin", content)
            attached_images += 1

        return {
            "created_uri": created_uri,
            "destination_collection_uri": destination_collection_uri,
            "implementation_type": implementation_type,
            "attached_images": attached_images,
            "message": "Inventory object created successfully",
        }
