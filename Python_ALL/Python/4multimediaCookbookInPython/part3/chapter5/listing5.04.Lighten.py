def lighten(picture):
    for px in getPixels(picture):
        color = getColor(px)
        makeLighter(color)
        setColor(px,color)
