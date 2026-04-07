"""SynBioHub client abstraction with local stub support."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4


@dataclass
class SessionIdentity:
    username: str
    token: str


class SynBioHubClient:
    def __init__(self, base_url: str, use_stub: bool = True):
        self.base_url = base_url.rstrip("/")
        self.use_stub = use_stub

    def login(self, username: str, password: str) -> SessionIdentity:
        if self.use_stub:
            return SessionIdentity(username=username, token=f"stub-token-{uuid4().hex}")

        # TODO: Validate exact auth endpoint and payload format against target SynBioHub.
        if not password:
            raise ValueError("Invalid credentials")
        return SessionIdentity(username=username, token=f"live-token-{uuid4().hex}")

    def logout(self, _token: str) -> None:
        if self.use_stub:
            return
        # TODO: call SynBioHub logout endpoint once live integration is validated.

    def get_root_collections(self, _token: str) -> list[dict[str, object]]:
        if self.use_stub:
            return [
                {
                    "uri": "https://stub.synbiohub.org/collections/fridge-80",
                    "display_id": "fridge_80",
                    "name": "Main -80C Freezer",
                    "description": "Primary bacterial stock freezer",
                    "has_subcollections": True,
                    "storage_kind": "FridgeMinus80C",
                },
                {
                    "uri": "https://stub.synbiohub.org/collections/fridge-20",
                    "display_id": "fridge_20",
                    "name": "Main -20C Freezer",
                    "description": "Extracted plasmid freezer",
                    "has_subcollections": True,
                    "storage_kind": "FridgeMinus20C",
                },
                {
                    "uri": "https://stub.synbiohub.org/collections/fridge-4",
                    "display_id": "fridge_4",
                    "name": "Main 4C Fridge",
                    "description": "Solid media storage",
                    "has_subcollections": True,
                    "storage_kind": "Fridge4C",
                },
            ]

        # TODO: fetch from live SynBioHub collections endpoint.
        return []

    def get_subcollections(self, _token: str, uri: str) -> list[dict[str, object]]:
        if self.use_stub:
            children = {
                "https://stub.synbiohub.org/collections/fridge-80": [
                    {
                        "uri": "https://stub.synbiohub.org/collections/fridge-80/shelf-a",
                        "display_id": "shelf_a",
                        "name": "Shelf A",
                        "description": "Top shelf",
                        "has_subcollections": True,
                        "storage_kind": "Shelf",
                    }
                ],
                "https://stub.synbiohub.org/collections/fridge-80/shelf-a": [
                    {
                        "uri": "https://stub.synbiohub.org/collections/fridge-80/shelf-a/box-1",
                        "display_id": "box_1",
                        "name": "Box 1",
                        "description": "Cryobox",
                        "has_subcollections": True,
                        "storage_kind": "Box",
                    }
                ],
                "https://stub.synbiohub.org/collections/fridge-80/shelf-a/box-1": [
                    {
                        "uri": "https://stub.synbiohub.org/collections/fridge-80/shelf-a/box-1/slot-a1",
                        "display_id": "slot_a1",
                        "name": "Slot A1",
                        "description": "Slot A1",
                        "has_subcollections": False,
                        "storage_kind": "FridgeMinus80C",
                    }
                ],
            }
            return children.get(uri, [])

        # TODO: fetch from live SynBioHub subcollection endpoint.
        return []

    def submit_inventory_sbol(self, _token: str, sbol_rdfxml: str, fallback_uri: str) -> str:
        if self.use_stub:
            return fallback_uri

        # TODO: submit SBOL payload and parse created URI.
        _ = sbol_rdfxml
        return fallback_uri

    def attach_image(self, _token: str, _object_uri: str, _filename: str, _blob: bytes) -> None:
        if self.use_stub:
            return
        # TODO: call SynBioHub attachment endpoint for binary payload.
