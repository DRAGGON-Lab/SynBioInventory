"""Inventory orchestration service for create workflow."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from draggon_inventory_sbol import (
    PlacementValidationError,
    StorageCollection,
    implementation_to_rdfxml,
    make_bacterial_stock,
    make_extracted_plasmid,
    make_solid_media_plate,
    validate_placement,
)

from app.services.synbiohub_client import SynBioHubClient


@dataclass(slots=True)
class UploadedImage:
    filename: str
    content: bytes


@dataclass(slots=True)
class CreateInventoryCommand:
    destination_collection_uri: str
    destination_storage_kind: str
    implementation_type: str
    object_uri: str
    barcode: str | None = None
    lot_id: str | None = None
    notes: str | None = None
    built_uri: str | None = None


class InventoryService:
    def __init__(self, client: SynBioHubClient) -> None:
        self._client = client

    @staticmethod
    def list_types() -> list[dict[str, str]]:
        return [
            {"key": "ExtractedPlasmid", "label": "Extracted Plasmid"},
            {"key": "BacterialStock", "label": "Bacterial Stock"},
            {"key": "SolidMediaPlate", "label": "Solid Media Plate"},
        ]

    def create_inventory(
        self, command: CreateInventoryCommand, images: Iterable[UploadedImage]
    ) -> dict[str, object]:
        factory_map = {
            "ExtractedPlasmid": make_extracted_plasmid,
            "BacterialStock": make_bacterial_stock,
            "SolidMediaPlate": make_solid_media_plate,
        }
        factory = factory_map.get(command.implementation_type)
        if not factory:
            raise PlacementValidationError(
                f"Unsupported implementation type: {command.implementation_type}"
            )

        implementation = factory(
            uri=command.object_uri,
            stored_at=command.destination_collection_uri,
            barcode=command.barcode,
            lot_id=command.lot_id,
            notes=command.notes,
            built_uri=command.built_uri,
        )
        destination = StorageCollection(
            uri=command.destination_collection_uri,
            storage_kind=command.destination_storage_kind,
        )
        validate_placement(implementation, destination)

        rdf_xml = implementation_to_rdfxml(implementation)
        created_uri = self._client.submit_inventory_sbol(rdf_xml, preferred_uri=command.object_uri)

        image_count = 0
        for image in images:
            self._client.attach_image(created_uri, image.filename, image.content)
            image_count += 1

        return {
            "created_uri": created_uri,
            "destination_collection_uri": command.destination_collection_uri,
            "implementation_type": command.implementation_type,
            "attached_images": image_count,
            "message": "Inventory object created successfully",
            "rdf_xml_preview": rdf_xml[:500],
        }
