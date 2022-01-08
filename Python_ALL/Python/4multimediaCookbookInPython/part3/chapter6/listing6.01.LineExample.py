def lineExample():
    img = makePicture(pickAFile())
    new = verticalLines(img)
    new2 = horizontalLines(img)
    show(new2)

    return new2

def horizontalLines(src):
    for x in range(1,getHeight(src),5):
        for y in range(1,getWidth(src)):
            setColor(getPixel(src,y,x),black)
    return src

def verticalLines(src):
    for x in range(1,getWidth(src),5):
        for y in range(1,getHeight(src)):
            setColor(getPixel(src,x,y),black)
    return src
