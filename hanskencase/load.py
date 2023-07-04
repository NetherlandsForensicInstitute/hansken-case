from rdflib import Graph

from hanskencase._email import get_email_message
from hanskencase._file import get_file, is_directory
from .namespaces import HANSKEN, RDF, UCO_CORE, UCO_OBSERVABLE

image_query_facet = """"
SELECT DISTINCT ?facet
WHERE {
    ?img uco_core:hasFacet ?facet.
    ?facet a uco_observable:ImageFacet .
}"""


def get_id(subj):
    return str(subj).split("-", 1)[1]


def traces_from_jsonld(filename="export.jsonld"):
    graph = Graph().parse(filename, format="json-ld")
    return traces_from_graph(graph)


def image_facet_from_graph(graph: Graph, image_facet_subj):
    return {}


def image_from_graph(graph: Graph, image_subj):
    image_id = get_id(image_subj)
    image_facet_data = image_facet_from_graph(
        graph, graph.value(image_subj, UCO_CORE.hasFacet)
    )
    name = str(graph.value(image_subj, UCO_CORE.name))
    description = str(graph.value(image_subj, UCO_CORE.description))
    created_by = str(graph.value(image_subj, UCO_CORE.createdBy))
    created_date = str(graph.value(image_subj, UCO_CORE.createdTime))

    return dict(
        image_id=image_id,
        name=name,
        description=description,
        createdBy=created_by,
        createdDate=created_date,
        **image_facet_data,
    )


def trace_from_graph(graph: Graph, trace_subj):
    trace = {}
    trace["uid"] = get_id(trace_subj)

    description = graph.value(trace_subj, UCO_CORE.description, default=False)
    if description:
        trace["description"] = str(description)

    model_version = graph.value(trace_subj, HANSKEN.modelVersion, default=False)
    if model_version:
        trace["model_version"] = model_version
    name = graph.value(trace_subj, UCO_CORE.name, default=False)
    if name:
        trace["name"] = str(name)
    image_subject = graph.value(trace_subj, UCO_OBSERVABLE.image, default=False)
    if image_subject:
        trace["image"] = image_from_graph(graph, image_subject)

    # image = add_image(graph, trace)
    # graph.add((trace_kb, HANSKEN.image, image))

    # parent -- maybe use with UCO_OBSERVABLE.ObservableRelationship
    # or maybe with the observable:PathRelationFacet
    return trace


def get_value(graph, subject, predicate, default=""):
    value = default
    objects = graph.objects(subject, predicate)
    for object in objects:
        value = str(object)
        break  # Only first object

    return value


def email_from_graph(graph: Graph, email_subject):
    email = get_email_message(graph, email_subject)
    return email


def file_from_graph(graph: Graph, file_subject):
    file = get_file(graph, file_subject)
    return file


def folder_from_graph(graph: Graph, folder_subject):
    raise NotImplementedError("Folder import not yet implemented")


def traces_from_graph(graph: Graph):
    traces = []
    for trace_subject in graph.subjects(RDF.type, HANSKEN.Trace):
        trace = trace_from_graph(graph, trace_subject)
        traces.append(trace)

        for data_facet in graph.objects(trace_subject, HANSKEN.hasData):
            types = graph.objects(data_facet, RDF.type)
            for t in types:
                if t == UCO_OBSERVABLE.EmailMessage:
                    trace["email"] = email_from_graph(graph, data_facet)
                if t == UCO_OBSERVABLE.File:  # and folder(?)
                    if is_directory(graph, data_facet):
                        trace["folder"] = file_from_graph(graph, data_facet)
                    else:
                        trace["file"] = file_from_graph(graph, data_facet)

    return traces
