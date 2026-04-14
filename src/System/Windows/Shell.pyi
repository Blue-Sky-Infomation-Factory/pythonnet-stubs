"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows.shell
"""

from typing import Self

from System.Windows import Freezable, Window


class WindowChrome(Freezable):
	# incomplete
	@classmethod
	def SetWindowChrome(cls, window: Window, chrome: Self) -> None: ...