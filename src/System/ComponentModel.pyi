"""
https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel
"""

from abc import ABC

from System import EventArgs, MarshalByRefObject


class Component(MarshalByRefObject):
	# incomplete
	pass

class CancelEventArgs(EventArgs):
	def __init__(self, cancel: bool = False):
		self.Cancel: bool

class ISupportInitialize(ABC):
	#incomplete
	pass