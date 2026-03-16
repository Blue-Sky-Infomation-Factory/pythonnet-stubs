from typing import Final

from System import IEquatable, IFormattable, ValueType
from System.Windows import DependencyObject
from System.Windows.Media.Animation import Animatable


class Visual(DependencyObject):
	#incomplete
	pass

class Brush(Animatable, IFormattable):
	#incomplete
	pass

class Color(ValueType, IEquatable[Color], IFormattable):
	#incomplete
	pass

class SolidColorBrush(Brush):
	#incomplete
	def __init__(self, color: Color = ...): ...
	@property
	def Color(self) -> Color: ...
	@Color.setter
	def Color(self, value: Color) -> None: ...

class __Brushes_static(type):
	AliceBlue: Final[SolidColorBrush]  # FFF0F8FF
	AntiqueWhite: Final[SolidColorBrush]  # FFFAEBD7
	Aqua: Final[SolidColorBrush]  # FF00FFFF
	Aquamarine: Final[SolidColorBrush]  # FF7FFFD4
	Azure: Final[SolidColorBrush]  # FFF0FFFF
	Beige: Final[SolidColorBrush]  # FFF5F5DC
	Bisque: Final[SolidColorBrush]  # FFFFE4C4
	Black: Final[SolidColorBrush]  # FF000000
	BlanchedAlmond: Final[SolidColorBrush]  # FFFFEBCD
	Blue: Final[SolidColorBrush]  # FF0000FF
	BlueViolet: Final[SolidColorBrush]  # FF8A2BE2
	Brown: Final[SolidColorBrush]  # FFA52A2A
	BurlyWood: Final[SolidColorBrush]  # FFDEB887
	CadetBlue: Final[SolidColorBrush]  # FF5F9EA0
	Chartreuse: Final[SolidColorBrush]  # FF7FFF00
	Chocolate: Final[SolidColorBrush]  # FFD2691E
	Coral: Final[SolidColorBrush]  # FFFF7F50
	CornflowerBlue: Final[SolidColorBrush]  # FF6495ED
	Cornsilk: Final[SolidColorBrush]  # FFFFF8DC
	Crimson: Final[SolidColorBrush]  # FFDC143C
	Cyan: Final[SolidColorBrush]  # FF00FFFF
	DarkBlue: Final[SolidColorBrush]  # FF00008B
	DarkCyan: Final[SolidColorBrush]  # FF008B8B
	DarkGoldenrod: Final[SolidColorBrush]  # FFB8860B
	DarkGray: Final[SolidColorBrush]  # FFA9A9A9
	DarkGreen: Final[SolidColorBrush]  # FF006400
	DarkKhaki: Final[SolidColorBrush]  # FFBDB76B
	DarkMagenta: Final[SolidColorBrush]  # FF8B008B
	DarkOliveGreen: Final[SolidColorBrush]  # FF556B2F
	DarkOrange: Final[SolidColorBrush]  # FFFF8C00
	DarkOrchid: Final[SolidColorBrush]  # FF9932CC
	DarkRed: Final[SolidColorBrush]  # FF8B0000
	DarkSalmon: Final[SolidColorBrush]  # FFE9967A
	DarkSeaGreen: Final[SolidColorBrush]  # FF8FBC8F
	DarkSlateBlue: Final[SolidColorBrush]  # FF483D8B
	DarkSlateGray: Final[SolidColorBrush]  # FF2F4F4F
	DarkTurquoise: Final[SolidColorBrush]  # FF00CED1
	DarkViolet: Final[SolidColorBrush]  # FF9400D3
	DeepPink: Final[SolidColorBrush]  # FFFF1493
	DeepSkyBlue: Final[SolidColorBrush]  # FF00BFFF
	DimGray: Final[SolidColorBrush]  # FF696969
	DodgerBlue: Final[SolidColorBrush]  # FF1E90FF
	Firebrick: Final[SolidColorBrush]  # FFB22222
	FloralWhite: Final[SolidColorBrush]  # FFFFFAF0
	ForestGreen: Final[SolidColorBrush]  # FF228B22
	Fuchsia: Final[SolidColorBrush]  # FFFF00FF
	Gainsboro: Final[SolidColorBrush]  # FFDCDCDC
	GhostWhite: Final[SolidColorBrush]  # FFF8F8FF
	Gold: Final[SolidColorBrush]  # FFFFD700
	Goldenrod: Final[SolidColorBrush]  # FFDAA520
	Gray: Final[SolidColorBrush]  # FF808080
	Green: Final[SolidColorBrush]  # FF008000
	GreenYellow: Final[SolidColorBrush]  # FFADFF2F
	Honeydew: Final[SolidColorBrush]  # FFF0FFF0
	HotPink: Final[SolidColorBrush]  # FFFF69B4
	IndianRed: Final[SolidColorBrush]  # FFCD5C5C
	Indigo: Final[SolidColorBrush]  # FF4B0082
	Ivory: Final[SolidColorBrush]  # FFFFFFF0
	Khaki: Final[SolidColorBrush]  # FFF0E68C
	Lavender: Final[SolidColorBrush]  # FFE6E6FA
	LavenderBlush: Final[SolidColorBrush]  # FFFFF0F5
	LawnGreen: Final[SolidColorBrush]  # FF7CFC00
	LemonChiffon: Final[SolidColorBrush]  # FFFFFACD
	LightBlue: Final[SolidColorBrush]  # FFADD8E6
	LightCoral: Final[SolidColorBrush]  # FFF08080
	LightCyan: Final[SolidColorBrush]  # FFE0FFFF
	LightGoldenrodYellow: Final[SolidColorBrush]  # FFFAFAD2
	LightGray: Final[SolidColorBrush]  # FFD3D3D3
	LightGreen: Final[SolidColorBrush]  # FF90EE90
	LightPink: Final[SolidColorBrush]  # FFFFB6C1
	LightSalmon: Final[SolidColorBrush]  # FFFFA07A
	LightSeaGreen: Final[SolidColorBrush]  # FF20B2AA
	LightSkyBlue: Final[SolidColorBrush]  # FF87CEFA
	LightSlateGray: Final[SolidColorBrush]  # FF778899
	LightSteelBlue: Final[SolidColorBrush]  # FFB0C4DE
	LightYellow: Final[SolidColorBrush]  # FFFFFFE0
	Lime: Final[SolidColorBrush]  # FF00FF00
	LimeGreen: Final[SolidColorBrush]  # FF32CD32
	Linen: Final[SolidColorBrush]  # FFFAF0E6
	Magenta: Final[SolidColorBrush]  # FFFF00FF
	Maroon: Final[SolidColorBrush]  # FF800000
	MediumAquamarine: Final[SolidColorBrush]  # FF66CDAA
	MediumBlue: Final[SolidColorBrush]  # FF0000CD
	MediumOrchid: Final[SolidColorBrush]  # FFBA55D3
	MediumPurple: Final[SolidColorBrush]  # FF9370DB
	MediumSeaGreen: Final[SolidColorBrush]  # FF3CB371
	MediumSlateBlue: Final[SolidColorBrush]  # FF7B68EE
	MediumSpringGreen: Final[SolidColorBrush]  # FF00FA9A
	MediumTurquoise: Final[SolidColorBrush]  # FF48D1CC
	MediumVioletRed: Final[SolidColorBrush]  # FFC71585
	MidnightBlue: Final[SolidColorBrush]  # FF191970
	MintCream: Final[SolidColorBrush]  # FFF5FFFA
	MistyRose: Final[SolidColorBrush]  # FFFFE4E1
	Moccasin: Final[SolidColorBrush]  # FFFFE4B5
	NavajoWhite: Final[SolidColorBrush]  # FFFFDEAD
	Navy: Final[SolidColorBrush]  # FF000080
	OldLace: Final[SolidColorBrush]  # FFFDF5E6
	Olive: Final[SolidColorBrush]  # FF808000
	OliveDrab: Final[SolidColorBrush]  # FF6B8E23
	Orange: Final[SolidColorBrush]  # FFFFA500
	OrangeRed: Final[SolidColorBrush]  # FFFF4500
	Orchid: Final[SolidColorBrush]  # FFDA70D6
	PaleGoldenrod: Final[SolidColorBrush]  # FFEEE8AA
	PaleGreen: Final[SolidColorBrush]  # FF98FB98
	PaleTurquoise: Final[SolidColorBrush]  # FFAFEEEE
	PaleVioletRed: Final[SolidColorBrush]  # FFDB7093
	PapayaWhip: Final[SolidColorBrush]  # FFFFEFD5
	PeachPuff: Final[SolidColorBrush]  # FFFFDAB9
	Peru: Final[SolidColorBrush]  # FFCD853F
	Pink: Final[SolidColorBrush]  # FFFFC0CB
	Plum: Final[SolidColorBrush]  # FFDDA0DD
	PowderBlue: Final[SolidColorBrush]  # FFB0E0E6
	Purple: Final[SolidColorBrush]  # FF800080
	Red: Final[SolidColorBrush]  # FFFF0000
	RosyBrown: Final[SolidColorBrush]  # FFBC8F8F
	RoyalBlue: Final[SolidColorBrush]  # FF4169E1
	SaddleBrown: Final[SolidColorBrush]  # FF8B4513
	Salmon: Final[SolidColorBrush]  # FFFA8072
	SandyBrown: Final[SolidColorBrush]  # FFF4A460
	SeaGreen: Final[SolidColorBrush]  # FF2E8B57
	SeaShell: Final[SolidColorBrush]  # FFFFF5EE
	Sienna: Final[SolidColorBrush]  # FFA0522D
	Silver: Final[SolidColorBrush]  # FFC0C0C0
	SkyBlue: Final[SolidColorBrush]  # FF87CEEB
	SlateBlue: Final[SolidColorBrush]  # FF6A5ACD
	SlateGray: Final[SolidColorBrush]  # FF708090
	Snow: Final[SolidColorBrush]  # FFFFFAFA
	SpringGreen: Final[SolidColorBrush]  # FF00FF7F
	SteelBlue: Final[SolidColorBrush]  # FF4682B4
	Tan: Final[SolidColorBrush]  # FFD2B48C
	Teal: Final[SolidColorBrush]  # FF008080
	Thistle: Final[SolidColorBrush]  # FFD8BFD8
	Tomato: Final[SolidColorBrush]  # FFFF6347
	Transparent: Final[SolidColorBrush]  # 00FFFFFF
	Turquoise: Final[SolidColorBrush]  # FF40E0D0
	Violet: Final[SolidColorBrush]  # FFEE82EE
	Wheat: Final[SolidColorBrush]  # FFF5DEB3
	White: Final[SolidColorBrush]  # FFFFFFFF
	WhiteSmoke: Final[SolidColorBrush]  # FFF5F5F5
	Yellow: Final[SolidColorBrush]  # FFFFFF00
	YellowGreen: Final[SolidColorBrush]  # FF9ACD32
class Brushes(ValueType, metaclass = __Brushes_static):...