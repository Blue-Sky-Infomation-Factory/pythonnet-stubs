from abc import ABC, ABCMeta, abstractmethod
from enum import Enum
from typing import Final, overload
from System import AggregateException, CSharpObject, EventArgs, EventHandler, Exception
from System.Threading import CancellationToken

class TaskCreationOptions(Enum):
	"""
	⚠ Special key:<br>
	None = 0<br>
	getattr(TaskCreationOptions, "None")
	"""
	# None = 0
	PreferFairness = 1
	LongRunning = 2
	AttachedToParent = 4
	DenyChildAttach = 8
	HideScheduler = 16
	RunContinuationsAsynchronously = 64

class Task[RT]:
	# incomplete
	pass

class UnobservedTaskExceptionEventArgs(EventArgs):
	# incomplete
	def __init__(self):
		self.Exception: Final[AggregateException]

class __TaskScheduler_static(ABCMeta):
	Current: Final[TaskScheduler]
	Default: Final[TaskScheduler]
	UnobservedTaskException: EventHandler[object, UnobservedTaskExceptionEventArgs]
class TaskScheduler(ABC, CSharpObject, metaclass=__TaskScheduler_static):
	def __init__(self):
		self.Id: Final[int]
	@property
	@abstractmethod
	def MaximumConcurrencyLevel(self) -> int: ...

class TaskCompletionSource[RT](CSharpObject):
	@overload
	def __init__(self):
		self.Task: Final[Task]
	@overload
	def __init__(self, state: object): ...
	@overload
	def __init__(self, creation_options: TaskCreationOptions): ...
	@overload
	def __init__(self, state: object, creation_options: TaskCreationOptions): ...

	@overload
	def SetCanceled(self) -> None: ...
	@overload
	def SetCanceled(self, cancellation_token: CancellationToken) -> None: ...
	def SetException(self, exception: Exception) -> None: ...
	def SetFromTask(self, completedTask: Task[RT]) -> None: ...
	def SetResult(self, result: RT) -> None: ...
	@overload
	def TrySetCanceled(self) -> None: ...
	@overload
	def TrySetCanceled(self, cancellation_token: CancellationToken) -> bool: ...
	def TrySetException(self, exception: Exception) -> bool: ...
	def TrySetFromTask(self, completedTask: Task[RT]) -> bool: ...
	def TrySetResult(self, result: RT) -> bool: ...
