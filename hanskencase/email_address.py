from uuid import uuid4

from .namespaces import KB, Literal, UCO_CORE, UCO_OBSERVABLE, RDF


def add_email_address_facet(graph, address: str, display_name: str = None):
    if display_name is None:
        m = rgx.match(address)
        if m:
            address = m[1]
            display_name = m[2]

    email_address_facet = KB[f"EmailAddressFacet-{uuid4()}"]
    graph.add((email_address_facet, RDF.type, UCO_OBSERVABLE.EmailAddressFacet))

    graph.add((email_address_facet, UCO_OBSERVABLE.addressValue, Literal(address)))

    if display_name is not None:
        graph.add(
            (email_address_facet, UCO_OBSERVABLE.displayName, Literal(display_name))
        )

    return email_address_facet


import re

rgx = re.compile('"(.*)".*<(.*)>')


def add_email_address(graph, address: str, display_name: str = None):
    email_address = KB[f"EmailAddress-{uuid4()}"]
    email_address_facet = add_email_address_facet(graph, address, display_name)

    graph.add((email_address, RDF.type, UCO_OBSERVABLE.EmailAddress))
    graph.add((email_address, UCO_CORE.hasFacet, email_address_facet))

    return email_address


def get_email_address_facet(graph, facet_subject):
    data = {}

    address = graph.value(facet_subject, UCO_OBSERVABLE.addressValue)
    if address is not None:
        data["address"] = address

    dn = graph.value(facet_subject, UCO_OBSERVABLE.displayName)
    if dn is not None:
        data["displayName"] = dn

    return data


def get_email_address(graph, address_subject):
    email_facet = graph.value(address_subject, UCO_CORE.hasFacet)
    return get_email_address_facet(graph, email_facet)
