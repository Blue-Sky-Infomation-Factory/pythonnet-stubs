from enum import Enum
from typing import Final, NoReturn, Union, Literal, overload
from System import ValueType

class KnownColor(Enum):
	ActiveBorder = 1
	ActiveCaption = 2
	ActiveCaptionText = 3
	AppWorkspace = 4
	Control = 5
	ControlDark = 6
	ControlDarkDark = 7
	ControlLight = 8
	ControlLightLight = 9
	ControlText = 10
	Desktop = 11
	GrayText = 12
	Highlight = 13
	HighlightText = 14
	HotTrack = 15
	InactiveBorder = 16
	InactiveCaption = 17
	InactiveCaptionText = 18
	Info = 19
	InfoText = 20
	Menu = 21
	MenuText = 22
	ScrollBar = 23
	Window = 24
	WindowFrame = 25
	WindowText = 26
	Transparent = 27
	AliceBlue = 28
	AntiqueWhite = 29
	Aqua = 30
	Aquamarine = 31
	Azure = 32
	Beige = 33
	Bisque = 34
	Black = 35
	BlanchedAlmond = 36
	Blue = 37
	BlueViolet = 38
	Brown = 39
	BurlyWood = 40
	CadetBlue = 41
	Chartreuse = 42
	Chocolate = 43
	Coral = 44
	CornflowerBlue = 45
	Cornsilk = 46
	Crimson = 47
	Cyan = 48
	DarkBlue = 49
	DarkCyan = 50
	DarkGoldenrod = 51
	DarkGray = 52
	DarkGreen = 53
	DarkKhaki = 54
	DarkMagenta = 55
	DarkOliveGreen = 56
	DarkOrange = 57
	DarkOrchid = 58
	DarkRed = 59
	DarkSalmon = 60
	DarkSeaGreen = 61
	DarkSlateBlue = 62
	DarkSlateGray = 63
	DarkTurquoise = 64
	DarkViolet = 65
	DeepPink = 66
	DeepSkyBlue = 67
	DimGray = 68
	DodgerBlue = 69
	Firebrick = 70
	FloralWhite = 71
	ForestGreen = 72
	Fuchsia = 73
	Gainsboro = 74
	GhostWhite = 75
	Gold = 76
	Goldenrod = 77
	Gray = 78
	Green = 79
	GreenYellow = 80
	Honeydew = 81
	HotPink = 82
	IndianRed = 83
	Indigo = 84
	Ivory = 85
	Khaki = 86
	Lavender = 87
	LavenderBlush = 88
	LawnGreen = 89
	LemonChiffon = 90
	LightBlue = 91
	LightCoral = 92
	LightCyan = 93
	LightGoldenrodYellow = 94
	LightGray = 95
	LightGreen = 96
	LightPink = 97
	LightSalmon = 98
	LightSeaGreen = 99
	LightSkyBlue = 100
	LightSlateGray = 101
	LightSteelBlue = 102
	LightYellow = 103
	Lime = 104
	LimeGreen = 105
	Linen = 106
	Magenta = 107
	Maroon = 108
	MediumAquamarine = 109
	MediumBlue = 110
	MediumOrchid = 111
	MediumPurple = 112
	MediumSeaGreen = 113
	MediumSlateBlue = 114
	MediumSpringGreen = 115
	MediumTurquoise = 116
	MediumVioletRed = 117
	MidnightBlue = 118
	MintCream = 119
	MistyRose = 120
	Moccasin = 121
	NavajoWhite = 122
	Navy = 123
	OldLace = 124
	Olive = 125
	OliveDrab = 126
	Orange = 127
	OrangeRed = 128
	Orchid = 129
	PaleGoldenrod = 130
	PaleGreen = 131
	PaleTurquoise = 132
	PaleVioletRed = 133
	PapayaWhip = 134
	PeachPuff = 135
	Peru = 136
	Pink = 137
	Plum = 138
	PowderBlue = 139
	Purple = 140
	Red = 141
	RosyBrown = 142
	RoyalBlue = 143
	SaddleBrown = 144
	Salmon = 145
	SandyBrown = 146
	SeaGreen = 147
	SeaShell = 148
	Sienna = 149
	Silver = 150
	SkyBlue = 151
	SlateBlue = 152
	SlateGray = 153
	Snow = 154
	SpringGreen = 155
	SteelBlue = 156
	Tan = 157
	Teal = 158
	Thistle = 159
	Tomato = 160
	Turquoise = 161
	Violet = 162
	Wheat = 163
	White = 164
	WhiteSmoke = 165
	Yellow = 166
	YellowGreen = 167
	ButtonFace = 168
	ButtonHighlight = 169
	ButtonShadow = 170
	GradientActiveCaption = 171
	GradientInactiveCaption = 172
	MenuBar = 173
	MenuHighlight = 174
	RebeccaPurple = 175

