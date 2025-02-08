"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms
"""

from abc import ABC
from enum import Enum
from typing import Final, List, Optional, Self, Union, overload
from System import CSharpObject, EventArgs, EventHandler, ICloneable, IntPtr
from System.ComponentModel import CancelEventArgs, Component
from System.Drawing import Size, Color
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

class CloseReason(Enum):
	"""
	⚠ Special Key:<br>
	None = 0<br>
	getattr(CloseReason, "None")
	"""
	# The cause of the closure was not defined or could not be determined.
	# None = 0
	# The operating system is closing all applications before shutting down.
	WindowsShutDown = 1
	# The parent form of this multiple document interface (MDI) form is closing.
	MdiFormClosing = 2
	# The form is closing either programmatically or through a user action in the user interface (for example, by clicking the Close button on the form window, selecting Close from the window's control menu, or pressing ALT+F4).
	UserClosing = 3
	# The Microsoft Windows Task Manager is closing the application.
	# In Windows 8.1 and later versions, this member is not used, because Task Manager issues the WM_SYSCOMMAND message with SC_CLOSE. In Windows 7 and earlier versions, the WM_CLOSE message was issued. This action is now indistinguishable from and misclassified as CloseReason.UserClosing.
	TaskManagerClosing = 4
	# The owner form is closing.
	FormOwnerClosing = 5
	# The Exit() method of the Application class was invoked.
	ApplicationExitCall = 6

class FormClosedEventArgs(EventArgs):
	def __init__(self, close_reason: CloseReason):
		self.CloseReason: Final[CloseReason]

class FormClosedEventHandler(EventHandler[Form, FormClosedEventArgs]): ...

class ArrangedElementCollection(CSharpObject, ICollection, IEnumerable, IList): ...

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
		self.Dock: DockStyle
		self.BackColor: Color
		self.DefaultBackColor : Final[Color]
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
		self.BackColor: Color
		self.TransparencyKey: Color

		self.Closed: FormClosedEventHandler
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
