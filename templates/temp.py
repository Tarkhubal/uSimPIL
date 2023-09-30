...

# class Image:
#     def __init__(self, image: str):
#         """Load an image
        
#         Attributes
#         ----------
#          - image (str) : path to the image
#         """
#         self.image = PILImage.open(image)
#         self.corners = Corners(self)
    
#     @property
#     def view(self):
#         self.image.show()
    
#     def save(self, path: str):
#         """Save the image
        
#         Attributes
#         ----------
#          - path (str) : path to save the image
#         """
#         self.image.save(path)


# class Corners:
#     def __init__(self, image: Image):
#         self.image = image

#     def roundall(self, radius: int):
#         """
#         Round the corners of an image

#         Attributes
#         ----------
#          - radius (int) : The radius to use for the rounded corners
#         """
#         # Create a mask
#         mask = PILImage.new('L', self.image.image.size, 0)
#         draw = PILImageDraw.Draw(mask)
        
#         width, height = self.image.image.size
        
#         # Draw rounded corners on the mask image
#         draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=255)
#         draw.rectangle((radius, 0, width - radius, height), fill=255)
#         draw.rectangle((0, radius, width, height - radius), fill=255)
#         draw.pieslice((width - radius * 2, 0, width, radius * 2), 270, 360, fill=255)
#         draw.pieslice((0, height - radius * 2, radius * 2, height), 90, 180, fill=255)
#         draw.pieslice((width - radius * 2, height - radius * 2, width, height), 0, 90, fill=255)
        
#         # Apply the mask to the image
#         self.image.image.putalpha(mask)
#         self.image.image.show()
#         return self.image
    
#     def round(self, radius: int, corner: int):
#         """
#         Round a corner of an image

#         Attributes
#         ----------
#          - radius (int) : The radius to use for the rounded corners
#          - corners (tuple) : A tuple of integers specifying which corners to round.
#                             0 = top-left, 1 = top-right, 2 = bottom-right, 3 = bottom-left
#                             Example: (0, 2) to round top-left and bottom-right corners.
#         """
#         # Create a mask
#         mask = PILImage.new('L', self.image.image.size, 0)
#         draw = PILImageDraw.Draw(mask)
        
#         width, height = self.image.image.size
        
#         # Draw rounded corners based on the specified corners
#         if corner == 0:
#             draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=255)
#             draw.rectangle((radius, 0, width, height), fill=255)
#             draw.rectangle((0, radius, width, height), fill=255)
#         elif corner == 1:
#             draw.pieslice((width - radius * 2, 0, width, radius * 2), 270, 360, fill=255)
#             draw.rectangle((0, 0, width - radius, height), fill=255)
#             draw.rectangle((0, radius, width, height), fill=255)
#         elif corner == 2:
#             draw.pieslice((width - radius * 2, height - radius * 2, width, height), 0, 90, fill=255)
#             draw.rectangle((0, 0, width, height - radius), fill=255)
#             draw.rectangle((0, 0, width - radius, height), fill=255)
#         elif corner == 3:
#             draw.pieslice((0, height - radius * 2, radius * 2, height), 90, 180, fill=255)
#             draw.rectangle((radius, 0, width, height), fill=255)
#             draw.rectangle((0, 0, width, height - radius), fill=255)
        
#         # Apply the mask to the image
#         self.image.image.putalpha(mask)
#         self.image.image.show()
#         return self.image