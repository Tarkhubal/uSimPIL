import uSimPIL


if __name__ == "__main__":
    # This program:
    img = uSimPIL.open("before.png")
    img.corners.roundall(50)
    img.create()
    img.view()
    
    
    # is equivalent to this program:
    img = uSimPIL.open("before.png")
    
    corners = uSimPIL.Corners()
    corners.roundall(50)
    
    img = uSimPIL.merge(img, corners)
    
    img.create()
    img.view()
    
    