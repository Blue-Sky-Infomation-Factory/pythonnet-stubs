from abc import ABC, abstractmethod
from typing import Any, List

from System import ValueType


class IList(ABC):
	@abstractmethod
	def Add(self, value: Any) -> int: ...
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

	@abstractmethod
	@property
	def IsFixedSize(self) -> bool: ...
	@abstractmethod
	@property
	def IsReadOnly(self) -> bool: ...

	@abstractmethod
	def __getitem__(self, index: int) -> Any: ...
	@abstractmethod
	def __setitem__(self, index: int, value: Any) -> None: ...

class ICollection(ABC):
	@abstractmethod
	def CopyTo(self, array: List, index: int) -> None: ...

	@abstractmethod
	@property
	def Count(self) -> int: ...
	@abstractmethod
	@property
	def IsSynchronized(self) -> bool: ...
	@abstractmethod
	@property
	def SyncRoot(self) -> object: ...

class IEnumerator(ABC):
	@abstractmethod
	@property
	def Current(self) -> Any: ...

	@abstractmethod
	def MoveNext(self) -> bool: ...
	@abstractmethod
	def Reset(self) -> None: ...

class IEnumerable(ABC):
	@abstractmethod
	def GetEnumerator(self) -> IEnumerator: ...

class IDictionary(ABC, ICollection, IEnumerable):
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
	def Add(self, key: object, value: Any) -> None: ...
	@abstractmethod
	def Clear(self) -> None: ...
	@abstractmethod
	def Contains(self, key: object) -> bool: ...
	@abstractmethod
	def GetEnumerator(self) -> IDictionaryEnumerator: ...
	@abstractmethod
	def Remove(self, key: object) -> bool: ...

	@abstractmethod
	def __getitem__(self, key: object) -> object: ...
	@abstractmethod
	def __setitem__(self, key: object, value: Any) -> None: ...

class DictionaryEntry(ValueType):
	# incomplete
	def __init__(self):
		self.Key: object
		self.Value: Any
	# def Deconstruct()

class IDictionaryEnumerator(ABC, IEnumerator):
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