import uuid
from datetime import datetime

import pytest

from boards.domain.entities import Board, Task, BOARD_TASKS_LIMIT, BoardExceededTasksLimit, NotUniqueTaskTitleInBoard, \
    TaskIsAlreadyDone
from tests.boards.factories import BoardFactory, TaskFactory
from tests.random_refs import random_suffix


def test_board_raise_exception_if_number_of_tasks_has_exceeded_the_limit():
    board: Board = BoardFactory()
    for _ in range(BOARD_TASKS_LIMIT):
        task_title = f"Task {random_suffix()}"
        board.create_task(title=task_title)

    with pytest.raises(BoardExceededTasksLimit):
        task_title = f"Task {random_suffix()}"
        board.create_task(title=task_title)


def test_board_raise_exception_when_create_task_with_not_unique_title():
    board: Board = BoardFactory()
    task_title = "Task name"
    board.create_task(title=task_title)
    with pytest.raises(NotUniqueTaskTitleInBoard):
        board.create_task(title=task_title)


def test_task_is_removed_from_board():
    board: Board = BoardFactory()
    task: Task = TaskFactory()
    board.tasks.append(task)
    board.remove_task(task.id)
    assert board.number_of_tasks == 0


def test_task_is_set_as_done():
    task: Task = TaskFactory()
    task.complete_task()

    assert task.is_done


def test_raise_exception_when_try_complete_done_task():
    task: Task = TaskFactory()
    task.complete_task()

    with pytest.raises(TaskIsAlreadyDone):
        task.complete_task()
