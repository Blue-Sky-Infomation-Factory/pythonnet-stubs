"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms
"""

from abc import ABC
from enum import Enum
from typing import Final, List, Optional, Self, Union, overload
from System import CSharpObject, ICloneable, IntPtr
from System.ComponentModel import CancelEventArgs, Component
from System.Drawing import Size
from System.Collections import ICollection, IEnumerable, IList

class DockStyle(Enum):
	"""
	⚠ Special Key:<br>
	None = 0<br>
	getattr(DockStyle, "None")
	"""
	# The control is not docked.
	# None = 0
	# The control's top edge is docked to the top of its containing control.
	Top = 1
	# The control's bottom edge is docked to the bottom of its containing control.
	Bottom = 2
	# The control's left edge is docked to the left edge of its containing control.
	Left = 3
	# The control's right edge is docked to the right edge of its containing control.
	Right = 4
	# Al the control's edges are docked to the all edges of its containing control and sized appropriately.
	Fill = 5

class ArrangedElementCollection(CSharpObject, ICollection, IEnumerable, IList):
	pass

class Control(Component):
	# incomplete
	class ControlCollection(ArrangedElementCollection, ICloneable):
		def __init__(self, owner: Control):
			self.Owner: Final[Control]

		def __getitem__(self, index: Union[int, str]) -> Control: ...
		def __setitem__(self, index: Union[int, str], value: Control): ...

		def Add(self, value: Control) -> None: ...
		def Clear(self) -> None: ...
		def Contains(self, value: Control) -> bool: ...
		def IndexOf(self, value: Control) -> int: ...
		def Remove(self, value: Control) -> None: ...

		def AddRange(self, controls: List[Control]) -> None: ...
		def ContainsKey(self, key: str) -> bool: ...
		def IndexOfKey(self, key: str) -> int: ...
		def RemoveByKey(self, key: str) -> None: ...
		def Find(self, key: str, search_all_children: bool) -> List[Control]: ...
		def GetChildIndex(self, child: Control, throw_exception: bool = False) -> int: ...
		def SetChildIndex(self, child: Control, new_index: int) -> None: ...

	@overload
	def __init__(self):
		self.Handle: Final[IntPtr]
		self.Controls: Final[Control.ControlCollection]
	@overload
	def __init__(self, text: str): ...
	@overload
	def __init__(self, parent: Self, text: str): ...
	@overload
	def __init__(self, text: str, left: int, top: int, width: int, height: int): ...
	@overload
	def __init__(self, parent: Self, text: str, left: int, top: int, width: int, height: int): ...


class ScrollableControl(Control):
	# incomplete
	pass

class ContainerControl(ScrollableControl):
	# incomplete
	pass

class IWin32Window(ABC):
	# incomplete
	pass

class Form(ContainerControl):
	# incomplete
	def __init__(self):
		self.Size: Size
		self.Text: str
	def Show(self, owner: Optional[IWin32Window] = None) -> None: ...

class ApplicationContext(CSharpObject):
	# incomplete
	@overload
	def __init__(self): ...
	@overload
	def __init__(self, main_form: Form): ...

class Application(CSharpObject):
	# incomplete
	@overload
	@staticmethod
	def Run() -> None: ...
	@overload
	@staticmethod
	def Run(context: ApplicationContext) -> None: ...
	@overload
	@staticmethod
	def Run(main_form: Form) -> None: ...
	@overload
	@staticmethod
	def Exit() -> None: ...
	@overload
	@staticmethod
	def Exit(event: CancelEventArgs) -> None: ...
