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

text = uSimPIL.Text("Bonjour")

text.font.poppins

print(text.font.font)

text.font.weight.bold()

print(text.font.weight.weight)

font = uSimPIL.Font()
font.calibri
font.weight.ultra_bold()

print(font.font)
print(font.weight.weight)

text = text.merge(font)

print(text.font.font)



# img.create()
# img.view()

