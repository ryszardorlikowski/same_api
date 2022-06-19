import uuid
from datetime import datetime

import pytest
from pytest import fixture

from boards.domain.entities import Board, Task, BOARD_TASKS_LIMIT, BoardExceededTasksLimit, NotUniqueTaskTitleInBoard, \
    TaskIsAlreadyDone
from tests.random_refs import random_suffix


@fixture
def board() -> Board:
    return Board(
        id=uuid.uuid4(),
        title="Board",
        tasks=[]
    )


@fixture
def task() -> Task:
    return Task(
        id=uuid.uuid4(),
        title=f"Task {random_suffix()}",
        created=datetime.now()

    )


def test_board_raise_exception_if_number_of_tasks_has_exceeded_the_limit(board: Board):
    for _ in range(BOARD_TASKS_LIMIT):
        task_title = f"Task {random_suffix()}"
        board.add_new_task(title=task_title)

    with pytest.raises(BoardExceededTasksLimit):
        task_title = f"Task {random_suffix()}"
        board.add_new_task(title=task_title)


def test_board_raise_exception_when_adding_task_with_not_unique_title(board: Board):
    task_title = "Task name"
    board.add_new_task(title=task_title)
    with pytest.raises(NotUniqueTaskTitleInBoard):
        board.add_new_task(title=task_title)


def test_task_is_removed_from_board(board: Board, task: Task):
    board.tasks.append(task)
    board.remove_task(task.id)
    assert board.number_of_tasks == 0


def test_task_is_set_as_done(task: Task):
    task.complete_task()

    assert task.is_done


def test_raise_exception_when_try_complete_done_task(task: Task):
    task.complete_task()

    with pytest.raises(TaskIsAlreadyDone):
        task.complete_task()
