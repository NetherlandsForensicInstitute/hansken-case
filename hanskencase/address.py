from uuid import uuid4
from hanskencase.utils import add_misc_map

from namespaces import KB, Literal, RDF, UCO_CORE, UCO_OBSERVABLE, UCO_LOCATION

from account import add_application_account_facet


def add_simple_address_facet(graph, trace):
    address_facet = KB[f"AddressFacet-{uuid4()}"]
    graph.add((address_facet, RDF.type, UCO_LOCATION.SimpleAddressFacet))

    # city (string) - The name of the city.
    city = trace.address.city
    if city:
        graph.add((address_facet, UCO_LOCATION.locality, Literal(city)))

    # country (string) - The name of the country.
    country = trace.address.country
    if country:
        graph.add((address_facet, UCO_LOCATION.country, Literal(country)))
    # street (string) - The name of the street.
    street = trace.address.street
    if street:
        graph.add((address_facet, UCO_LOCATION.street, Literal(street)))

    # type (string) - The type of the address, for instance home or work.
    address_type = trace.address.type
    if address_type:
        graph.add((address_facet, UCO_LOCATION.addressType, Literal(address_type)))
    # zipCode (string) - The zip-code.
    postalCode = trace.address.zipCode
    if postalCode:
        graph.add((address_facet, UCO_LOCATION.postalCode, Literal(postalCode)))

    return address_facet


def add_address(graph, trace):
    """A physical location in the world."""

    address = KB["Address-{uuid4()}"]
    address_facet = add_simple_address_facet(graph, trace)
    # application (string) - The application using the address.
    account_facet = add_application_account_facet(
        graph, trace
    )  # Or bind to application account?

    graph.add((address, RDF.type, UCO_LOCATION.SimpleAddress))
    graph.add((address, UCO_CORE.hasFacet, account_facet))
    graph.add((address, UCO_CORE.hasFacet, address_facet))

    # misc (map:string) - Additional information about the location.
    add_misc_map(graph, address, trace.address.misc)
