import uuid

import factory

from boards.domain.entities import Board, Task


class BoardFactory(factory.Factory):
    class Meta:
        model = Board

    id = uuid.uuid4()
    tasks = factory.List([])


class TaskFactory(factory.Factory):
    class Meta:
        model = Task

    id = uuid.uuid4()
    title = factory.Faker("name")
    created = factory.Faker("date_time")
    done = False
