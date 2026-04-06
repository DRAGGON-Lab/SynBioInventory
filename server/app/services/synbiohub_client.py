"""SynBioHub client abstraction.

In stub mode this returns deterministic data to unblock full-stack development.
TODO: Validate endpoint contracts against a real SynBioHub deployment.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4

from app.config import settings


@dataclass(slots=True)
class Session:
    session_id: str
    username: str
    synbiohub_token: str


class SynBioHubClient:
    def __init__(self) -> None:
        self._sessions: dict[str, Session] = {}
        self._stub_collections: dict[str, dict] = {
            "https://example.org/storage/fridge-80": {
                "uri": "https://example.org/storage/fridge-80",
                "display_id": "fridge_minus_80",
                "name": "-80C Freezer",
                "description": "Primary bacterial stock freezer",
                "has_subcollections": True,
                "storage_kind": "FridgeMinus80C",
                "parent": None,
            },
            "https://example.org/storage/fridge-20": {
                "uri": "https://example.org/storage/fridge-20",
                "display_id": "fridge_minus_20",
                "name": "-20C Freezer",
                "description": "Extracted plasmid freezer",
                "has_subcollections": True,
                "storage_kind": "FridgeMinus20C",
                "parent": None,
            },
            "https://example.org/storage/fridge-4": {
                "uri": "https://example.org/storage/fridge-4",
                "display_id": "fridge_4c",
                "name": "4C Fridge",
                "description": "Plate storage",
                "has_subcollections": True,
                "storage_kind": "Fridge4C",
                "parent": None,
            },
            "https://example.org/storage/fridge-80/shelf-a": {
                "uri": "https://example.org/storage/fridge-80/shelf-a",
                "display_id": "shelf_a",
                "name": "Shelf A",
                "description": None,
                "has_subcollections": True,
                "storage_kind": "Shelf",
                "parent": "https://example.org/storage/fridge-80",
            },
            "https://example.org/storage/fridge-80/shelf-a/box-1": {
                "uri": "https://example.org/storage/fridge-80/shelf-a/box-1",
                "display_id": "box_1",
                "name": "Box 1",
                "description": None,
                "has_subcollections": True,
                "storage_kind": "Box",
                "parent": "https://example.org/storage/fridge-80/shelf-a",
            },
            "https://example.org/storage/fridge-80/shelf-a/box-1/slot-a1": {
                "uri": "https://example.org/storage/fridge-80/shelf-a/box-1/slot-a1",
                "display_id": "slot_a1",
                "name": "Slot A1",
                "description": None,
                "has_subcollections": False,
                "storage_kind": "Slot",
                "parent": "https://example.org/storage/fridge-80/shelf-a/box-1",
            },
        }

    def login(self, username: str, password: str) -> Session:
        # TODO: Replace with live SynBioHub auth call in non-stub mode.
        if not settings.use_stub_synbiohub and not password:
            raise ValueError("Password required in live mode")
        session = Session(session_id=str(uuid4()), username=username, synbiohub_token=f"stub-{uuid4()}")
        self._sessions[session.session_id] = session
        return session

    def logout(self, session_id: str) -> None:
        self._sessions.pop(session_id, None)

    def get_session(self, session_id: str | None) -> Session | None:
        if not session_id:
            return None
        return self._sessions.get(session_id)

    def get_root_collections(self) -> list[dict]:
        return [c for c in self._stub_collections.values() if c["parent"] is None]

    def get_subcollections(self, uri: str) -> list[dict]:
        return [c for c in self._stub_collections.values() if c["parent"] == uri]

    def get_collection(self, uri: str) -> dict | None:
        return self._stub_collections.get(uri)

    def get_top_level_storage_kind(self, uri: str) -> str | None:
        current = self._stub_collections.get(uri)
        while current:
            parent = current.get("parent")
            if parent is None:
                return current["storage_kind"]
            current = self._stub_collections.get(parent)
        return None

    def submit_sbol_document(self, sbol_xml: str, implementation_name: str | None) -> str:
        # TODO: Replace with actual SynBioHub submission endpoint behavior.
        slug = implementation_name or "inventory"
        return f"https://example.org/user/{slug}-{uuid4().hex[:8]}"

    def attach_image(self, created_uri: str, filename: str, content: bytes) -> None:
        # TODO: Replace with real SynBioHub attachment endpoint once validated.
        _ = (created_uri, filename, len(content))


synbiohub_client = SynBioHubClient()
