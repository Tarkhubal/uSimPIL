from typing import Union, Tuple, List, Dict, Any, Optional, Literal

from ..operations import *
from .image import Image



class Text:
    def __init__(self, text: Union[str, "Text"] = "", operations: List[Operation] = []):
        if isinstance(text, Text):
            self.text = text.text
            self.operations = text.operations
        elif isinstance(text, str):
            self.text = text
            self.operations = operations
        else:
            raise TypeError(f'"{type(text)}" is not a valid text type. Must be a string or uSimPIL.Text')

        self.font = Font(self.operations, self)
        self.color = Color()

        self.position = (0, 0) # (x_pos, y_pos)
    
    def new(text: str, font: str = "Arial", font_weight: int = 200, position: Tuple[Union[int, str]] = (0, 0)):
        text = Text(text=text)
        text.font.custom(font)
        text.font.weight.custom(font_weight)
        text.position = position
        return text

    def center(self):
        self.pos = ("center", "center")
    
    def merge(self, item: Union["Font", "FontWeight"]):
        if isinstance(item, Font):
            self.operations += item.operations
            self.font = item
        elif isinstance(item, FontWeight):
            self.operations += item.operations
            try:
                if self.font is None:
                    self.font = Font(self.operations, self)
            except AttributeError:
                self.font = Font(self.operations, self)
            self.font.weight = item
        else:
            raise TypeError(f'"{type(item)}" is not a valid merge type. Must be a uSimPIL.Font or uSimPIL.FontWeight')

        return self
    
    def y_pos(self, pos: Optional[Union[str, int]]):
        """Return the y_pos if no "pos" is provided else set y position to "pos"
        
        pos="center" to center it on y axis
        """
        if pos is None:
            return self.position[1]
        else:
            self.position = (self.position[0], pos)
    
    def x_pos(self, pos: Optional[Union[str, int]]):
        """Return the x_pos if no "pos" is provided else set x position to "pos"
        
        pos="center" to center it on x axis
        """
        if pos is None:
            return self.position[0]
        else:
            self.position = (pos, self.position[1])

    def _h_align(self):
        self.position = ("center", self.position[1])
    
    def _v_align(self):
        self.position = (self.position[0], "center")
    
    def vertical_align(self):
        self._v_align()
        
    def valign(self):
        self._v_align()
    
    def horizontal_align(self):
        self._h_align()
    
    def halign(self):
        self._h_align()

    def __repr__(self):
        return f"<Text text={self.text} operations={self.operations}>"


class Font(OperationsSystem):
    def __init__(self, operations: List[Operation] = [], text: Text = None):
        self.text = text
        self.operations = operations
        self.font = "Arial"
        self.weight = FontWeight()

    @property
    def poppins(self):
        self.font = "Poppins"
        return self
    
    @property
    def calibri(self):
        self.font = "Calibri"
        return self
    
    def from_path(path: str):
        if not path.endswith(".woff"):
            raise ValueError("path must be a font file")
        
        font = Font()
        font.font = path
        return font
    
    def custom(self, font: str):
        self.font = font
        return self


class Color:
    def __init__(self):
        self.colors = {
            "black": "#000000",
            "red": "#ff0000",
            "white": "#ffffff",
            "blue": "#0000ff",
            "green": "#00ff00"
        }

        self.choosed_color = self.colors["black"]
    
    def _set_color(self, key: str, value: str):
        if not isinstance(key, str):
            raise TypeError(f'"key" element must be a string, not {type(key)}')
        if not isinstance(value, str):
            raise TypeError(f'the color element must be a string, not {type(value)}')
        if not value.startswith("#") or len(value) < 7 or len(value) > 9:
            raise ValueError(f'the color element must be a hexadecimal code, like this : "#RRGGBBTT" (r = red, g = green, b = blue, t = transparency (ff = fully visible) (optional)). It must starts with "#"')


        self.colors["key"] = value

            

    @property
    def red(self):
        self.choosed_color = self.colors["red"]
    
    @red.setter
    def red(self, value: str):
        self._set_color("red", )
    


# CustomColor with a hexadecimal in init ?
# Add a system to generate properties based on the dict colors






class FontWeight(OperationsSystem):
    def __init__(self, operations: List[Operation] = [], font: Font = None):
        self.font = font
        self.operations = operations
        self.weight = 400
    
    def regular(self):
        self.weight = 300
        
        return self
    
    def bold(self):
        self.weight = 600
        return self
    
    def ultra_bold(self):
        self.weight = 900
        return self

    def thin(self):
        self.weight = 200
        return self
    
    def custom(self, weight: int):
        self.weight = weight
        return self