class __Color_static(type):
	Empty: Final[Color]
	AliceBlue: Final[Color]  #FFF0F8FF
	AntiqueWhite: Final[Color]  #FFFAEBD7
	Aqua: Final[Color]  #FF00FFFF
	Aquamarine: Final[Color]  #FF7FFFD4
	Azure: Final[Color]  #FFF0FFFF
	Beige: Final[Color]  #FFF5F5DC
	Bisque: Final[Color]  #FFFFE4C4
	Black: Final[Color]  #FF000000
	BlanchedAlmond: Final[Color]  #FFFFEBCD
	Blue: Final[Color]  #FF0000FF
	BlueViolet: Final[Color]  #FF8A2BE2
	Brown: Final[Color]  #FFA52A2A
	BurlyWood: Final[Color]  #FFDEB887
	CadetBlue: Final[Color]  #FF5F9EA0
	Chartreuse: Final[Color]  #FF7FFF00
	Chocolate: Final[Color]  #FFD2691E
	Coral: Final[Color]  #FFFF7F50
	CornflowerBlue: Final[Color]  #FF6495ED
	Cornsilk: Final[Color]  #FFFFF8DC
	Crimson: Final[Color]  #FFDC143C
	Cyan: Final[Color]  #FF00FFFF
	DarkBlue: Final[Color]  #FF00008B
	DarkCyan: Final[Color]  #FF008B8B
	DarkGoldenrod: Final[Color]  #FFB8860B
	DarkGray: Final[Color]  #FFA9A9A9
	DarkGreen: Final[Color]  #FF006400
	DarkKhaki: Final[Color]  #FFBDB76B
	DarkMagenta: Final[Color]  #FF8B008B
	DarkOliveGreen: Final[Color]  #FF556B2F
	DarkOrange: Final[Color]  #FFFF8C00
	DarkOrchid: Final[Color]  #FF9932CC
	DarkRed: Final[Color]  #FF8B0000
	DarkSalmon: Final[Color]  #FFE9967A
	DarkSeaGreen: Final[Color]  #FF8FBC8B
	DarkSlateBlue: Final[Color]  #FF483D8B
	DarkSlateGray: Final[Color]  #FF2F4F4F
	DarkTurquoise: Final[Color]  #FF00CED1
	DarkViolet: Final[Color]  #FF9400D3
	DeepPink: Final[Color]  #FFFF1493
	DeepSkyBlue: Final[Color]  #FF00BFFF
	DimGray: Final[Color]  #FF696969
	DodgerBlue: Final[Color]  #FF1E90FF
	Firebrick: Final[Color]  #FFB22222
	FloralWhite: Final[Color]  #FFFFFAF0
	ForestGreen: Final[Color]  #FF228B22
	Fuchsia: Final[Color]  #FFFF00FF
	Gainsboro: Final[Color]  #FFDCDCDC
	GhostWhite: Final[Color]  #FFF8F8FF
	Gold: Final[Color]  #FFFFD700
	Goldenrod: Final[Color]  #FFDAA520
	Gray: Final[Color]  #FF808080
	Green: Final[Color]  #FF008000
	GreenYellow: Final[Color]  #FFADFF2F
	Honeydew: Final[Color]  #FFF0FFF0
	HotPink: Final[Color]  #FFFF69B4
	IndianRed: Final[Color]  #FFCD5C5C
	Indigo: Final[Color]  #FF4B0082
	Ivory: Final[Color]  #FFFFFFF0
	Khaki: Final[Color]  #FFF0E68C
	Lavender: Final[Color]  #FFE6E6FA
	LavenderBlush: Final[Color]  #FFFFF0F5
	LawnGreen: Final[Color]  #FF7CFC00
	LemonChiffon: Final[Color]  #FFFFFACD
	LightBlue: Final[Color]  #FFADD8E6
	LightCoral: Final[Color]  #FFF08080
	LightCyan: Final[Color]  #FFE0FFFF
	LightGoldenrodYellow: Final[Color]  #FFFAFAD2
	LightGray: Final[Color]  #FFD3D3D3
	LightGreen: Final[Color]  #FF90EE90
	LightPink: Final[Color]  #FFFFB6C1
	LightSalmon: Final[Color]  #FFFFA07A
	LightSeaGreen: Final[Color]  #FF20B2AA
	LightSkyBlue: Final[Color]  #FF87CEFA
	LightSlateGray: Final[Color]  #FF778899
	LightSteelBlue: Final[Color]  #FFB0C4DE
	LightYellow: Final[Color]  #FFFFFFE0
	Lime: Final[Color]  #FF00FF00
	LimeGreen: Final[Color]  #FF32CD32
	Linen: Final[Color]  #FFFAF0E6
	Magenta: Final[Color]  #FFFF00FF
	Maroon: Final[Color]  #FF800000
	MediumAquamarine: Final[Color]  #FF66CDAA
	MediumBlue: Final[Color]  #FF0000CD
	MediumOrchid: Final[Color]  #FFBA55D3
	MediumPurple: Final[Color]  #FF9370DB
	MediumSeaGreen: Final[Color]  #FF3CB371
	MediumSlateBlue: Final[Color]  #FF7B68EE
	MediumSpringGreen: Final[Color]  #FF00FA9A
	MediumTurquoise: Final[Color]  #FF48D1CC
	MediumVioletRed: Final[Color]  #FFC71585
	MidnightBlue: Final[Color]  #FF191970
	MintCream: Final[Color]  #FFF5FFFA
	MistyRose: Final[Color]  #FFFFE4E1
	Moccasin: Final[Color]  #FFFFE4B5
	NavajoWhite: Final[Color]  #FFFFDEAD
	Navy: Final[Color]  #FF000080
	OldLace: Final[Color]  #FFFDF5E6
	Olive: Final[Color]  #FF808000
	OliveDrab: Final[Color]  #FF6B8E23
	Orange: Final[Color]  #FFFFA500
	OrangeRed: Final[Color]  #FFFF4500
	Orchid: Final[Color]  #FFDA70D6
	PaleGoldenrod: Final[Color]  #FFEEE8AA
	PaleGreen: Final[Color]  #FF98FB98
	PaleTurquoise: Final[Color]  #FFAFEEEE
	PaleVioletRed: Final[Color]  #FFDB7093
	PapayaWhip: Final[Color]  #FFFFEFD5
	PeachPuff: Final[Color]  #FFFFDAB9
	Peru: Final[Color]  #FFCD853F
	Pink: Final[Color]  #FFFFC0CB
	Plum: Final[Color]  #FFDDA0DD
	PowderBlue: Final[Color]  #FFB0E0E6
	Purple: Final[Color]  #FF800080
	RebeccaPurple: Final[Color]  #663399
	Red: Final[Color]  #FFFF0000
	RosyBrown: Final[Color]  #FFBC8F8F
	RoyalBlue: Final[Color]  #FF4169E1
	SaddleBrown: Final[Color]  #FF8B4513
	Salmon: Final[Color]  #FFFA8072
	SandyBrown: Final[Color]  #FFF4A460
	SeaGreen: Final[Color]  #FF2E8B57
	SeaShell: Final[Color]  #FFFFF5EE
	Sienna: Final[Color]  #FFA0522D
	Silver: Final[Color]  #FFC0C0C0
	SkyBlue: Final[Color]  #FF87CEEB
	SlateBlue: Final[Color]  #FF6A5ACD
	SlateGray: Final[Color]  #FF708090
	Snow: Final[Color]  #FFFFFAFA
	SpringGreen: Final[Color]  #FF00FF7F
	SteelBlue: Final[Color]  #FF4682B4
	Tan: Final[Color]  #FFD2B48C
	Teal: Final[Color]  #FF008080
	Thistle: Final[Color]  #FFD8BFD8
	Tomato: Final[Color]  #FFFF6347
	Transparent: Final[Color]  #system-defined color
	Turquoise: Final[Color]  #FF40E0D0
	Violet: Final[Color]  #FFEE82EE
	Wheat: Final[Color]  #FFF5DEB3
	White: Final[Color]  #FFFFFFFF
	WhiteSmoke: Final[Color]  #FFF5F5F5
	Yellow: Final[Color]  #FFFFFF00
	YellowGreen: Final[Color]  #FF9ACD32
