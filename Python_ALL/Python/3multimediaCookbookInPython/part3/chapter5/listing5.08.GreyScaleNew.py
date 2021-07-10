def greyScaleNew(picture):
    for px in getPixels(picture):
        newRed = getRed(px) * 0.299
        newGreen = getGreen(px) * 0.587
        newBlue = getBlue(px) * 0.114
        luminance = newRed+newGreen+newBlu
        setColor(px,makeColor(luminance,luminance,luminance))
