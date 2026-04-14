"""
https://learn.microsoft.com/en-us/dotnet/api/Microsoft.Win32
"""

from abc import ABC, abstractmethod
from typing import overload

from System import Array, Object
from System.Windows import Window

class CommonDialog(Object, ABC):
	# incomplete
	@abstractmethod
	@overload
	def ShowDialog(self) -> bool: ...
	@abstractmethod
	@overload
	def ShowDialog(self, owner: Window) -> bool: ...

class CommonItemDialog(CommonDialog, ABC):
	# incomplete
	pass

class FileDialog(CommonItemDialog, ABC):
	# incomplete
	@property
	def FileName(self) -> str: ...
	@FileName.setter
	def FileName(self, value: str) -> None: ...
	@property
	def FileNames(self) -> Array[str]: ...

class OpenFileDialog(FileDialog):
	# incomplete
	@overload
	def ShowDialog(self) -> bool: ...
	@overload
	def ShowDialog(self, owner: Window) -> bool: ...
	@property
	def Multiselect(self) -> bool: ...
	@Multiselect.setter
	def Multiselect(self, value: bool) -> None: ...