"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows
"""

from abc import ABC
from enum import Enum
from typing import Self, overload

from System import EventArgs, EventHandler
from System.ComponentModel import ISupportInitialize
from System.Windows.Controls import ContentControl
from System.Windows.Markup import IQueryAmbient
from System.Windows.Media import Visual
from System.Windows.Media.Animation import IAnimatable
from System.Windows.Threading import DispatcherObject

class HorizontalAlignment(Enum):
	# An element aligned to the left of the layout slot for the parent element.
	Left = 0
	# An element aligned to the center of the layout slot for the parent element.
	Center = 1
	# An element aligned to the right of the layout slot for the parent element.
	Right = 2
	# An element stretched to fill the entire layout slot of the parent element.
	Stretch = 3

class VerticalAlignment(Enum):
	# The child element is aligned to the top of the parent's layout slot.
	Top = 0
	# The child element is aligned to the center of the parent's layout slot.
	Center = 1
	# The child element is aligned to the bottom of the parent's layout slot.
	Bottom = 2
	# The child element stretches to fill the parent's layout slot.
	Stretch = 3

class ShutdownMode(Enum):
	# An application shuts down when either the last window closes, or Shutdown() is called.
	OnLastWindowClose = 0
	# An application shuts down when either the main window closes, or Shutdown() is called.
	OnMainWindowClose = 1
	# An application shuts down only when Shutdown() is called.
	OnExplicitShutdown = 2

class Application(DispatcherObject, IQueryAmbient):
	@overload
	def Run(self) -> int:...
	@overload
	def Run(self, window: Window) -> int:...
	@overload
	def Shutdown(self) -> None: ...
	@overload
	def Shutdown(self, code: int) -> None: ...
	@property
	def ShutdownMode(self) -> ShutdownMode: ...
	@ShutdownMode.setter
	def ShutdownMode(self, value: ShutdownMode) -> None: ...

class DependencyObject(DispatcherObject):
	#incomplete
	pass

class Freezable(DependencyObject, ABC):
	#incomplete
	pass

class IInputElement(ABC):
	#incomplete
	pass

class UIElement(Visual, IInputElement, IAnimatable):
	#incomplete
	pass

class IFrameworkInputElement(ABC):
	#incomplete
	pass

class FrameworkElement(UIElement, ISupportInitialize, IFrameworkInputElement, IQueryAmbient):
	#incomplete
	@property
	def Width(self) -> float: ...
	@Width.setter
	def Width(self, value: float) -> None: ...
	@property
	def Height(self) -> float: ...
	@Height.setter
	def Height(self, value: float) -> None: ...
	@property
	def MinWidth(self) -> float: ...
	@MinWidth.setter
	def MinWidth(self, value: float) -> None: ...
	@property
	def MinHeight(self) -> float: ...
	@MinHeight.setter
	def MinHeight(self, value: float) -> None: ...
	@property
	def MaxWidth(self) -> float: ...
	@MaxWidth.setter
	def MaxWidth(self, value: float) -> None: ...
	@property
	def MaxHeight(self) -> float: ...
	@MaxHeight.setter
	def MaxHeight(self, value: float) -> None: ...
	@property
	def HorizontalAlignment(self) -> HorizontalAlignment:...
	@HorizontalAlignment.setter
	def HorizontalAlignment(self, value: HorizontalAlignment) -> None:...
	@property
	def VerticalAlignment(self) -> VerticalAlignment:...
	@VerticalAlignment.setter
	def VerticalAlignment(self, value: VerticalAlignment) -> None:...

class ContentElement(DependencyObject, IInputElement, IAnimatable):
	#incomplete
	pass

class FrameworkContentElement(ContentElement, ISupportInitialize, IFrameworkInputElement, IInputElement, IQueryAmbient):
	#incomplete
	pass

class Window(ContentControl):
	#incomplete
	def __init__(self):
		self.Closed: EventHandler[Self, EventArgs]
	@property
	def Title(self) -> str: ...
	@Title.setter
	def Title(self, value: str) -> None: ...
	def Show(self) -> None: ...
	def Close(self) -> None: ...