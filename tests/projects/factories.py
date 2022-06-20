import uuid

import factory

from projects.domain.entities import Project, Task


class ProjectFactory(factory.Factory):
    class Meta:
        model = Project

    id = uuid.uuid4()
    name = factory.Faker("name")
    tasks = factory.List([])
    done = False


class TaskFactory(factory.Factory):
    class Meta:
        model = Task

    id = uuid.uuid4()
    name = factory.Faker("name")
    created = factory.Faker("date_time")
    done = False
