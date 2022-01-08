# Resizes a picture by a given positve real > 0
# such that 1 is the image unalterd, 2 is the image double in size,
# 0.5 is the image sized down in half
# so far only both the width and height can be altered at once(not one seperate of the other)
# basic formula is old(x or y) / szMult = new(x or y)
# this code takes the new picture and for every pixel get a coresponding pixel from the original
# szMult > 1 reuses pixels, while szMult < 1 skips pixels
# this is the simplest way to go about resizing an image, the result will look blocky
# better algorithims involve linear interpolation and other such ways to smoth the image and
# fill in the gaps, one thing that does help is to blur the enlarged images to smooth them.
def resize(szMult):
    pic = makePicture(pickAFile())
    print(’old szw ’ , getWidth(pic) , ’ old szH ’ ,getHeight(pic))
    szW = getWidth(pic) * szMult
    szH = getHeight(pic) * szMult
    szW = int(szW)szH = int(szH)
    print(’new szw ’ , szW , ’ new szH ’ , szH)
    newPic = BlankPicture(szW,szH)

    for x in range(0,getWidth(newPic)):
        for y in range(0,getHeight(newPic)):
            setColor(getPixel(newPic,x,y), getColor( getPixel( pic,int(x/szMult), int(y/szMult))))
    return newPic
