from abc import ABC, abstractmethod
from typing import Any

from System import Array, IDisposable
from System.Collections import IEnumerable as n_IEnumerable, IEnumerator as n_IEnumerator

class IEnumerator[T](n_IEnumerator, IDisposable, ABC):
	@property
	@abstractmethod
	def Current(self) -> T: ...

class IEnumerable[T](n_IEnumerable, ABC):
	@abstractmethod
	def GetEnumerator(self) -> IEnumerator[T]: ...

class ICollection[T](IEnumerable[T], ABC):
	@property
	@abstractmethod
	def Count(self) -> int: ...
	@property
	@abstractmethod
	def IsReadOnly(self) -> bool: ...

	@abstractmethod
	def Add(self, value: T, /) -> int: ...
	@abstractmethod
	def Clear(self) -> None: ...
	@abstractmethod
	def Contains(self, value: T) -> bool: ...
	@abstractmethod
	def CopyTo(self, array: Array[T], index: int) -> None: ...
	@abstractmethod
	def Remove(self, value: T) -> None: ...