from typing import Tuple, Union
from PIL import (
    Image as PILImage,
    ImageDraw as PILImageDraw,
    ImageFont
)


def add_text(image: PILImage.Image,
             text: str,
             position: Union[Tuple[int, int], Tuple[str, str], Tuple[int, str], Tuple[str, int]],
             font: str = None,
             color: Tuple[int, int, int, int] = (0, 0, 0, 255),
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
    if font is None:
        font = ImageFont.load_default(size=size)
    else:
        font = ImageFont.truetype(font, size=size)

    position = list(position)
    if position[0] == "center":
        W, H = image.size
        draw = PILImageDraw.Draw(PILImage.new('RGB', image.size))
        _, _, w, h = draw.textbbox((0, 0), text, font=font)
        position[0] = (W - w) / 2
    
    if position[1] == "center":
        W, H = image.size
        draw = PILImageDraw.Draw(PILImage.new('RGB', image.size))
        _, _, w, h = draw.textbbox((0, 0), text, font=font)
        position[1] = (H - h) / 2

    draw = PILImageDraw.Draw(image)
    draw.text(position, text, font=font, fill=color)
    return image