import uSimPIL


if __name__ == "__main__":
    img = uSimPIL.open("before.png")
    
    img.corners.roundall(50)
    
    img.create()
    img.save("after.png")
    img.view()