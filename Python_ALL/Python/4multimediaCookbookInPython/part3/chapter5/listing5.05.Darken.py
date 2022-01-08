def darken(picture):
    for px in getPixels(picture):
        color = getColor(px)
        makeDarker(color)
        setColor(px,color)