class Color(ValueType, metaclass = __Color_static):
	def __init__(self) -> NoReturn:
		"""⚠ Protected"""
		self.A: Final[int]
		self.R: Final[int]
		self.G: Final[int]
		self.B: Final[int]
		self.IsEmpty: Final[bool]
		self.IsKnownColor: Final[bool]
		self.IsNamedColor: Final[bool]
		self.IsSystemColor: Final[bool]
		self.Name: Final[str]
	def Equals(self, object: object) -> bool: ...
	def GetHashCode(self) -> int: ...
	def ToString(self) -> str: ...
	def GetBrightness(self) -> float: ...
	def GetHue(self) -> float: ...
	def GetSaturation(self) -> float: ...
	def ToArgb(self) -> int: ...
	def ToKnownColor(self) -> Union[KnownColor, Literal[0]]: ...
	@staticmethod
	def FromArgb(alpha: int, red: int, green: int, blue: int) -> Color: ...
	@staticmethod
	def FromKnownColor(known_color: KnownColor) -> Color: ...
	@staticmethod
	def FromName(name: str) -> Color: ...

class Point(ValueType):
	# incomplete
	pass

class __Size_static(type):
	Empty: Final[Size]
class Size(ValueType, metaclass = __Size_static):
	@overload
	def __init__(self, width: int, height: int):
		self.Height: int
		self.Width: int
	@overload
	def __init__(self, point: Point): ...

	@property
	def IsEmpty(self) -> bool: ...

	@staticmethod
	def Add(s1: Size, s2: Size) -> Size: ...
	@staticmethod
	def Subtract(s1: Size, s2: Size) -> Size: ...
	
	def Equals(self, obj: Size) -> bool: ...
	def GetHashCode(self) -> int: ...
	def ToString(self) -> str: ...