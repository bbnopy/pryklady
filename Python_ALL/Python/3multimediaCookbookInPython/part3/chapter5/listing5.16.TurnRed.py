def turnedRed():
    brown = makeColor(57,16,8)
    file = "/Users/guszdial/mediasources/barbara.jpg"
    picture = makePicture(file)
    for px in getPixels(picture):
        color = getColor(px)
        if distance(color,brown) < 50.0:
            redness = int(getRed(px) * 1.5)
            bluenness = getBlue(px)
            greenless = getGreen(px)
            setColor(px,makeColor(redness,blueness,greenless))
    show(picture)
    return(picture)
