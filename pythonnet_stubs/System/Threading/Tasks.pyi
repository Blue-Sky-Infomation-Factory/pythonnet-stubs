from abc import ABC, abstractmethod
from typing import Final
from System import AggregateException, CSharpObject, EventArgs, EventHandler


class Task[RT]:
	# incomplete
	pass

class UnobservedTaskExceptionEventArgs(EventArgs):
	# incomplete
	def __init__(self):
		self.Exception[Final[AggregateException]]

class __TaskScheduler_static(type):
	Current: Final[TaskScheduler]
	Default: Final[TaskScheduler]
	UnobservedTaskException: EventHandler[object, UnobservedTaskExceptionEventArgs]
class TaskScheduler(ABC, CSharpObject, metaclass=__TaskScheduler_static):
	def __init__(self):
		self.Id: Final[int]
	@abstractmethod
	@property
	def MaximumConcurrencyLevel(self) -> int: ...