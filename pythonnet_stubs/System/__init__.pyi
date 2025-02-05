from abc import ABC
from typing import Callable, Final, Self, overload

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

class MemberInfo(ABC, CSharpObject):
	pass

class Type(ABC, MemberInfo):
	pass

class Uri(CSharpObject):
	@overload
	def __init__(self, uri: str): ...
	@overload
	def __init__(self, uri: str, escape: bool): ...

class __EventArgs_static(type):
	Empty: Final[EventArgs]
class EventArgs(CSharpObject, metaclass = __EventArgs_static):
	pass

class EventHandler[T, A](Delegate[None, T, A]):
	pass

class MarshalByRefObject(CSharpObject):
	pass

class ValueType(CSharpObject):
	def Equals(self, object: object) -> bool: ...
	def GetHashCode(self) -> int: ...
	def ToString(self) -> str: ...

class IntPtr(ValueType):
	def __init__(self, value: int): ...
	def ToInt32(self) -> int: ...

