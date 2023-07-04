from uuid import uuid4

from rdflib import Graph
from hansken.util import parse_datetime

from .namespaces import UCO_OBSERVABLE, RDF, KB, Literal, HANSKEN, KB, UCO_CORE
from .utils import add_misc_map, get_misc_map

# TODO: Add file export


def add_file_facet(graph, trace, isFolder=False):
    """
    File

    A file is a block of arbitrary information, or resource for storing information.
    """

    file_facet = KB[f"FileFacet-{uuid4()}"]
    # graph.add((file_facet, UCO_OBSERVABLE.HasFacet, UCO_OBSERVABLE.FileTrace))
    graph.add((file_facet, RDF.type, UCO_OBSERVABLE.FileFacet))

    # accessedOn (date) - The last time at which the file was accessed. -
    aon = trace.file.accessed_on
    if aon:
        graph.add((file_facet, UCO_OBSERVABLE.accessedTime, Literal(aon)))
    # changedOn (date) - The time at which the metadata of the file was last changed.
    chon = trace.file.changed_on
    if chon:
        graph.add((file_facet, UCO_OBSERVABLE.changedTime, Literal(chon)))
    # createdOn (date) - The date and time at which the file was created.
    cron = trace.file.created_on
    if cron:
        graph.add((file_facet, UCO_OBSERVABLE.createdTime, Literal(cron)))
    # entryId (integer) - A unique identifier for the file within the filesystem. Currently, used for NTFS MFT entry id.
    # TODO: add entry ID?

    # extension (string) - The file name extension: everything after the last dot. Not present if the file has no dot in its name.",
    ext = trace.file.extension
    if ext:
        graph.add((file_facet, UCO_OBSERVABLE.extension, Literal(ext)))

    # modifiedOn (date) - The time at which the content of the file was last modified.
    mon = trace.file.modified_on
    if mon:
        graph.add((file_facet, UCO_OBSERVABLE.modifiedTime, Literal(mon)))

    # name (string) - The name of the file.
    filename = trace.file.name
    if filename:
        graph.add((file_facet, UCO_OBSERVABLE.fileName, Literal(filename)))

    # owner (string) - The owner of the file.
    owner = trace.file.owner
    if owner:
        graph.add((file_facet, UCO_OBSERVABLE.owner, Literal(owner)))

    # path (string) - The path of the file in the filesystem, including filename.",
    path = trace.file.path
    if path:
        graph.add((file_facet, UCO_OBSERVABLE.filePath, Literal(path)))
    # timestamps (map:date) - Additional timestamps found for files.
    timestamps = trace.file.timestamps or {}
    for _, timestamp in timestamps.items():
        graph.add((file_facet, HANSKEN.hasTimeStamp, Literal(timestamp)))

    graph.add((file_facet, UCO_OBSERVABLE.isDirectory, Literal(isFolder)))

    # accessedOn (date) - The last time at which the file was accessed.
    # changedOn (date) - The time at which the metadata of the file was last changed.
    # createdOn (date) - The date and time at which the file was created.
    # entryId (integer) - A unique identifier for the file within the filesystem. Currently, used for NTFS MFT entry id.
    # extension (string) - The file name extension: everything after the last dot. Not present if the file has no dot in its name.
    # misc (map:string) - Additional information.
    # modifiedOn (date) - The time at which the content of the file was last modified.
    # name (string) - The name of the file.
    # owner (string) - The owner of the file.
    # path (string) - The path of the file in the filesystem, including filename.
    # timestamps (map:date) - Additional timestamps found for files.

    return file_facet


def add_file(graph, trace):
    """A file is a block of arbitrary information, or resource for storing information."""
    the_file = KB[f"File-{uuid4()}"]
    file_facet = add_file_facet(graph, trace, isFolder=False)

    graph.add((the_file, RDF.type, UCO_OBSERVABLE.File))
    graph.add((the_file, UCO_CORE.hasFacet, file_facet))

    misc = trace.file.misc
    if misc:
        add_misc_map(graph, the_file, misc)

    return the_file


def add_file_archive_facet(graph, trace):
    archive_file_facet = KB[f"ArchiveFileFacet-{uuid4()}"]

    # misc (map:string) - Additional information about the file archive.
    add_misc_map(graph, archive_file_facet, trace.file_archive.misc)

    # type (string) - The type of a file archive, e.g. ZIP, GZIP or RAR.
    graph.add((archive_file_facet, UCO_OBSERVABLE.archiveType, trace.file_archive.type))

    return archive_file_facet


