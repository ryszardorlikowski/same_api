import abc

from boards.domain.entities import Board
from boards.domain.value_objects import BoardId


class BoardDoesNotExist(Exception):
    """"""


class BoardsRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, board_id: BoardId) -> Board:
        pass

    @abc.abstractmethod
    def save(self, board: Board) -> None:
        pass

    @abc.abstractmethod
    def delete(self, board_id: BoardId) -> None:
        pass

    @abc.abstractmethod
    def list(self):
        pass
