"""
https://learn.microsoft.com/en-us/dotnet/api/system.threading
"""

from enum import Enum
from typing import Any, Final, Optional, overload
from System import Object, Delegate, MarshalByRefObject, TimeSpan, ValueType
from System.Globalization import CultureInfo
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Security.Principal import IPrincipal

class ExecutionContext(Object):
	# incomplete
	pass

class ApartmentState(Enum):
	# The Thread will create and enter a single-threaded apartment.
	STA = 0
	# The Thread will create and enter a multithreaded apartment.
	MTA = 1
	# The ApartmentState property has not been set.
	Unknown = 2

class ThreadPriority(Enum):
	Lowest = 0
	BelowNormal = 1	
	Normal = 2
	AboveNormal = 3
	Highest = 4

class ThreadState(Enum):
	Running = 0
	StopRequested = 1
	SuspendRequested = 2
	Background = 4
	Unstarted = 8
	Stopped = 16
	WaitSleepJoin = 32
	Suspended = 64
	AbortRequested = 128
	Aborted = 256

class WaitHandle(MarshalByRefObject):
	# incomplete
	pass

class __CancellationToken_static(type):
	# None: Final[CancellationToken]
	pass
class CancellationToken(ValueType, metaclass=__CancellationToken_static):
	"""
	⚠ Special static key:<br>
	None -> getattr(CancellationToken, "None")
	"""
	# incomplete
	def __init__(self, canceled: bool):
		self.CanBeCanceled: Final[bool]
		self.IsCancellationRequested: Final[bool]
		self.WaitHandle: Final[WaitHandle]

class ThreadStart(Delegate[None]): ...

class ParameterizedThreadStart(Delegate[None, Any]): ...

class __Thread_static(type):
	CurrentPrincipal: IPrincipal
	CurrentThread: Final[Thread]
class Thread(CriticalFinalizerObject, metaclass = __Thread_static):
	# incomplete
	@overload
	def __init__(self, start: ThreadStart):
		self.CurrentCulture: CultureInfo
		self.CurrentUICulture: CultureInfo
		self.ExecutionContext: Final[Optional[ExecutionContext]]
		self.IsAlive: Final[bool]
		self.IsBackground: bool
		self.IsThreadPoolThread: Final[bool]
		self.ManagedThreadId: Final[int]
		self.Name: Optional[str]
		self.Priority: ThreadPriority
		self.ThreadState: Final[ThreadState]
	@overload
	def __init__(self, start: ThreadStart, max_stack_size: int): ...
	@overload
	def __init__(self, start: ParameterizedThreadStart): ...
	@overload
	def __init__(self, start: ParameterizedThreadStart, max_stack_size: int): ...

	def GetApartmentState(self) -> ApartmentState: ...
	def SetApartmentState(self, state: ApartmentState) -> None: ...
	@overload
	def Join(self) -> None: ...
	@overload
	def Join(self, milliseconds_timeout: int) -> bool: ...
	@overload
	def Join(self, timeout: TimeSpan) -> bool: ...
	@overload
	def Start(self) -> None: ...
	@overload
	def Start(self, parameter: Any) -> None: ...

class SendOrPostCallback(Delegate[None, Any]): ...

class __SynchronizationContext_static(type):
	Current: Final[Optional[SynchronizationContext]]
class SynchronizationContext(Object, metaclass=__SynchronizationContext_static):
	# incomplete
	def __init__(self) :...
	def Post(self, d: SendOrPostCallback, arg: Any) -> None: ...
	def Send(self, d: SendOrPostCallback, arg: Any) -> None: ...

	@classmethod
	def SetSynchronizationContext(cls, syncContext: Optional[SynchronizationContext]) -> None: ...