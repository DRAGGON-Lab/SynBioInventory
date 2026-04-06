"""Minimal RDF/XML serialization helpers for MVP scaffolding.

TODO: Replace with pySBOL2-backed document serialization once live SynBioHub
integration details are validated.
"""

from __future__ import annotations

from xml.sax.saxutils import escape

from .schema import InventoryImplementation


def serialize_inventory_to_rdf_xml(implementation: InventoryImplementation) -> str:
    """Serialize a minimal RDF/XML fragment for a single implementation."""

    data = {
        "uri": implementation.uri,
        "kind": implementation.inventory_kind,
        "stored_at": implementation.stored_at,
        "built_uri": implementation.built_uri,
        "barcode": implementation.barcode,
        "lot_id": implementation.lot_id,
        "notes": implementation.notes,
        "name": implementation.name,
    }

    optional_tags = "\n".join(
        f"    <draggon:{key}>{escape(str(value))}</draggon:{key}>"
        for key, value in data.items()
        if key not in {"uri", "kind", "stored_at"} and value
    )

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:sbol="http://sbols.org/v2#"
         xmlns:draggon="https://draggon.org/ns/inventory#">
  <sbol:Implementation rdf:about="{escape(data['uri'])}">
    <draggon:inventory_kind>{escape(str(data['kind']))}</draggon:inventory_kind>
    <draggon:stored_at rdf:resource="{escape(data['stored_at'])}" />
{optional_tags}
  </sbol:Implementation>
</rdf:RDF>
'''
