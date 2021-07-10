def mirrorVertical(source):
    for y in range(1, getHeight(source)):
        for x in range((getWidth(source)/2)+1, getWidth(source)):
            p = getPixel(source,x,y)
            p2 = getPixel(source,(( getWidth(source)/2)- (x-( getWidth(source)/2))),y)
            setColor(p,makeColor( getRed(p2), getGreen(p2), getBlue(p2)))
