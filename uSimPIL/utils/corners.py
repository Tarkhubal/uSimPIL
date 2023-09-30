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

def circle_from_center(image: PILImage.Image, radius: int):
    """
    Create a circle from the center of an image

    Attributes
    ----------
     - radius (int) : The radius of the circle
    """
    if radius <= 0:
        radius = min(image.size[0] // 2, image.size[1] // 2)
    
    width, height = image.size
    position = (width // 2, height // 2)  # center of the image

    circle = PILImage.new('L', (width, height), 0)
    draw = PILImageDraw.Draw(circle)
    draw.ellipse((position[0] - radius, position[1] - radius, position[0] + radius, position[1] + radius), fill=255)

    result = PILImage.new('RGBA', (width, height))
    result.paste(image, mask=circle)
    return result
