from dataclasses import dataclass

from foundation.event import Event
from projects.domain.value_objects import ProjectId, TaskId


@dataclass
class ProjectCreated(Event):
    project_id: ProjectId


@dataclass
class ProjectFinished(Event):
    project_id: ProjectId


@dataclass
class AddedProjectTask(Event):
    project_id: ProjectId
    task_id: TaskId


@dataclass
class RemovedProjectTask(Event):
    project_id: ProjectId
    task_name: str


@dataclass
class CompletedProjectTask(Event):
    project_id: ProjectId
    task_id: TaskId
