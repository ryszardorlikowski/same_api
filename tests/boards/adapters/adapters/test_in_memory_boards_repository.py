import uuid

import pytest

from boards.adapters.in_memory_boards_repository import InMemoryBoardsRepository
from boards.application.repositories.boards import BoardDoesNotExist
from tests.boards.factories import BoardFactory


@pytest.fixture
def repo() -> InMemoryBoardsRepository:
    return InMemoryBoardsRepository()


def test_repo_save_board(repo):
    board = BoardFactory(id=uuid.uuid4())
    board_2 = BoardFactory(id=uuid.uuid4())

    repo.save(board)
    repo.save(board_2)

    assert len(repo._storage) == 2
    assert repo._storage[board.id].id == board.id


def test_get_board_from_repo(repo):
    board = BoardFactory(id=uuid.uuid4())
    repo.save(board)

    assert repo.get(board.id) == board


def test_rasie_exception_when_board_does_not_exist(repo):
    with pytest.raises(BoardDoesNotExist):
        repo.get(uuid.uuid4())


def test_get_boards_list(repo):
    board_list = []
    for _ in range(3):
        board = BoardFactory(id=uuid.uuid4())
        board_list.append(board)
        repo.save(board)

    assert repo.list() == board_list
