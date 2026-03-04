from abc import ABC
from typing import overload

from System.ComponentModel import ISupportInitialize
from System.Windows.Controls import ContentControl
from System.Windows.Markup import IQueryAmbient
from System.Windows.Media import Visual
from System.Windows.Media.Animation import IAnimatable
from System.Windows.Threading import DispatcherObject


class Application(DispatcherObject, IQueryAmbient):
	@overload
	def Run(self) -> int:...
	@overload
	def Run(self, window: Window) -> int:...

class DependencyObject(DispatcherObject):
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
	pass

class Window(ContentControl):
	#incomplete
	pass