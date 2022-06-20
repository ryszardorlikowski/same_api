import abc

from projects.domain.entities import Project
from projects.domain.value_objects import ProjectId


class ProjectDoesNotExist(Exception):
    """"""


class ProjectsRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, project: ProjectId) -> Project:
        pass

    @abc.abstractmethod
    def save(self, project: Project) -> None:
        pass

    @abc.abstractmethod
    def delete(self, project_id: ProjectId) -> None:
        pass

    @abc.abstractmethod
    def list(self):
        pass
