from dataclasses import dataclass

from foundation.event import Event
from projects.domain.value_objects import ProjectId, TaskId


@dataclass
class ProjectIsCreated(Event):
    project_id: ProjectId
    name: str


@dataclass
class AddedNewTaskToProject(Event):
    project_id: ProjectId
    task_id: TaskId
    task_name: str
