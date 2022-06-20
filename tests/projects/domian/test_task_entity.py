import pytest

from projects.domain.entities import Task, TaskIsAlreadyDone
from tests.projects.factories import TaskFactory


def test_task_is_set_as_done():
    task: Task = TaskFactory()
    task.complete()

    assert task.is_done


def test_raise_exception_when_try_complete_done_task():
    task: Task = TaskFactory()
    task.complete()

    with pytest.raises(TaskIsAlreadyDone):
        task.complete()
