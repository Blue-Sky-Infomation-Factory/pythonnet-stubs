from System import EventArgs, MarshalByRefObject


class Component(MarshalByRefObject):
	# incomplete
	pass

class CancelEventArgs(EventArgs):
	def __init__(self, cancel: bool = False):
		self.Cancel: bool