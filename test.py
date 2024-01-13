import uSimPIL

# img = uSimPIL.open("before.png")
# img.corners.roundall(100)


# # is equivalent to this program:
# img = uSimPIL.open("before.png")

# corners = uSimPIL.Corners()
# corners.roundall(50)

# img = uSimPIL.merge(img, corners)

# img.create()
# img.view()

img = uSimPIL.open("before.png")
text = uSimPIL.Text("Hello world !")

font = uSimPIL.Font()
font.size.custom(90)

text.merge(font)
text.font.weight.bold()
text.center()

print(text)
img = uSimPIL.merge(img, text)
img.corners.roundall(50)

# Add another text
text2 = uSimPIL.Text("Oh hayo !")
text2.font.size.custom(90)
img.merge(text2)

print(img.operations)
img.create()
img.view()
