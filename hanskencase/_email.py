from uuid import uuid4

from rdflib import Graph
from hansken.recipes.export import data_stream
from hansken.util import parse_datetime


from .email_address import add_email_address, get_email_address
from .namespaces import UCO_OBSERVABLE, Literal, KB, RDF, UCO_CORE
from .utils import add_misc_map, get_misc_map


def create_raw_headers(headers: dict):
    return (f"{k}: {v}" for k, v in headers.items())


def create_address_string(address_data: dict):
    dn = address_data.get("displayName", "")
    av = address_data.get("addressValue", "")

    if dn:
        address_string = f'"{dn}" <{av}>'
    else:
        address_string = av

    return address_string


def add_email_account_facet(graph: Graph, address):
    email_account_facet = KB[f"EmailAccountFacet-{uuid4()}"]
    email_address = add_email_address(graph, address)

    graph.add((email_account_facet, RDF.type, UCO_OBSERVABLE.EmailAccountFacet))
    graph.add((email_account_facet, UCO_OBSERVABLE.emailAddress, email_address))

    return email_account_facet


def add_email_account(graph: Graph, address):
    email_account = KB[f"EmailAccount-{uuid4()}"]
    email_account_facet = add_email_account_facet(graph, address)

    graph.add((email_account, RDF.type, UCO_OBSERVABLE.EmailAccount))
    graph.add((email_account, UCO_CORE.hasFacet, email_account_facet))

    return email_account


def add_email_facet(graph, trace):
    email_facet = KB[f"EmailMessageFacet-{uuid4()}"]
    graph.add((email_facet, RDF.type, UCO_OBSERVABLE.EmailMessageFacet))

    app = trace.email.application
    if app:
        graph.add((email_facet, UCO_OBSERVABLE.application, Literal(app)))

    bcc = trace.email.bcc or []
    for string in bcc:
        graph.add((email_facet, UCO_OBSERVABLE.bcc, Literal(string)))

    cc = trace.email.cc or []
    for string in cc:
        graph.add((email_facet, UCO_OBSERVABLE.cc, Literal(string)))

    categories = trace.email.categories or []
    for category in categories:
        graph.add((email_facet, UCO_OBSERVABLE.categories, Literal(category)))

    con = trace.email.created_on  # trace.email.createdOn
    if con:
        graph.add((email_facet, UCO_OBSERVABLE.creationTime, Literal(con)))

    if trace.email.__contains__("from"):
        from_ = trace.email["from"]
        from_account = add_email_address(graph, from_)  # TODO: type EmailAddress
        graph.add((email_facet, UCO_OBSERVABLE["from"], from_account))
        graph.add((email_facet, UCO_OBSERVABLE.sender, from_account))

    # trace.email.hasAttachment

    headers = trace.email.headers or {}
    raw_headers = create_raw_headers(headers)
    for rh in raw_headers:
        graph.add((email_facet, UCO_OBSERVABLE.headerRaw, Literal(rh)))

    irt = trace.email.in_reply_to
    if irt:
        # irt_account = KB[f"EmailAccount-{irt}"]
        # irt_account = KB[f"EmailAccount-{uuid4()}"]
        graph.add((email_facet, UCO_OBSERVABLE.inReplyTo, Literal(irt)))

    labels = trace.email.labels or {}  # labels, map:string
    for label in labels.values():
        graph.add((email_facet, UCO_OBSERVABLE.labels, Literal(label)))

    mid = trace.email.message_id  # messageId, string
    if mid:
        graph.add((email_facet, UCO_OBSERVABLE.messageID, Literal(mid)))

    mod = trace.email.modified_on  # modifiedOn, date
    if mod:
        graph.add((email_facet, UCO_OBSERVABLE.modifiedTime, mod))

    prio = trace.email.priority  # priority, string
    if prio:
        graph.add((email_facet, UCO_OBSERVABLE.priority, prio))

    read = trace.email.read  # read, boolean
    if read is not None:
        graph.add((email_facet, UCO_OBSERVABLE.isRead, Literal(read)))

    ron = trace.email.received_on  # receivedOn, date
    if ron:
        graph.add((email_facet, UCO_OBSERVABLE.receivedTime, Literal(ron)))

    # references, list:string, A list of email message identifiers this email relates to.",

    son = trace.email.sent_on
    if son:
        graph.add((email_facet, UCO_OBSERVABLE.sentTime, Literal(son)))

    graph.add((email_facet, UCO_OBSERVABLE.subject, Literal(trace.email.subject)))

    tos = trace.email.to or []
    for to in tos:
        to_account = add_email_account(graph, to)
        graph.add((email_facet, UCO_OBSERVABLE.to, to_account))

    graph.add(
        (
            email_facet,
            UCO_OBSERVABLE.bodyRaw,
            Literal(data_stream("html").to_text(trace)),
        )
    )

    # TODO: link email addresses etc
    # (address_facet, RDF.type, UCO_OBSERVABLE.EmailAddressFacet),
    # (digital_account_facet, RDF.type, UCO_OBSERVABLE.DigitalAccountFacet),
    # (email_account_facet, RDF.type, UCO_OBSERVABLE.EmailAccountFacet),
    return email_facet