def add_file_archive(graph, trace):
    """A collection of folders and files packed into one file."""

    archive_file = KB[f"ArchiveFile-{uuid4()}"]
    archive_file_facet = add_file_archive_facet(graph, trace)

    graph.add((archive_file, RDF.type, UCO_OBSERVABLE.ArchiveFile))
    graph.add((archive_file, UCO_CORE.hasFacet, archive_file_facet))

    return archive_file


def add_filesystem_facet(graph, trace):
    filesystem_facet = KB[f"FilesystemFacet-{uuid4()}"]

    graph.add((filesystem_facet, RDF.type, UCO_OBSERVABLE.FileSystemFacet))

    # misc (map:string) - Additional information on the filesystem, for example the version number.",
    add_misc_map(graph, filesystem_facet, trace.filesystem.misc)

    # type (string) - The type of a filesystem, for example NTFS or FAT32.",
    fstype = trace.filesystem.type
    if fstype:
        graph.add((filesystem_facet, UCO_OBSERVABLE.filesystemType), Literal(fstype))

    return filesystem_facet


def add_filesystem(graph, trace):
    """A filesystem is a special-purpose database for the storage, organization, manipulation, and retrieval of data."""
    filesystem = KB[f"Filesystem-{uuid4()}"]
    filesystem_facet = add_filesystem_facet(graph, trace)

    graph.add((filesystem, RDF.type, UCO_OBSERVABLE.FileSystem))
    graph.add((filesystem, UCO_CORE.hasFacet, filesystem_facet))


def add_folder(graph, trace):
    folder = KB[f"Folder-{uuid4()}"]
    file_facet = add_file_facet(graph, trace, isFolder=True)

    graph.add((folder, RDF.type, UCO_OBSERVABLE.File))
    graph.add((folder, UCO_CORE.hasFacet, file_facet))

    return folder


def get_file_facet(graph, file_facet):
    file_facet_data = {}

    # accessedOn (date) - The last time at which the file was accessed. -
    aon = graph.value(file_facet, UCO_OBSERVABLE.accessedTime)
    if aon is not None:
        file_facet_data["accessed_on"] = parse_datetime(aon)

    # changedOn (date) - The time at which the metadata of the file was last changed.
    chon = graph.value(file_facet, UCO_OBSERVABLE.changedTime)
    if chon is not None:
        file_facet_data["changed_on"] = parse_datetime(chon)

    # createdOn (date) - The date and time at which the file was created.
    cron = graph.value(file_facet, UCO_OBSERVABLE.createdTime)
    if cron is not None:
        file_facet_data["created_on"] = parse_datetime(cron)

    # extension (string) - The file name extension: everything after the last dot. Not present if the file has no dot in its name.",
    ext = graph.value(file_facet, UCO_OBSERVABLE.extension)
    if ext is not None:
        file_facet_data["extension"] = ext

    # modifiedOn (date) - The time at which the content of the file was last modified.
    mon = graph.value(file_facet, UCO_OBSERVABLE.modifiedTime)
    if mon is not None:
        file_facet_data["modified_on"] = parse_datetime(mon)

    # name (string) - The name of the file.
    filename = graph.value(file_facet, UCO_OBSERVABLE.fileName)
    if filename:
        file_facet_data["name"] = filename

    # owner (string) - The owner of the file.
    owner = graph.value(file_facet, UCO_OBSERVABLE.owner)
    if owner:
        file_facet_data["owner"] = owner

    # path (string) - The path of the file in the filesystem, including filename.",
    path = graph.value(file_facet, UCO_OBSERVABLE.filePath)
    if path:
        file_facet_data["path"] = path

    return file_facet_data


def is_directory(graph: Graph, file_subject):
    facets = graph.objects(file_subject, UCO_CORE.hasFacet)

    file_facet = None
    for facet in facets:
        facet_type = graph.value(facet, RDF.type)
        if facet_type == UCO_OBSERVABLE.FileFacet:
            file_facet = facet
            break

    return graph.value(file_facet, UCO_OBSERVABLE.isDirectory)


def get_file(graph: Graph, file_subject):
    facets = graph.objects(file_subject, UCO_CORE.hasFacet)

    file_facet = None
    for facet in facets:
        facet_type = graph.value(facet, RDF.type)
        if facet_type == UCO_OBSERVABLE.FileFacet:
            file_facet = facet
            break

    file_facet_data = get_file_facet(graph, file_facet) if file_facet else {}

    # graph.add((file_facet, UCO_OBSERVABLE.isDirectory, Literal(isFolder)))

    misc_data = get_misc_map(graph, file_subject)
    # timestamps (map:date) - Additional timestamps found for files.
    # timestamps = trace.file.timestamps or {}
    # for _, timestamp in timestamps.items():
    # graph.add((file_facet, HANSKEN.hasTimeStamp, Literal(timestamp)))

    return {"misc": misc_data, **file_facet_data}
