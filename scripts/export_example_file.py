"""
Export example using the hanskencase wrapper around the Hansken Python API

"""

from hanskencase.project import get_project
from hanskencase.export import to_zip, to_folder

ctx = get_project()
results = ctx.search("type:file")
traces = results.take(5)

to_folder(traces)
# to_zip(traces)
