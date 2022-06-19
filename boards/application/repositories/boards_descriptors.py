import abc

from boards.domain.entities import BoardDescriptor
from boards.domain.value_objects import BoardId


class BoardDescriptorDoesNotExist(Exception):
    """"""


class BoardsDescriptorsRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, board_id: BoardId) -> BoardDescriptor:
        """"""

    @abc.abstractmethod
    def save(self, board: BoardDescriptor) -> None:
        """"""

    @abc.abstractmethod
    def delete(self, board_id: BoardId) -> None:
        """"""
