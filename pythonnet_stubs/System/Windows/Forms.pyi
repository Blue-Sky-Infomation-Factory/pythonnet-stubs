from typing import Final, Self, overload
from System import IntPtr
from System.ComponentModel import Component


class Control(Component):
	@overload
	def __init__(self): ...
	@overload
	def __init__(self, text: str): ...
	@overload
	def __init__(self, parent: Self, text: str): ...
	@overload
	def __init__(self, text: str, left: int, top: int, width: int, height: int): ...
	@overload
	def __init__(self, parent: Self, text: str, left: int, top: int, width: int, height: int): ...

	Handle: Final[IntPtr]