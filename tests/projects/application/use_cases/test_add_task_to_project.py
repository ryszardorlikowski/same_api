import pytest

from projects.infrastructure.repositories.in_memory_projects_repository import InMemoryProjectsRepository
from projects.application.repositories.projects_repository import ProjectsRepository
from projects.application.use_cases.add_task_to_project import AddTaskToProject, AddTaskToProjectInputDto
from tests.projects.factories import ProjectFactory


@pytest.fixture
def repo() -> ProjectsRepository:
    return InMemoryProjectsRepository()


def test_new_task_is_added_to_project(repo: ProjectsRepository) -> None:
    project = ProjectFactory()
    repo.save(project)

    use_case = AddTaskToProject(projects_repo=repo)

    input_dto = AddTaskToProjectInputDto(
        project_id=project.id,
        name="Task"
    )

    use_case.execute(input_dto)

    refreshed_project = repo.get(project.id)

    assert refreshed_project.number_of_tasks == 1
