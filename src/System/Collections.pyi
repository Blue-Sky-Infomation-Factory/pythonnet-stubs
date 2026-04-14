"""
https://learn.microsoft.com/en-us/dotnet/api/system.collections
"""

from abc import ABC, abstractmethod
from typing import Any, Iterator

from System import Array, ValueType


class IList(ABC):
	@abstractmethod
	def Add(self, value: Any, /) -> int: ...
	@abstractmethod
	def Clear(self) -> None: ...
	@abstractmethod
	def Contains(self, value: Any) -> bool: ...
	@abstractmethod
	def IndexOf(self, value: Any) -> int: ...
	@abstractmethod
	def Insert(self, index: int, value: Any) -> None: ...
	@abstractmethod
	def Remove(self, value: Any) -> None: ...
	@abstractmethod
	def RemoveAt(self, index: int) -> None: ...

	@property
	@abstractmethod
	def IsFixedSize(self) -> bool: ...
	@property
	@abstractmethod
	def IsReadOnly(self) -> bool: ...

	@abstractmethod
	def __getitem__(self, index: int) -> Any: ...
	@abstractmethod
	def __setitem__(self, index: int, value: Any) -> None: ...

class IEnumerator(ABC):
	@property
	@abstractmethod
	def Current(self) -> Any: ...

	@abstractmethod
	def MoveNext(self) -> bool: ...
	@abstractmethod
	def Reset(self) -> None: ...
	@abstractmethod
	def __next__(self) -> Any: ...

class IEnumerable(ABC):
	@abstractmethod
	def GetEnumerator(self) -> IEnumerator: ...

class ICollection(IEnumerable, ABC):
	#incomplete
	@abstractmethod
	def CopyTo(self, array: Array, index: int) -> None: ...

	@property
	@abstractmethod
	def Count(self) -> int: ...
	@property
	@abstractmethod
	def IsSynchronized(self) -> bool: ...
	@property
	@abstractmethod
	def SyncRoot(self) -> object: ...

class KeyValuePair[KT, VT](ValueType):
	# incomplete
	@property
	def Key(self) -> KT: ...
	@property
	def Value(self) -> VT: ...

class IDictionary(ICollection, ABC):
	@property
	@abstractmethod
	def IsFixedSize(self) -> bool: ...
	@property
	@abstractmethod
	def IsReadOnly(self) -> bool: ...
	@property
	@abstractmethod
	def Keys(self) -> ICollection: ...
	@property
	@abstractmethod
	def Values(self) -> ICollection: ...

	@abstractmethod
	def Add(self, key: Any, value: Any) -> None: ... # type: ignore
	@abstractmethod
	def Clear(self) -> None: ...
	@abstractmethod
	def Contains(self, key: Any) -> bool: ... # type: ignore
	@abstractmethod
	def GetEnumerator(self) -> IDictionaryEnumerator: ...
	@abstractmethod
	def Remove(self, key: Any) -> bool: ... # type: ignore

	@abstractmethod
	def __getitem__(self, key: Any) -> Any: ...
	@abstractmethod
	def __setitem__(self, key: Any, value: Any) -> None: ...

class DictionaryEntry(ValueType):
	# incomplete
	def __init__(self):
		self.Key: object
		self.Value: Any
	# def Deconstruct()

class IDictionaryEnumerator(IEnumerator, ABC):
	@property
	@abstractmethod
	def Entry(self) -> DictionaryEntry: ...
	@property
	@abstractmethod
	def Key(self) -> object: ...
	@property
	@abstractmethod
	def Value(self) -> Any: ...

class IStructuralComparable(ABC):
	# incomplete
	pass

class IStructuralEquatable(ABC):
	# incomplete
	pass