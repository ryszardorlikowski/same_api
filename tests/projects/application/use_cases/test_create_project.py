import pytest

from projects.application.repositories.projects_repository import ProjectsRepository
from projects.application.use_cases.create_project import CreateProjectInputDto, CreateProject
from projects_infra.repositories.in_memory_projects_repository import InMemoryProjectsRepository


@pytest.fixture
def projects_repo() -> ProjectsRepository:
    return InMemoryProjectsRepository()


def test_new_project_is_created(projects_repo):
    input_dto = CreateProjectInputDto(
        name="New board"
    )
    use_case = CreateProject(projects_repo=projects_repo)

    use_case.execute(input_dto)

    tasks_lists = projects_repo.list()

    assert len(tasks_lists) == 1
    assert tasks_lists[0].name == input_dto.name
