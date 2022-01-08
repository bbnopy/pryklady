def increaseRed(picture):
    for p in getPixels(picture):
        value=getRed(p)
        setRed(p,value*1.2)
