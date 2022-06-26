import injector as injector

from projects.application.repositories.projects_repository import ProjectsRepository
from projects_infra.repositories.in_memory_projects_repository import InMemoryProjectsRepository


class ProjectsInfra(injector.Module):

    @injector.provider
    def projects_repo(self) -> ProjectsRepository:
        return InMemoryProjectsRepository()