def parse_raw_header(raw_header):
    raw_header = str(raw_header)

    key, value = [str(s).strip() for s in raw_header.split(":", 1)]

    return [(key, value)]


def get_email_facet(graph, email_facet) -> dict:
    email_facet_data = {}

    app = graph.value(email_facet, UCO_OBSERVABLE.application)
    if app is not None:
        email_facet_data["application"] = app

    bcc = graph.objects(email_facet, UCO_OBSERVABLE.bcc)
    bcclist = [str(b) for b in bcc]
    if bcclist:
        email_facet_data["bcc"] = bcclist

    cc = graph.objects(email_facet, UCO_OBSERVABLE.cc)
    cclist = [str(c) for c in cc]
    if cclist:
        email_facet_data["cc"] = cclist

    cats = graph.objects(email_facet, UCO_OBSERVABLE.categories)
    catlist = [str(c) for c in cats]
    if catlist:
        email_facet_data["categories"] = catlist

    con = graph.value(email_facet, UCO_OBSERVABLE.createdTime)
    if con:
        email_facet_data["created_on"] = parse_datetime(con)

    from_ = graph.value(email_facet, UCO_OBSERVABLE["from"])
    if from_:
        from_data = get_email_address(graph, from_)
        email_facet_data["from"] = create_address_string(from_data)

    # trace.email.hasAttachment

    headers = {
        key: value
        for header in graph.objects(email_facet, UCO_OBSERVABLE.headerRaw)
        for key, value in parse_raw_header(header)
    }
    if headers:
        email_facet_data["headers"] = headers

    irt = graph.value(email_facet, UCO_OBSERVABLE.inReplyTo)
    if irt is not None:
        email_facet_data["in_reply_to"] = str(irt)

    # labels = trace.email.labels or {}  # labels, map:string
    # for label in labels.values():
    #     graph.add((email_facet, UCO_OBSERVABLE.labels, Literal(label)))

    mid = graph.value(email_facet, UCO_OBSERVABLE.messageID)
    if mid is not None:
        email_facet_data["message_id"] = str(mid)

    # mod = trace.email.modified_on  # modifiedOn, date
    mod = graph.value(email_facet, UCO_OBSERVABLE.modifiedTime)
    if mod is not None:
        email_facet_data["modified_on"] = parse_datetime(mod)

    # read = trace.email.read  # read, boolean
    read = graph.value(email_facet, UCO_OBSERVABLE.isRead)
    if read is not None:
        read = True if str(read) == "true" else False
        email_facet_data["read"] = read

    ron = graph.value(email_facet, UCO_OBSERVABLE.receivedTime)
    if ron is not None:
        email_facet_data["received_on"] = parse_datetime(ron)

    # references, list:string, A list of email message identifiers this email relates to.",
    # son = trace.email.sent_on
    # if son:
    #     graph.add((email_facet, UCO_OBSERVABLE.sentTime, Literal(son)))

    sbj = graph.value(email_facet, UCO_OBSERVABLE.subject)
    if sbj is not None:
        email_facet_data["subject"] = str(sbj)

    to = graph.value(email_facet, UCO_OBSERVABLE.to)
    if to is not None:
        to_data = get_email_address(graph, to)
        email_facet_data["to"] = create_address_string(to_data)

    prio = graph.value(email_facet, UCO_OBSERVABLE.priority)
    if prio is not None:
        email_facet_data = str(prio)

    return email_facet_data


def add_email_message(graph, trace):
    email_message = KB[f"EmailMessage-{uuid4()}"]
    email_facet = add_email_facet(graph, trace)

    graph.add((email_message, RDF.type, UCO_OBSERVABLE.EmailMessage))
    graph.add((email_message, UCO_CORE.hasFacet, email_facet))

    # trace.email.misc, map:string
    misc = trace.email.misc
    if misc:
        add_misc_map(graph, email_message, misc)

    return email_message


def get_email_message(graph, email_subject):
    facets = graph.objects(email_subject, UCO_CORE.hasFacet)

    email_facet = None
    for facet in facets:
        facet_type = graph.value(facet, RDF.type)
        if facet_type == UCO_OBSERVABLE.EmailMessageFacet:
            email_facet = facet
            break

    email_facet_data = get_email_facet(graph, email_facet) if email_facet else {}

    misc_data = get_misc_map(graph, email_subject)
    return {"misc": misc_data, **email_facet_data}
