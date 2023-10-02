from typing import Union, Tuple, List, Dict, Any

from ..operations import *

from .image import Image



class Text:
    def __init__(self, text: str = "", operations: List[Operation] = []):
        self.text = ""
        self.operations = operations

        self.font = Font()
        self.color = Color()

        self.pos = (0, 0) # (x_pos, y_pos)
    
    def center(self):
        self.pos = ("center", "center")
    
    def y_pos(self, pos: Optional[Union[str, int]]):
        """Return the y_pos if no "pos" is provided else set y position to "pos"
        
        pos="center" to center it on y axis
        """
        if pos is None:
            return self.pos[1]
        else:
            self.pos = (self.pos[0], pos)
    
    def x_pos(self, pos: Optional[Union[str, int]]):
        """Return the x_pos if no "pos" is provided else set x position to "pos"
        
        pos="center" to center it on x axis
        """
        if pos is None:
            return self.pos[0]
        else:
            self.pos = (pos, self.pos[1])

    def _h_align(self):
        self.pos = ("center", self.pos[1])
    
    def _v_align(self):
        self.pos = (self.pos[0], "center")
    
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


class Font:
    def __init__(self):
        self.font = "Arial"
        self.weight = FontWeight()

    @property
    def poppins(self):
        self.font = "Poppins"
    
    @property
    def calibri(self):
        self.font = "Calibri"


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






class FontWeight:
    def __init__(self):
        self.weight = 300
    
    def regular(self):
        self.weight = 300
    
    def bold(self):
        self.weight = 600
    
    def ultra_bold(self):
        self.weight = 900
    
    def fine(self):
        self.weight = 100

