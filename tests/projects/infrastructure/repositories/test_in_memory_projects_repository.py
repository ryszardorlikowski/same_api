import uuid

import pytest

from projects.infrastructure.repositories.in_memory_projects_repository import InMemoryProjectsRepository
from projects.application.repositories.projects_repository import ProjectDoesNotExist
from tests.projects.factories import ProjectFactory


@pytest.fixture
def repo() -> InMemoryProjectsRepository:
    return InMemoryProjectsRepository()


def test_repo_save_project(repo):
    project_1 = ProjectFactory(id=uuid.uuid4())
    project_2 = ProjectFactory(id=uuid.uuid4())

    repo.save(project_1)
    repo.save(project_2)

    assert len(repo._storage) == 2
    assert repo._storage[project_1.id].id == project_1.id


def test_get_project_from_repo(repo):
    project = ProjectFactory(id=uuid.uuid4())
    repo.save(project)

    assert repo.get(project.id) == project


def test_rasie_exception_when_project_does_not_exist(repo):
    with pytest.raises(ProjectDoesNotExist):
        repo.get(uuid.uuid4())


def test_get_projects_list(repo):
    projects_list = []
    for _ in range(3):
        project = ProjectFactory(id=uuid.uuid4())
        projects_list.append(project)
        repo.save(project)

    assert repo.list() == projects_list
