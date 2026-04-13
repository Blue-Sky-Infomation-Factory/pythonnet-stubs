"""
https://learn.microsoft.com/en-us/dotnet/api/system.windows.interop
"""

from System import IDisposable, IKeyboardInputSink, IWin32Window
from System.Windows import FrameworkElement


class HwndHost(FrameworkElement, IDisposable, IKeyboardInputSink, IWin32Window):
	#incomplete
	pass