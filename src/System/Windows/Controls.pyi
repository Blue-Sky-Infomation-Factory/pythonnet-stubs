"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls
"""

from typing import Optional

from System import Object
from System.Collections import ICollection, IEnumerable, IList
from System.Windows import FrameworkContentElement, FrameworkElement, UIElement
from System.Windows.Markup import IAddChild


class Control(FrameworkElement):
    # incomplete
	pass

class ContentControl(Control, IAddChild):
	# incomplete
	@property
	def Content(self) -> Optional[Object]: ...
	@Content.setter
	def Content(self, value: Optional[Object]) -> None: ...

class UIElementCollection(Object, ICollection[UIElement]):
	# incomplete
	pass

class Panel(FrameworkElement, IAddChild):
	# incomplete
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
	ICollection[ColumnDefinition]
):
	@property
	def ColumnDefinitions(self) -> ColumnDefinitionCollection:...
	@ColumnDefinitions.setter
	def ColumnDefinitions(self, value: ColumnDefinitionCollection) -> None:...

class Grid(Panel):
    # incomplete
	pass