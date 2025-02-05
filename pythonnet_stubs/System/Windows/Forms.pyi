"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms
"""

from typing import Final, Self, overload
from System import CSharpObject, IntPtr
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

class ScrollableControl(Control):
	pass

class ContainerControl(ScrollableControl):
	pass

class Form(ContainerControl):
	pass

class ApplicationContext(CSharpObject):
	@overload
	def __init__(self): ...
	@overload
	def __init__(self, main_form: Form): ...