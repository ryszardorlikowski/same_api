from dataclasses import dataclass

from boards.application.repositories.boards import BoardsRepository
from boards.domain.entities import Board
from boards.domain.value_objects import BoardId


@dataclass(frozen=True)
class CreateTaskOnBoardInputDto:
    board_id: BoardId
    title: str


class CreateTaskOnBoard:

    def __init__(self, boards_repo: BoardsRepository) -> None:
        self._boards_repo = boards_repo

    def execute(self, input_dto: CreateTaskOnBoardInputDto) -> None:
        board: Board = self._boards_repo.get(input_dto.board_id)
        board.create_task(title=input_dto.title)
        self._boards_repo.save(board)
