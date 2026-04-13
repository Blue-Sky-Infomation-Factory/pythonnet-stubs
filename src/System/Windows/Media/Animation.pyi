"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.animation
"""

from abc import ABC

from System.Windows import Freezable


class IAnimatable(ABC):
	#incomplete
	pass

class Animatable(Freezable, IAnimatable):
	#incomplete
	pass