"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows
"""

from abc import ABC
from enum import Enum
from typing import Optional, Self, overload

from System import EventArgs, EventHandler, IEquatable, ValueType
from System.ComponentModel import ISupportInitialize
from System.Windows.Controls import ContentControl
from System.Windows.Markup import IQueryAmbient
from System.Windows.Media import ImageSource, Visual
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
	@property
	def MainWindow(self) -> Optional[Window]:...
	@MainWindow.setter
	def MainWindow(self, value: Optional[Window]) -> None:...

class DependencyObject(DispatcherObject):
	#incomplete
	pass

class Freezable(DependencyObject, ABC):
	#incomplete
	@property
	def CanFreeze(self) -> bool: ...
	@property
	def IsFrozen(self) -> bool: ...
	def Clone(self) -> Self: ...
	def Freeze(self) -> None: ...

class IInputElement(ABC):
	#incomplete
	pass

class UIElement(Visual, IInputElement, IAnimatable):
	#incomplete
	@property
	def IsVisible(self) -> bool: ...

class IFrameworkInputElement(ABC):
	#incomplete
	pass

class Thickness(ValueType, IEquatable[Thickness]):
	@overload
	def __init__(self, uniformLength: float): ...
	@overload
	def __init__(self, left: float, top: float, right: float, bottom: float): ...
	@property
	def Left(self) -> float: ...
	@Left.setter
	def Left(self, value: float) -> None: ...
	@property
	def Top(self) -> float: ...
	@Top.setter
	def Top(self, value: float) -> None: ...
	@property
	def Right(self) -> float: ...
	@Right.setter
	def Right(self, value: float) -> None: ...
	@property
	def Bottom(self) -> float: ...
	@Bottom.setter
	def Bottom(self, value: float) -> None: ...
	def Equals(self, other: Thickness) -> bool: ... # pyright: ignore[reportIncompatibleMethodOverride]

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
	def Margin(self) -> Thickness:...
	@Margin.setter
	def Margin(self, value: Thickness) -> None:...
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

class WindowState(Enum):
	# The window is restored.
	Normal = 0
	# The window is minimized.
	Minimized = 1
	# The window is maximized.
	Maximized = 2

class WindowStyle(Enum):
	"""
	⚠ Special static key:<br>
	None -> getattr(WindowStyle, "None")
	"""
	# Only the client area is visible - the title bar and border are not shown. A NavigationWindow with a WindowStyle of None will still display the navigation user interface (UI).
	# None = 0
	# A window with a single border. This is the default value.
	SingleBorderWindow = 1
	# A window with a 3-D border.
	ThreeDBorderWindow = 2
	# A fixed tool window.
	ToolWindow = 3

class ResizeMode(Enum):
	# A window cannot be resized. The Minimize and Maximize buttons are not displayed in the title bar.
	NoResize = 0
	# A window can only be minimized and restored. The Minimize and Maximize buttons are both shown, but only the Minimize button is enabled.
	CanMinimize = 1
	# A window can be resized. The Minimize and Maximize buttons are both shown and enabled.
	CanResize = 2
	# A window can be resized. The Minimize and Maximize buttons are both shown and enabled. A resize grip appears in the bottom-right corner of the window.
	CanResizeWithGrip = 3

class Window(ContentControl):
	#incomplete
	def __init__(self):
		self.Closed: EventHandler[Self, EventArgs]
	@property
	def Title(self) -> str: ...
	@Title.setter
	def Title(self, value: str) -> None: ...
	@property
	def Icon(self) -> Optional[ImageSource]: ...
	@Icon.setter
	def Icon(self, value: Optional[ImageSource]) -> None: ...
	@property
	def WindowState(self) -> WindowState: ...
	@WindowState.setter
	def WindowState(self, value: WindowState) -> None: ...
	@property
	def WindowStyle(self) -> WindowStyle: ...
	@WindowStyle.setter
	def WindowStyle(self, value: WindowStyle) -> None: ...
	def Show(self) -> None: ...
	def Hide(self) -> None: ...
	def Close(self) -> None: ...
	@property
	def Top(self) -> float: ...
	@Top.setter
	def Top(self, value: float) -> None: ...
	@property
	def Left(self) -> float: ...
	@Left.setter
	def Left(self, value: float) -> None: ...
	@property
	def ResizeMode(self) -> ResizeMode: ...
	@ResizeMode.setter
	def ResizeMode(self, value: ResizeMode) -> None: ...
