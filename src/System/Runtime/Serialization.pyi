"""
https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization
"""

from abc import ABC, abstractmethod
from System import Object, EventArgs, ValueType


class SerializationInfo(Object):
	# incomplete
	pass

class StreamingContext(ValueType):
	# incomplete
	pass

class SafeSerializationEventArgs(EventArgs):
	# incomplete
	pass

class ISerializable(ABC):
	@abstractmethod
	def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...