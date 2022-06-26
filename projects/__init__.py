import injector

from projects.application.repositories.projects_repository import ProjectsRepository
from projects.application.use_cases.add_task_to_project import AddTaskToProject, AddTaskToProjectInputDto
from projects.application.use_cases.create_project import CreateProject, CreateProjectInputDto

from projects.domain.exceptions import ProjectExceededLimit, NotUniqueTaskTitle, TaskIsAlreadyDone, \
    CannotRemoveTaskFromDoneProject, NotFoundTaskInProject, CannotFinishProjectWithUncompletedTasks

__all__ = [
    # module
    'Projects',

    # use cases
    'CreateProject',
    'AddTaskToProject',

    # input dto
    'CreateProjectInputDto',
    'AddTaskToProjectInputDto',

    # exceptions
    'ProjectExceededLimit',
    'NotUniqueTaskTitle',
    'TaskIsAlreadyDone',
    'CannotRemoveTaskFromDoneProject',
    'NotFoundTaskInProject',
    'CannotFinishProjectWithUncompletedTasks',
]


class Projects(injector.Module):
    @injector.provider
    def create_project_us(self, repo: ProjectsRepository) -> CreateProject:
        return CreateProject(projects_repo=repo)

    @injector.provider
    def add_task_to_project_us(self, repo: ProjectsRepository) -> AddTaskToProject:
        return AddTaskToProject(projects_repo=repo)
