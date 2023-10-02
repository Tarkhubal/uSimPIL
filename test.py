import uSimPIL

img = uSimPIL.open("before.png")
img.corners.roundall(100)



# # is equivalent to this program:
# img = uSimPIL.open("before.png")

# corners = uSimPIL.Corners()
# corners.roundall(50)

# img = uSimPIL.merge(img, corners)

# img.create()
# img.view()

text = Text("Bonjour")

text.font.weight



img.create()
img.view()