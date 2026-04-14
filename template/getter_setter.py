from typing import List

from pyperclip import copy

def getter(name: str, type: str = "Any"):
	return f"\t@property\n\tdef {name}(self) -> {type}:...\n"
def setter(name: str, type: str = "Any"):
	return f"\t@{name}.setter\n\tdef {name}(self, value: {type}) -> None:...\n"
def pair(name: str, type: str = "Any"):
	return getter(name, type) + setter(name, type)

def gen_get(name: str, type: str = "Any"):
	text = getter(name, type)
	copy(text)
	return text

def gen_pair(name: str, type: str = "Any"):
	text = pair(name, type)
	copy(text)
	return text

def batch_gen(list: List[List[str]]):
	text = "".join([pair(item[0], item[1]) for item in list])
	copy(text)
	return text