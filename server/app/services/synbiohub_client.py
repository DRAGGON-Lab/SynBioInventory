"""SynBioHub service abstraction with local stub mode support."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class SynBioHubClient:
    base_url: str
    use_stub: bool = True

    _token: str | None = None
    _username: str | None = None

    def login(self, username: str, password: str) -> bool:
        """Authenticate against SynBioHub or local stub."""
        if self.use_stub:
            self._token = f"stub-token-{uuid4()}"
            self._username = username
            return True

        # TODO: implement live SynBioHub auth exchange and token parsing.
        raise NotImplementedError("Live SynBioHub auth is not implemented yet")

    def logout(self) -> None:
        self._token = None
        self._username = None

    def current_user(self) -> str | None:
        return self._username

    def is_authenticated(self) -> bool:
        return self._token is not None

    def list_root_collections(self) -> list[dict[str, Any]]:
        if self.use_stub:
            return [
                {
                    "uri": f"{self.base_url}/public/FridgeMinus80C",
                    "display_id": "FridgeMinus80C",
                    "name": "-80C Freezer",
                    "description": "Cryostock storage",
                    "has_subcollections": True,
                },
                {
                    "uri": f"{self.base_url}/public/FridgeMinus20C",
                    "display_id": "FridgeMinus20C",
                    "name": "-20C Freezer",
                    "description": "Plasmid prep storage",
                    "has_subcollections": True,
                },
                {
                    "uri": f"{self.base_url}/public/Fridge4C",
                    "display_id": "Fridge4C",
                    "name": "4C Fridge",
                    "description": "Plate storage",
                    "has_subcollections": True,
                },
            ]

        # TODO: map real SynBioHub collection payloads into CollectionSummary shape.
        raise NotImplementedError("Live SynBioHub collection listing not implemented")

    def list_subcollections(self, uri: str) -> list[dict[str, Any]]:
        if self.use_stub:
            if uri.endswith("FridgeMinus80C"):
                return [
                    {
                        "uri": f"{uri}/ShelfA",
                        "display_id": "ShelfA",
                        "name": "Shelf A",
                        "description": None,
                        "has_subcollections": True,
                    }
                ]
            if uri.endswith("ShelfA"):
                return [
                    {
                        "uri": f"{uri}/Box1",
                        "display_id": "Box1",
                        "name": "Box 1",
                        "description": None,
                        "has_subcollections": True,
                    }
                ]
            if uri.endswith("Box1"):
                return [
                    {
                        "uri": f"{uri}/SlotA1",
                        "display_id": "SlotA1",
                        "name": "Slot A1",
                        "description": None,
                        "has_subcollections": False,
                    }
                ]
            return []

        # TODO: fetch subcollections using SynBioHub API and pagination.
        raise NotImplementedError("Live SynBioHub subcollection listing not implemented")

    def submit_inventory_sbol(self, rdf_xml: str, preferred_uri: str | None = None) -> str:
        if self.use_stub:
            tail = preferred_uri or f"inventory_{uuid4().hex[:8]}"
            return f"{self.base_url}/user/{tail}"

        # TODO: submit RDF/XML payload to SynBioHub and parse created URI.
        raise NotImplementedError("Live SynBioHub SBOL submission not implemented")

    def attach_image(self, created_uri: str, filename: str, content: bytes) -> None:
        if self.use_stub:
            return

        # TODO: attach binary files to SynBioHub object endpoint.
        raise NotImplementedError("Live SynBioHub attachment upload not implemented")
