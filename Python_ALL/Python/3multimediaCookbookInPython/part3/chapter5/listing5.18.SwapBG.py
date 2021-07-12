# Picture with person, background, and newbackground
def swapbg(pic1,bg,newbg):
    for x in range(1,getWidth(pic1)):
        for y in range(1,getHeight(pic1)):
            p1px = getPixel(pic1,x,y)
        bgpx = getPixel(bg,x,y)
        if (distance(getColor(p1px),getColor(bgpx)) < 15.0):
            setColor(p1px,getColor(getPixel(newbg,x,y)))
    return pic1
