from uuid import uuid4
from rdflib.namespace import Namespace, XSD, RDF, RDFS

from rdflib import Literal, Graph

# import rdflib

UCO_ACTION = Namespace("https://ontology.unifiedcyberontology.org/uco/action/")
UCO_CORE = Namespace("https://ontology.unifiedcyberontology.org/uco/core/")
UCO_IDENTITY = Namespace("https://ontology.unifiedcyberontology.org/uco/identity/")
UCO_LOCATION = Namespace("https://ontology.unifiedcyberontology.org/uco/location/")
UCO_OBSERVABLE = Namespace("https://ontology.unifiedcyberontology.org/uco/observable/")
UCO_ROLE = Namespace("https://ontology.unifiedcyberontology.org/uco/role/")
UCO_TOOL = Namespace("https://ontology.unifiedcyberontology.org/uco/tool/")
UCO_TYPES = Namespace("https://ontology.unifiedcyberontology.org/uco/types/")
UCO_VOCABULARY = Namespace("https://ontology.unifiedcyberontology.org/uco/vocabulary/")

CASE_INVESTIGATION = Namespace("https://ontology.caseontology.org/case/investigation/")


VOCAB = Namespace("http://example.org/ontology/local#")
DRAFTING = Namespace("http://example.org/ontology/drafting#")
KB = Namespace("http://example.org/kb/")

HANSKEN = Namespace("http://example.org/hansken/")


context = {
    "@vocab": str(VOCAB),
    "drafting": str(DRAFTING),
    "kb": str(KB),
    "rdf": str(RDF),
    "rdfs": str(RDFS),
    "xsd": str(XSD),
    "case-investigation": str(CASE_INVESTIGATION),
    "uco-action": str(UCO_ACTION),
    "uco-core": str(UCO_CORE),
    "uco-identity": str(UCO_IDENTITY),
    "uco-location": str(UCO_LOCATION),
    "uco-observable": str(UCO_OBSERVABLE),
    "uco-role": str(UCO_ROLE),
    "uco-tool": str(UCO_TOOL),
    "uco-types": str(UCO_TYPES),
    "uco-vocabulary": str(UCO_VOCABULARY),
    "hansken": str(HANSKEN),
}
