import uuid
from dataclasses import dataclass

import injector

from projects.application.repositories.projects_repository import ProjectsRepository
from projects.domain.entities import Project


@dataclass(frozen=True)
class CreateProjectInputDto:
    name: str


class CreateProject:
    def __init__(self, projects_repo: ProjectsRepository):
        self._project_repo = projects_repo

    def execute(self, input_dto: CreateProjectInputDto):
        self._project_repo.save(Project(
            id=uuid.uuid4(),
            name=input_dto.name,
            tasks=[]
        ))
