from injector import Injector

from projects import Projects
from projects_infra import ProjectsInfra


def assemble() -> Injector:
    return Injector(
        [
            Projects(),
            ProjectsInfra()
        ],
        auto_bind=False,
    )
