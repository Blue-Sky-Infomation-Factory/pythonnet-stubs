"""
https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization
"""

from abc import ABC, abstractmethod
from System import CSharpObject, EventArgs, ValueType


class SerializationInfo(CSharpObject):
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