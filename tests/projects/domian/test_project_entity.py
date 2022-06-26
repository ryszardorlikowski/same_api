import uuid

import pytest

from projects.domain import events
from projects.domain.entities import Project, Task, PROJECT_TASKS_LIMIT, ProjectExceededLimit, NotUniqueTaskTitle, \
    CannotFinishProjectWithUncompletedTasks
from tests.projects.factories import ProjectFactory, TaskFactory
from tests.random_refs import random_suffix


def test_cannot_add_new_task_when_number_of_tasks_has_exceeded_the_limit():
    project: Project = ProjectFactory()
    for _ in range(PROJECT_TASKS_LIMIT):
        task_name = f"Task {random_suffix()}"
        project.add_task(name=task_name)

    with pytest.raises(ProjectExceededLimit):
        task_name = f"Task {random_suffix()}"
        project.add_task(name=task_name)


def test_cannot_add_task_with_not_unique_title():
    project: Project = ProjectFactory()
    task_name = "Task name"
    project.add_task(name=task_name)
    with pytest.raises(NotUniqueTaskTitle):
        project.add_task(name=task_name)


def test_task_is_removed_from_project():
    project: Project = ProjectFactory()
    task: Task = TaskFactory()
    project.tasks.append(task)
    project.remove_task(task.id)
    assert project.number_of_tasks == 0


def test_can_done_project_when_all_tasks_have_been_completed():
    project: Project = ProjectFactory()
    task_1: Task = TaskFactory(id=uuid.uuid4())
    task_2: Task = TaskFactory(id=uuid.uuid4())

    project.tasks.append(task_1)
    project.tasks.append(task_2)

    project.complete_task(task_1.id)
    project.complete_task(task_2.id)

    project.finish()

    assert project.is_done


def test_cannot_done_project_when_all_tasks_have_not_been_completed():
    project: Project = ProjectFactory()
    task: Task = TaskFactory(id=uuid.uuid4())

    project.tasks.append(task)

    with pytest.raises(CannotFinishProjectWithUncompletedTasks):
        project.finish()


def test_record_event_when_project_is_created():
    project: Project = ProjectFactory()

    assert events.ProjectCreated(project_id=project.id) == project.domain_events[0]
