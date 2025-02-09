"""
https://learn.microsoft.com/en-us/dotnet/api/system
"""

from abc import ABC, abstractmethod
from typing import Callable, Final, Optional, Self, overload

from System.Runtime.Serialization import ISerializable, SafeSerializationEventArgs, SerializationInfo, StreamingContext
from System.Collections import ICollection, IDictionary, IEnumerable, IList, IStructuralComparable, IStructuralEquatable
from System.Reflection import MethodBase

class CSharpObject:
	@staticmethod
	def Equals(object1: object, object2: object) -> bool: ... # type: ignore
	@staticmethod
	def ReferenceEquals(object1: object, object2: object) ->bool: ...
	def Equals(self, object: object) -> bool: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def MemberwiseClone(self) -> Self: ...
	def ToString(self) -> str: ...

class Delegate[RT, *AT]:
	def __init__(self, method: Callable[[*AT], RT]): ...
	def __iadd__(self, method: Callable[[*AT], RT]) -> Self: ...

class Action[*AT](Delegate[None, *AT]): ...

class MemberInfo(ABC, CSharpObject):
	# incomplete
	pass

class Type(ABC, MemberInfo): # type: ignore
	# incomplete
	pass

class Uri(CSharpObject):
	# incomplete
	@overload
	def __init__(self, uri: str): ...
	@overload
	def __init__(self, uri: str, escape: bool): ...

class __EventArgs_static(type):
	Empty: Final[EventArgs]
class EventArgs(CSharpObject, metaclass = __EventArgs_static): ...

class EventHandler[T, A: EventArgs](Delegate[None, T, A]): ...

class MarshalByRefObject(CSharpObject):
	# incomplete
	pass

class ValueType(CSharpObject):
	def Equals(self, object: object) -> bool: ...
	def GetHashCode(self) -> int: ...
	def ToString(self) -> str: ...

class IntPtr(ValueType):
	# incomplete
	def __init__(self, value: int): ...
	def ToInt32(self) -> int: ...

class Exception(CSharpObject, ISerializable):
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

class Array[T](CSharpObject, ICollection, IEnumerable, IList, IStructuralComparable, IStructuralEquatable, ICloneable):
	# incomplete
	pass