import json

with open("trace-model-output.json") as fh:
    model = json.load(fh)


props = model["origins"]["categories"]["extracted"]["types"]

props["file"]

f = props["file"]

f["description"]
f


def get_propstring(key, value):
    map = "map:" if value.get("isMap") else ""
    lst = "list:" if value.get("isList") else ""
    mol = map or lst
    _type = value["type"]
    desc = value["description"]

    return f"\t# {key} ({mol}{_type}) - {desc}"


def get_typestring(key, value):
    description_txt = f'"""{value["description"]}"""'
    properties_txt = "\n".join(
        get_propstring(k, v) for k, v in value["properties"].items()
    )

    return f"""def add_{key}(graph, trace):
    {description_txt}
{properties_txt}
    
    
    """


txt = "\n\n".join(get_typestring(k, v) for k, v in props.items())

with open("datamodel_functions.py", "w") as fh:
    fh.write(txt)
