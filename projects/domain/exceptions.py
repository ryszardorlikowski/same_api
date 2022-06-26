from foundation.exception import DomainException


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
