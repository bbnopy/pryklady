def lighten(picture):
    for x in range(1,getWidth(picture)):
        for y in range(1,getHeight(picture)):
            px = getPixel(picture,x,y)
            color = getColor(px)
            makeLighter(color)
            setColor(px,color)
