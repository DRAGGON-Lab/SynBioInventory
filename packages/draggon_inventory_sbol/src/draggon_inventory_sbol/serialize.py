"""Serialization helpers for inventory SBOL domain objects."""

from rdflib import Graph, Literal, RDF, URIRef

from draggon_inventory_sbol.namespaces import DRAGGON, SBOL2
from draggon_inventory_sbol.schema import InventoryImplementation


def implementation_to_rdfxml(implementation: InventoryImplementation) -> str:
    """Serialize an inventory implementation to RDF/XML.

    This is a minimal MVP representation that encodes an SBOL Implementation
    plus extension properties.
    """

    impl_uri = URIRef(implementation.uri)
    g = Graph()
    g.bind("sbol", SBOL2)
    g.bind("draggon", DRAGGON)
    g.add((impl_uri, RDF.type, SBOL2.Implementation))
    g.add((impl_uri, DRAGGON.inventory_kind, URIRef(DRAGGON[implementation.inventory_kind])))
    g.add((impl_uri, DRAGGON.stored_at, URIRef(implementation.stored_at)))

    if implementation.built_uri:
        g.add((impl_uri, SBOL2.built, URIRef(implementation.built_uri)))
    if implementation.barcode:
        g.add((impl_uri, DRAGGON.barcode, Literal(implementation.barcode)))
    if implementation.lot_id:
        g.add((impl_uri, DRAGGON.lot_id, Literal(implementation.lot_id)))
    if implementation.notes:
        g.add((impl_uri, DRAGGON.notes, Literal(implementation.notes)))

    return g.serialize(format="xml")
