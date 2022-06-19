import copy

from boards.application.repositories.boards_descriptors import BoardsDescriptorsRepository, BoardDescriptorDoesNotExist
from boards.domain.entities import Board, BoardDescriptor
from boards.domain.value_objects import BoardId


class InMemoryBoardsDescriptorsRepository(BoardsDescriptorsRepository):

    def __init__(self):
        self._storage: dict[BoardId, Board] = {}

    def get(self, board_id: BoardId) -> Board:
        try:
            return copy.deepcopy(self._storage[board_id])
        except KeyError:
            raise BoardDescriptorDoesNotExist

    def save(self, board: Board) -> None:
        self._storage[board.id] = copy.deepcopy(board)

    def delete(self, board_id: BoardId) -> None:
        pass
