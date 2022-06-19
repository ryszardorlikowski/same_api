import pytest

from boards.adapters.in_memory_boards_descriptors_repository import InMemoryBoardsDescriptorsRepository
from boards.adapters.in_memory_boards_repository import InMemoryBoardsRepository
from boards.application.repositories.boards import BoardsRepository
from boards.application.repositories.boards_descriptors import BoardsDescriptorsRepository
from boards.application.use_cases.create_board import CreateBoardInputDto, CreateBoard


@pytest.fixture
def boards_repo() -> BoardsRepository:
    return InMemoryBoardsRepository()


@pytest.fixture
def boards_descriptors_repo() -> BoardsDescriptorsRepository:
    return InMemoryBoardsDescriptorsRepository()


def test_new_board_is_created(boards_repo, boards_descriptors_repo):
    input_dto = CreateBoardInputDto(
        title="New board"
    )
    use_case = CreateBoard(boards_repo=boards_repo, boards_descriptors_repo=boards_descriptors_repo)

    use_case.execute(input_dto)

    boards = boards_repo.list()

    board_descriptor = boards_descriptors_repo.get(boards[0].id)

    assert len(boards) == 1
    assert board_descriptor.title == input_dto.title
