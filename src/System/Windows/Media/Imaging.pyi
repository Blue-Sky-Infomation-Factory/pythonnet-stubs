"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows.media.imaging
"""

from abc import ABC

from System import Uri
from System.Net.Cache import RequestCachePolicy
from System.Windows.Media import ImageMetadata, ImageSource


class BitmapSource(ImageSource, ABC):
	#incomplete
	pass

class BitmapImage(BitmapSource):
	#incomplete
	def __init__(self, uriSource: Uri = ..., uriCachePolicy: RequestCachePolicy = ...): ...
	@property
	def Height(self) -> float: ...
	@property
	def Width(self) -> float: ...
	@property
	def Metadata(self) -> ImageMetadata: ...
