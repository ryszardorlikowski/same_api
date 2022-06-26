import uuid
from dataclasses import dataclass, field
from datetime import datetime

from foundation.event import EventMixin
from projects.domain import events
from projects.domain.exceptions import TaskIsAlreadyDone, ProjectExceededLimit, NotUniqueTaskTitle, \
    CannotFinishProjectWithUncompletedTasks, CannotRemoveTaskFromDoneProject, NotFoundTaskInProject
from projects.domain.value_objects import TaskId, ProjectId

PROJECT_TASKS_LIMIT: int = 20


@dataclass
class Task:
    id: TaskId
    name: str
    description: str
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
class Project(EventMixin):
    id: ProjectId
    name: str
    done: bool = False
    tasks: list[Task] = field(default_factory=list)

    def __post_init__(self) -> None:
        super().__post_init__()
        self._record_event(events.ProjectCreated(project_id=self.id))

    @property
    def is_done(self):
        return self.done

    @property
    def number_of_tasks(self) -> int:
        return len(self.tasks)

    def add_task(self, name: str, description: str = '') -> None:
        if self.number_of_tasks == PROJECT_TASKS_LIMIT:
            raise ProjectExceededLimit

        if not self.__is_task_name_unique(name):
            raise NotUniqueTaskTitle

        new_task = Task(
            id=uuid.uuid4(),
            name=name,
            description=description,
            created=datetime.now()
        )
        self.tasks.append(new_task)
        self._record_event(events.AddedProjectTask(project_id=self.id, task_id=new_task.id))

    def remove_task(self, task_id: TaskId) -> None:
        if self.done:
            raise CannotRemoveTaskFromDoneProject
        task: Task = self.__get_task(task_id)
        self.tasks.remove(task)
        self._record_event(events.RemovedProjectTask(project_id=self.id, task_name=task.name))

    def complete_task(self, task_id: TaskId) -> None:
        task: Task = self.__get_task(task_id)
        task.complete()
        self._record_event(events.CompletedProjectTask(project_id=self.id, task_id=task.id))

    def finish(self):
        if all([task.is_done for task in self.tasks]):
            self.done = True
            self._record_event(events.ProjectFinished(project_id=self.id))
            return
        raise CannotFinishProjectWithUncompletedTasks

    def __get_task(self, task_id: TaskId) -> Task:
        try:
            task: Task = [task for task in self.tasks if task.id == task_id][0]
            return task
        except IndexError:
            raise NotFoundTaskInProject

    def __is_task_name_unique(self, title: str) -> bool:
        return all([not task.name == title for task in self.tasks])
