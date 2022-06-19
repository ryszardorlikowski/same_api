import uuid
from dataclasses import dataclass

from boards.application.repositories.boards import BoardsRepository
from boards.application.repositories.boards_descriptors import BoardsDescriptorsRepository
from boards.domain.entities import Board, BoardDescriptor


@dataclass
class CreateBoardInputDto:
    title: str


class CreateBoard:

    def __init__(self, boards_repo: BoardsRepository, boards_descriptors_repo: BoardsDescriptorsRepository):
        self._boards_repo = boards_repo
        self.boards_descriptors_repo = boards_descriptors_repo

    def execute(self, input_dto: CreateBoardInputDto):
        board_id = uuid.uuid4()
        self._boards_repo.save(Board(
            id=board_id,
            tasks=[]
        ))
        self.boards_descriptors_repo.save(BoardDescriptor(
            id=board_id,
            title=input_dto.title
        ))
