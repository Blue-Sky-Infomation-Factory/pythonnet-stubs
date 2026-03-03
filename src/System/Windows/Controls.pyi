from System.Windows import FrameworkElement
from System.Windows.Markup import IAddChild


class Control(FrameworkElement):
    # incomplete
	pass

class ContentControl(Control, IAddChild):
	# incomplete
	pass

class Panel(FrameworkElement, IAddChild):
	# incomplete
	pass

class DockPanel(Panel):
    # incomplete
	def __init__(self):
		self.LastChildFill: bool