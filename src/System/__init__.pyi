"""
https://learn.microsoft.com/en-us/dotnet/api/system
"""

from abc import ABC, abstractmethod
from typing import Callable, Final, Iterator, List, Optional, Self, Union, overload

from System.Runtime.Serialization import ISerializable, SafeSerializationEventArgs, SerializationInfo, StreamingContext
from System.Collections import ICollection, IDictionary, IEnumerable, IEnumerator, IList, IStructuralComparable, IStructuralEquatable
from System.Reflection import MethodBase

class Object:
	@staticmethod
	def Equals(object1: object, object2: object) -> bool: ... # type: ignore
	@staticmethod
	def ReferenceEquals(object1: object, object2: object) ->bool: ...
	def Equals(self, object: object) -> bool: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def MemberwiseClone(self) -> Self: ...
	def ToString(self) -> str: ...

class Delegate[RT, *AT](ABC):
	def __init__(self, method: Callable[[*AT], RT]): ...
	def __iadd__(self, method: Callable[[*AT], RT]) -> Self: ...
	def __isub__(self, method: Callable[[*AT], RT]) -> Self: ...

class Action[*AT](Delegate[None, *AT]): ...
class Func[*AT, RT](Delegate[RT, *AT]): ...

class MemberInfo(ABC, Object):
	# incomplete
	pass

class Type(MemberInfo, ABC):
	# incomplete
	pass

class Uri(Object):
	# incomplete
	@overload
	def __init__(self, uri: str): ...
	@overload
	def __init__(self, uri: str, escape: bool): ...

class __EventArgs_static(type):
	Empty: Final[EventArgs]
class EventArgs(Object, metaclass = __EventArgs_static): ...

class EventHandler[T, A: EventArgs](Delegate[None, T, A]): ...

class MarshalByRefObject(Object):
	# incomplete
	pass

class ValueType(Object):
	def Equals(self, object: object) -> bool: ...
	def GetHashCode(self) -> int: ...
	def ToString(self) -> str: ...

class IntPtr(ValueType):
	# incomplete
	def __init__(self, value: int): ...
	def ToInt32(self) -> int: ...

class Exception(Object, ISerializable):
	@overload
	def __init__(self):
		self.Data: Final[IDictionary]
		self.HelpLink: str
		self.HResult: int
		self.InnerException: Optional[Exception]
		self.Message: Final[str]
		self.Source: str
		self.StackTrace: Final[str]
		self.TargetSite: Final[Optional[MethodBase]]
		self.SerializeObjectState: EventHandler[object, SafeSerializationEventArgs]
	@overload
	def __init__(self, message: str): ...
	@overload
	def __init__(self, info: SerializationInfo, context: StreamingContext): ...
	@overload
	def __init__(self, message: str, inner_exception: Exception): ...

	def GetBaseException(self) -> Exception: ...
	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
	def GetType(self) -> Type: ...
	def ToString(self) -> str: ...

class AggregateException(Exception): ...

class ICloneable(ABC):
	@abstractmethod
	def Clone(self) -> Self: ...

class Array[T](Object, ICollection, IEnumerable, IList, IStructuralComparable, IStructuralEquatable, ICloneable):
	# incomplete
	def __getitem__(self, index: int) -> T: ...
	def __setitem__(self, index: int, value: T) -> None: ...
	def __len__(self) -> int: ...
	def __iter__(self) -> Iterator[T]: ...

type _inbound_array[T] = Union[Array[T], List[T]]

class IDisposable(ABC):
	# incomplete
	pass

class IKeyboardInputSink(ABC):
	# incomplete
	pass

class IWin32Window(ABC):
	# incomplete
	pass

class IFormattable(ABC):
	# incomplete
	pass

class IEquatable[T](ABC):
	@abstractmethod
	def Equals(self, other: T, /) -> bool: ...