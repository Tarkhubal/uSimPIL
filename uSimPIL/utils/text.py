from PIL import (
    Image as PILImage,
    ImageDraw as PILImageDraw,
    ImageFont
)
from typing import Union, Tuple, List, Dict, Any

import os

def add_text(image: PILImage.Image,
             text: str,
             position: Union[Tuple[int, int], Tuple[str, str], Tuple[int, str], Tuple[str, int]],
             font: str,
             color: Tuple[int, int, int, int],
             weight: int = 400,
             size: int = 18
             ):
    """
    Add text to an image

    Attributes
    ----------
     - text (str) : The text to add to the image
     - position (Tuple[int, int]) : The position of the text
     - font (str) : The font to use
     - color (Tuple[int, int, int, int]) : The color of the text
    """
    img_x, img_y = image.size
    position = list(position)
    if position[0] == "center":
        position[0] = img_x // 2
    if position[1] == "center":
        position[1] = img_y // 2
    
    font = ImageFont.load_default(size=size)
    draw = PILImageDraw.Draw(image)
    draw.text(position, text, font=font, fill=color)
    return image