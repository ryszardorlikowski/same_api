import uuid
from dataclasses import dataclass
from datetime import datetime

from projects.domain.value_objects import TaskId, ProjectId
from foundation.exception import DomainException

TASKS_LIMIT: int = 20


class ProjectExceededLimit(DomainException):
    """"""


class NotUniqueTaskTitle(DomainException):
    """"""


class TaskIsAlreadyDone(DomainException):
    """"""


class CannotRemoveTaskFromDoneProject(DomainException):
    """"""


class NotFoundTaskInProject(DomainException):
    """"""


class CannotFinishProjectWithUncompletedTasks(DomainException):
    """"""


@dataclass
class Task:
    id: TaskId
    name: str
    created: datetime
    done: bool = False

    @property
    def is_done(self):
        return self.done

    def complete(self):
        if self.done:
            raise TaskIsAlreadyDone
        self.done = True


@dataclass
class Project:
    id: ProjectId
    name: str
    tasks: list[Task]
    done: bool = False

    def add_task(self, name: str) -> None:
        if self.number_of_tasks == TASKS_LIMIT:
            raise ProjectExceededLimit

        if not self.__is_task_name_unique(name):
            raise NotUniqueTaskTitle

        new_task = Task(
            id=uuid.uuid4(),
            name=name,
            created=datetime.now()
        )
        self.tasks.append(new_task)

    @property
    def is_done(self):
        return self.done

    @property
    def number_of_tasks(self) -> int:
        return len(self.tasks)

    def finish(self):
        if all([task.is_done for task in self.tasks]):
            self.done = True
        else:
            raise CannotFinishProjectWithUncompletedTasks

    def remove_task(self, task_id: TaskId) -> None:
        if self.done:
            raise CannotRemoveTaskFromDoneProject
        task: Task = self.__find_task(task_id)
        self.tasks.remove(task)

    def complete_task(self, task_id: TaskId) -> None:
        task: Task = self.__find_task(task_id)
        task.complete()

    def __find_task(self, task_id: TaskId) -> Task:
        try:
            task: Task = [task for task in self.tasks if task.id == task_id][0]
            return task
        except IndexError:
            raise NotFoundTaskInProject

    def __is_task_name_unique(self, title: str) -> bool:
        return all([not task.name == title for task in self.tasks])
