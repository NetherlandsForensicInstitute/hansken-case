from uuid import uuid4

from rdflib import Graph
from hansken.trace import Trace

from .namespaces import KB, RDF, UCO_OBSERVABLE, UCO_CORE, Literal
from .utils import add_misc_map, add_timestamps


def add_account_facet(graph: Graph, trace: Trace):
    account_facet = KB[f"AccountFacet-{uuid4()}"]
    graph.add((account_facet, RDF.type, UCO_OBSERVABLE.AccountFacet))

    # accessedOn (date) - The date and time of the last usage of the account.
    aon = trace.account.accessed_on
    if aon:
        graph.add((account_facet, UCO_OBSERVABLE.accessedTime, Literal(aon)))

    # active (boolean) - Can the user account be used or is the account disabled or locked.
    active = trace.account.active
    if active:
        graph.add((account_facet, UCO_OBSERVABLE.isActive, Literal(aon)))

    # createdOn (date) - The date and time of account creation.
    con = trace.account.created_on
    if con:
        graph.add((account_facet, UCO_OBSERVABLE.createdTime, Literal(con)))

    # expiresOn (date) - The date and time of expiration of the account.
    eon = trace.account.expires_on
    if eon:
        graph.add((account_facet, UCO_OBSERVABLE.expirationTime, Literal(eon)))

    # modifiedOn (date) - The date and time of the last modification of the account.
    mon = trace.account.modified_on
    if mon:
        graph.add((account_facet, UCO_OBSERVABLE.modifiedTime, Literal(mon)))

    # name (string) - The account login name or another identifier that describes the account e.g. email address.
    an = trace.account.name
    if an:
        graph.add((account_facet, UCO_OBSERVABLE.accountIdentifier, Literal(an)))

    # owner (string) - The owner of this account.
    ao = trace.account.owner
    if ao:
        graph.add((account_facet, UCO_OBSERVABLE.owner, Literal(ao)))

    return account_facet


def add_account_authentication_facet(graph: Graph, trace: Trace):
    auth_facet = KB[f"AccountAuthenticationFacet-{uuid4()}"]
    graph.add((auth_facet, RDF.type, UCO_OBSERVABLE.AccountAuthenticationFacet))

    # password (string) - The stored password, might be encrypted.
    pw = trace.account.password
    if pw:
        graph.add(auth_facet, UCO_OBSERVABLE.password, Literal(pw))

    # passwordType (string) - The type of password, for instance plain-text or encrypted.
    pwt = trace.account.password_type
    if pwt:
        graph.add(auth_facet, UCO_OBSERVABLE.passwordType, Literal(pwt))

    return auth_facet


def add_application(graph: Graph, trace: Trace):
    application = KB[f"Application-{uuid4()}"]
    graph.add((application, RDF.type, UCO_OBSERVABLE.Application))

    app_name = trace.account.application or ""
    graph.add((application, UCO_CORE.name, app_name))

    return application


def add_application_account_facet(graph: Graph, trace: Trace):
    application_account_facet = KB[f"ApplicationAccountFacet"]

    graph.add(
        (application_account_facet, RDF.type, UCO_OBSERVABLE.ApplicationAccountFacet)
    )

    # application (string) - The application using the account.
    application = add_application(graph, trace)
    graph.add((application_account_facet, UCO_OBSERVABLE.application, application))

    return application_account_facet


def add_account(graph: Graph, trace: Trace):
    """A user account."""

    account = KB[f"Account-{uuid4()}"]
    account_facet = add_account_facet(graph, trace)
    application_account_facet = add_application_account_facet(graph, trace)
    auth_facet = add_account_authentication_facet(graph, trace)

    graph.add((account, RDF.type, UCO_OBSERVABLE.Account))
    graph.add((account, UCO_CORE.hasFacet, account_facet))
    graph.add((account, UCO_CORE.hasFacet, application_account_facet))
    graph.add((account, UCO_CORE.hasFacet, auth_facet))

    # description (string) - A description.
    desc = trace.account.description
    if desc:
        graph.add((account, UCO_CORE.description, Literal(desc)))

    # misc (map:string) - Additional information about the account.
    add_misc_map(graph, account_facet, trace.account.misc)

    # timestamps (map:date) - Additional timestamps found for account e.g. timestamps.firstUsedOn.
    add_timestamps(graph, account_facet, trace.account.timestamps)

    return account


# TODO:
# type (string) - The type of account, for instance OS, website, email.


# def add_accountArchive(graph: Graph, trace: Trace):
#     """A list of accounts."""

#     account_archive = KB[f"AccountArchive-{uuid4()}"]

#     graph.add((account_archive, RDF.type, ...?))

#     add_misc_map(graph, account_archive, trace.account_archive.misc)
#     # misc (map:string) - Additional information about the account archive.
#     pass
