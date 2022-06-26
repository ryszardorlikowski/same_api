import copy

from projects.application.repositories.projects_repository import ProjectsRepository, ProjectDoesNotExist
from projects.domain.entities import Project
from projects.domain.value_objects import ProjectId


class InMemoryProjectsRepository(ProjectsRepository):

    def __init__(self):
        self._storage: dict[ProjectId, Project] = {}

    def get(self, project_id: ProjectId) -> Project:
        try:
            return copy.deepcopy(self._storage[project_id])
        except KeyError:
            raise ProjectDoesNotExist

    def save(self, tasks_list: Project) -> None:
        self._storage[tasks_list.id] = copy.deepcopy(tasks_list)

    def list(self):
        return [project for project in self._storage.values()]

    def delete(self, project_id: ProjectId) -> None:
        raise NotImplementedError
