from dataclasses import dataclass

from projects.application.repositories.projects_repository import ProjectsRepository
from projects.domain.entities import Project
from projects.domain.value_objects import ProjectId


@dataclass(frozen=True)
class AddTaskToProjectInputDto:
    project_id: ProjectId
    name: str


class AddTaskToProject:

    def __init__(self, projects_repo: ProjectsRepository) -> None:
        self._projects_repo = projects_repo

    def execute(self, input_dto: AddTaskToProjectInputDto) -> None:
        project: Project = self._projects_repo.get(input_dto.project_id)
        project.add_task(name=input_dto.name)
        self._projects_repo.save(project)
