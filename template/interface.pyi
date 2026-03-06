from abc import ABC, abstractmethod
from typing import Any


class Interface(ABC):
	@abstractmethod
	def method(self, arg: Any) -> Any: ...

	@property
	@abstractmethod
	def getter(self) -> Any: ...