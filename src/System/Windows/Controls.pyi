"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls
"""

from typing import Optional

from System import Object
from System.Collections import ICollection, IEnumerable, IList
from System.Collections.Generic import ICollection as g_ICollection
from System.Windows import FrameworkContentElement, FrameworkElement, UIElement
from System.Windows.Markup import IAddChild
from System.Windows.Media import Brush


class Control(FrameworkElement):
    # incomplete
	pass

class ContentControl(Control, IAddChild):
	# incomplete
	@property
	def Content(self) -> Optional[Object]: ...
	@Content.setter
	def Content(self, value: Optional[Object]) -> None: ...

class UIElementCollection(Object, ICollection, IEnumerable, IList):
	# incomplete
	pass

class Panel(FrameworkElement, IAddChild):
	# incomplete
	@property
	def Background(self) -> Optional[Brush]: ...
	@Background.setter
	def Background(self, value: Optional[Brush]) -> None: ...
	@property
	def Children(self) -> UIElementCollection: ...

class DockPanel(Panel):
    # incomplete
	def __init__(self):
		self.LastChildFill: bool

class Canvas(Panel):
    # incomplete
	@classmethod
	def SetLeft(cls, element: UIElement, length: float) -> None: ...
	@classmethod
	def SetRight(cls, element: UIElement, length: float) -> None: ...
	@classmethod
	def SetTop(cls, element: UIElement, length: float) -> None: ...
	@classmethod
	def SetBottom(cls, element: UIElement, length: float) -> None: ...

class DefinitionBase(FrameworkContentElement):
    # incomplete
	pass

class ColumnDefinition(DefinitionBase):
    # incomplete
	pass

class ColumnDefinitionCollection(
	Object,
	g_ICollection[ColumnDefinition]
):
    # incomplete
	pass

class RowDefinition(DefinitionBase):
    # incomplete
	pass

class RowDefinitionCollection(
	Object,
	g_ICollection[RowDefinition]
):
    # incomplete
	pass

class Grid(Panel):
    # incomplete
	@property
	def RowDefinitions(self) -> RowDefinitionCollection:...
	@RowDefinitions.setter
	def RowDefinitions(self, value: RowDefinitionCollection) -> None:...
	@property
	def ColumnDefinitions(self) -> ColumnDefinitionCollection:...
	@ColumnDefinitions.setter
	def ColumnDefinitions(self, value: ColumnDefinitionCollection) -> None:...