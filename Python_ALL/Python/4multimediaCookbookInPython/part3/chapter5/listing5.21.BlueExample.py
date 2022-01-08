def blurExample(size):
    pic = makePicture(pickAFile())
    newPic = blur(pic,size)
    show(newPic)
    show(pic)

    # !!
    # To blur an image we take a pixel and set it’s color to the average of all pixels around
    # it(of a certain distance) to the current pixels color.  This give the effect of
    # blending things together such as in the case of a blur where you lose detail.
    #
    # pic is the image, and size is how big an area to average, 1=3x3 pixel area with current pixel
    # in the center, 2=5x5, 3=7x7...
    # positive #s only , 0 will do nothing and return the original image

    def blur(pic,size):
        new = getFolderPath("640x480.jpg")

        for x in range(1,getWidth(pic)):
            print ’On x> ’, x

            for y in range(1,getHeight(pic)):
                newClr = blurHelper(pic,size,x-size,y-size)
                setColor(getPixel(new,x,y),newClr)
        return new

        # !!
        # At a given x,y(integer that is in the image) in the picture,pic, is sums up the area
        # of pixels as indicated by size.
        #
        # returns a Color representing the average of the surrounding pixels

        def blurHelper(pic,size,x,y):
            red,green,blue = 0,0,0
            cnt = 0

            for x2 in range(0,(1+(size*2))):
                if(x+x2 >= 0):
                    if(x+x2 < getWidth(pic)):

                        for y2 in range(0,(1+(size*2))):
                            if(y+y2 >= 0):
                                if(y+y2 < getHeight(pic)):
                                    p=getPixel(pic,(x+x2),(y+y2))
                                    blue = blue + getBlue(p)
                                    red = red + getRed(p)
                                    green = green + getGreen(p)
                                    cnt = cnt + 1
            return makeColor(red/cnt,green/cnt,blue/cnt)
