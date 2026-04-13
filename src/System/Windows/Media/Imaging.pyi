from abc import ABC

from System import Uri
from System.Net.Cache import RequestCachePolicy
from System.Windows.Media import ImageSource


class BitmapSource(ImageSource, ABC):
	#incomplete
	pass

class BitmapImage(BitmapSource):
	#incomplete
	def __init__(self, uriSource: Uri = ..., uriCachePolicy: RequestCachePolicy = ...): ...