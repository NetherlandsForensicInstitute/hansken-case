import json

from hanskencase.load import traces_from_jsonld


traces = traces_from_jsonld("./export/export.jsonld")


with open("imported_traces.json", "w") as fh:
    json.dump(traces, fh)
