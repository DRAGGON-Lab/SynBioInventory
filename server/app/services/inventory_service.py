"""Service orchestrating inventory creation flow."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4

from draggon_inventory_sbol import (
    StorageCollection,
    make_bacterial_stock,
    make_extracted_plasmid,
    make_solid_media_plate,
    serialize_inventory_to_rdfxml,
    validate_placement,
)

from .synbiohub_client import SynBioHubClient


@dataclass(slots=True)
class UploadedImage:
    filename: str
    content: bytes


class InventoryService:
    def __init__(self, synbiohub_client: SynBioHubClient):
        self.synbiohub_client = synbiohub_client

    def list_inventory_types(self) -> list[dict[str, str]]:
        return [
            {"key": "ExtractedPlasmid", "label": "Extracted Plasmid"},
            {"key": "BacterialStock", "label": "Bacterial Stock"},
            {"key": "SolidMediaPlate", "label": "Solid Media Plate"},
        ]

    def create_inventory(
        self,
        *,
        token: str,
        destination_collection_uri: str,
        destination_storage_kind: str,
        implementation_type: str,
        name: str | None,
        built_uri: str | None,
        barcode: str | None,
        lot_id: str | None,
        notes: str | None,
        images: list[UploadedImage],
    ) -> dict[str, object]:
        created_uri = f"https://stub.synbiohub.org/inventory/{uuid4().hex}"
        display_name = name or f"{implementation_type}-{uuid4().hex[:8]}"

        if implementation_type == "ExtractedPlasmid":
            implementation = make_extracted_plasmid(
                uri=created_uri,
                name=display_name,
                stored_at=destination_collection_uri,
                built_uri=built_uri,
                barcode=barcode,
                lot_id=lot_id,
                notes=notes,
            )
        elif implementation_type == "BacterialStock":
            implementation = make_bacterial_stock(
                uri=created_uri,
                name=display_name,
                stored_at=destination_collection_uri,
                built_uri=built_uri,
                barcode=barcode,
                lot_id=lot_id,
                notes=notes,
            )
        elif implementation_type == "SolidMediaPlate":
            implementation = make_solid_media_plate(
                uri=created_uri,
                name=display_name,
                stored_at=destination_collection_uri,
                built_uri=built_uri,
                barcode=barcode,
                lot_id=lot_id,
                notes=notes,
            )
        else:
            raise ValueError(f"Unsupported implementation type: {implementation_type}")

        validate_placement(
            implementation,
            StorageCollection(
                uri=destination_collection_uri,
                name="destination",
                storage_kind=destination_storage_kind,
            ),
        )

        sbol_payload = serialize_inventory_to_rdfxml(implementation)
        created_uri = self.synbiohub_client.submit_inventory_sbol(token, sbol_payload, created_uri)

        for image in images:
            self.synbiohub_client.attach_image(token, created_uri, image.filename, image.content)

        return {
            "created_uri": created_uri,
            "destination_collection_uri": destination_collection_uri,
            "implementation_type": implementation_type,
            "attached_images": len(images),
            "message": "Inventory object created successfully",
        }
