import pytest

from boards.adapters.in_memory_boards_repository import InMemoryBoardsRepository
from boards.application.repositories.boards import BoardsRepository
from boards.application.use_cases.create_task_on_board import CreateTaskOnBoard, CreateTaskOnBoardInputDto
from tests.boards.factories import BoardFactory


@pytest.fixture
def repo() -> BoardsRepository:
    return InMemoryBoardsRepository()


def test_new_task_is_added_to_board(repo: BoardsRepository) -> None:
    board = BoardFactory()
    repo.save(board)

    use_case = CreateTaskOnBoard(boards_repo=repo)

    input_dto = CreateTaskOnBoardInputDto(
        board_id=board.id,
        title="Task"
    )

    use_case.execute(input_dto)

    refreshed_board = repo.get(board.id)

    assert refreshed_board.number_of_tasks == 1
