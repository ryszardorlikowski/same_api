import copy

from boards.application.repositories.boards import BoardsRepository, BoardDoesNotExist
from boards.domain.entities import Board
from boards.domain.value_objects import BoardId


class InMemoryBoardsRepository(BoardsRepository):

    def __init__(self):
        self._storage: dict[BoardId, Board] = {}

    def get(self, board_id: BoardId) -> Board:
        try:
            return copy.deepcopy(self._storage[board_id])
        except KeyError:
            raise BoardDoesNotExist

    def save(self, board: Board) -> None:
        self._storage[board.id] = copy.deepcopy(board)

    def list(self):
        return [board for board in self._storage.values()]

    def delete(self, board_id: BoardId) -> None:
        raise NotImplementedError
