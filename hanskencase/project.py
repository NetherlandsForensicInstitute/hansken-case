import os

from hansken.connect import connect_project

def get_project():
    """Conveniently get project context from environment variables"""
    url = os.getenv("HANSKEN_URL", "https://demo.hansken.org/gatekeeper/")
    keystore = os.getenv("HANSKEN_KS", "https://demo.hansken.org/keystore/")
    # default project: Hansken Demo project
    project = os.getenv("HANSKEN_PROJECT", "779d0a92-83f5-46a2-b68c-a4e810e1c5b5")

    username = os.getenv("HANSKEN_USER")
    password = os.getenv("HANSKEN_PASS")

    context = connect_project(
        url,
        project,
        keystore=keystore,
        username=username,
        password=password,
    )

    return context
