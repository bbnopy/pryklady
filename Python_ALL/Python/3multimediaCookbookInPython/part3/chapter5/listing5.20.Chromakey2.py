def chromakey2(source,bg):
    for p in pixels(source):
        if (getRed(p)+getGreen(p) < getBlue(p)):
            setColor(p,getColor(getPixel(bg,x(p),y(p))))
    return source
