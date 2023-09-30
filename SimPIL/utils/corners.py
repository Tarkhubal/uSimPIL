from PIL import (
    Image as PILImage,
    ImageDraw as PILImageDraw
)

def round_corners(image: PILImage.Image, radius, corners=[True, True, True, True]):
    """
    Round the corners of an image.
    
    Attributes
    ----------
     - corners: A list of four booleans indicating whether to round the top-left, top-right, bottom-left and bottom-right corners respectively.
    """
    width, height = image.size
    circle = PILImage.new('L', (radius * 2, radius * 2), 0)
    draw = PILImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)

    alpha = PILImage.new('L', image.size, 255)
    w, h = circle.size
    if corners[0]:
        alpha.paste(circle.crop((0, 0, w//2, h//2)), (0, 0)) # top left
    if corners[1]:
        alpha.paste(circle.crop((w//2, 0, w, h//2)), (width - radius, 0)) # top right
    if corners[2]:
        alpha.paste(circle.crop((0, h//2, w//2, h)), (0, height - radius)) # bottom left
    if corners[3]:
        alpha.paste(circle.crop((w//2, h//2, w, h)), (width - radius, height - radius)) # bottom right

    image.putalpha(alpha)
    return image
