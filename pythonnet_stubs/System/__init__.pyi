from abc import ABC
from functools import singledispatchmethod
from typing import Callable, Final, Self

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

class MemberInfo(ABC, CSharpObject):
	pass

class Type(ABC, MemberInfo):
	pass

class Uri(CSharpObject):
	@singledispatchmethod
	def __init__(self, uri: str): ...
	@__init__.register
	def _(self, uri: str, escape: bool): ...

class __EventArgs_static(type):
	Empty: Final[EventArgs]
class EventArgs(CSharpObject, metaclass = __EventArgs_static):
	pass

class EventHandler[T, A]:
	def __iadd__(self, handler: Callable[[T, A], None]) -> Self: ...

class MarshalByRefObject(CSharpObject):
	pass

class ValueType(CSharpObject):
	def Equals(self, object: object) -> bool: ...
	def GetHashCode(self) -> int: ...
	def ToString(self) -> str: ...
