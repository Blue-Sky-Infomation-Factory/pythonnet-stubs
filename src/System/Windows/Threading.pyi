"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows.threading
"""

from typing import Final, Optional, Tuple, Unpack

from System import Delegate, Object

class Dispatcher(Object):
	# incomplete
	def Invoke[RT, *AT](self, method: Delegate[RT, Unpack[AT]], args: Tuple[Unpack[AT]]) -> Optional[RT]: ...

class DispatcherObject(Object):
	def __init__(self): # protected
		self.Dispatcher: Final[Dispatcher]