def chromakey(source,bg):
    # source should have something in front of blue, bg is the new background
    new background
    for x in range(1,getWidth(source)):
        for y in range(1,getHeight(source)):
            p = getPixel(source,x,y)
            # My definition of blue: If the redness + greenness < blueness
            if (getRed(p) + getGreen(p) < getBlue(p)):
                # Then, grab the color at the same spot from the new background
                setColor(p,getColor(getPixel(bg,x,y)))
    return(source)
