"""RDF/XML serialization helpers for MVP inventory payloads."""

from __future__ import annotations

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS

from . import namespaces as ns
from .schema import InventoryImplementation

SBOL = Namespace("http://sbols.org/v2#")
DRAGGON = Namespace(ns.DRAGGON_NS)


def serialize_inventory_to_rdfxml(implementation: InventoryImplementation) -> str:
    """Serialize an inventory implementation model to RDF/XML.

    Note: This helper emits minimal triples sufficient for MVP integration tests.
    TODO: Validate against target SynBioHub instance and expand required SBOL fields.
    """

    graph = Graph()
    graph.bind("sbol", SBOL)
    graph.bind("drag", DRAGGON)

    impl_ref = URIRef(implementation.uri)
    graph.add((impl_ref, RDF.type, SBOL.Implementation))
    graph.add((impl_ref, RDFS.label, Literal(implementation.name)))
    graph.add((impl_ref, URIRef(ns.PROP_INVENTORY_KIND), URIRef(f"{ns.DRAGGON_NS}{implementation.inventory_kind}")))
    graph.add((impl_ref, URIRef(ns.PROP_STORED_AT), URIRef(implementation.stored_at)))

    if implementation.built_uri:
        graph.add((impl_ref, SBOL.built, URIRef(implementation.built_uri)))
    if implementation.barcode:
        graph.add((impl_ref, URIRef(ns.PROP_BARCODE), Literal(implementation.barcode)))
    if implementation.lot_id:
        graph.add((impl_ref, URIRef(ns.PROP_LOT_ID), Literal(implementation.lot_id)))
    if implementation.notes:
        graph.add((impl_ref, URIRef(ns.PROP_NOTES), Literal(implementation.notes)))

    return graph.serialize(format="xml")
