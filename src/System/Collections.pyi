from abc import ABC, abstractmethod
from typing import Any, List

from System import ValueType


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

class IEnumerator[T](ABC):
	@property
	@abstractmethod
	def Current(self) -> T: ...

	@abstractmethod
	def MoveNext(self) -> bool: ...
	@abstractmethod
	def Reset(self) -> None: ...

class IEnumerable[T](ABC):
	@abstractmethod
	def GetEnumerator(self) -> IEnumerator[T]: ...

class ICollection[T](IEnumerable[T], ABC):
	#incomplete
	@abstractmethod
	def CopyTo(self, array: List[T], index: int) -> None: ...

	@property
	@abstractmethod
	def Count(self) -> int: ...
	@property
	@abstractmethod
	def IsSynchronized(self) -> bool: ...
	@property
	@abstractmethod
	def SyncRoot(self) -> object: ...

	@abstractmethod
	def Add(self, item: T) -> None: ...
	@abstractmethod
	def clear(self) -> None: ...
	@abstractmethod
	def Contains(self, item: T, /) -> bool: ...
	@abstractmethod
	def Remove(self, item: T, /) -> bool: ...

class KeyValuePair[KT, VT](ValueType):
	# incomplete
	@property
	def Key(self) -> KT: ...
	@property
	def Value(self) -> VT: ...

class IDictionary[KT, VT](ICollection[KeyValuePair[KT, VT]], ABC):
	@property
	@abstractmethod
	def IsFixedSize(self) -> bool: ...
	@property
	@abstractmethod
	def IsReadOnly(self) -> bool: ...
	@property
	@abstractmethod
	def Keys(self) -> ICollection[KT]: ...
	@property
	@abstractmethod
	def Values(self) -> ICollection[VT]: ...

	@abstractmethod
	def Add(self, key: KT, value: VT) -> None: ... # type: ignore
	@abstractmethod
	def Clear(self) -> None: ...
	@abstractmethod
	def Contains(self, key: KT) -> bool: ... # type: ignore
	@abstractmethod
	def GetEnumerator(self) -> IDictionaryEnumerator: ...
	@abstractmethod
	def Remove(self, key: KT) -> bool: ... # type: ignore

	@abstractmethod
	def __getitem__(self, key: KT) -> VT: ...
	@abstractmethod
	def __setitem__(self, key: KT, value: VT) -> None: ...

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