import copy

from boards.application.repositories.boards import BoardsRepository
from boards.domain.entities import Board
from boards.domain.value_objects import BoardId


class InMemoryBoardsRepository(BoardsRepository):

    def __int__(self):
        self._storage: dict[BoardId, Board] = {}

    def get(self, board_id: BoardId) -> Board:
        return copy.deepcopy(self._storage[board_id])

    def save(self, board: Board) -> None:
        self._storage[board.id] = Board
