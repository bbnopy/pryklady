def turnRedInRange():
    brown = makeColor(57,46,8)
    file = "/Users/guzdial/mediasources/barbara.jpg"
    picture = makePicture(file)
    for x in range(70,168):
        for y in range(56,190):
            px = getPixel(picture,x,y)
        color = getColor(px)
        if distance(color,brown) < 50.0:
            redness = int(getRed(px) * 1.5)
            blueness = getBlue(px)
            greenless = getGreen(px)
            setColor(px,makeColor(redness,blueness,greenless))
    show(picture)
    return(pixture)
