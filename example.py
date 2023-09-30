import uSimPIL


if __name__ == "__main__":
    img = uSimPIL.open("img.png")
    
    img.corners.roundall(50)
    
    img.create()
    img.save("img2.png")
    img.view()