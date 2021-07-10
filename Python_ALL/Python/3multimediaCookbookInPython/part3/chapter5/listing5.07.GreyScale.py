def greyScale(picture):
    for p in getPixels(picture):
        intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
        setColor(p,makeColor(intensity,intensity,intensity))
