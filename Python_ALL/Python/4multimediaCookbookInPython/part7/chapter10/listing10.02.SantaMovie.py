def santaMovie(folder):
    santafile = "/Users/guzdial/Work/mediasources/santa.jpg"
    santa = makePicture(santafile)
    startXPos = 10
    startYPos = 100

    import os

    for file in os.listdir(folder):
        frame = makePicture(folder+file)
        xmax = min(startXPos+getWidth(santa),getWidth(frame))
        ymax = min(startYPos+getHeight(santa),getHeight(frame))
        santaX = 1

        for x in range(startXPos,xmax):
            santaY = 1

            for y in range(startYPos,ymax):
                px = getPixel(frame,x,y)
                santaPixel = getPixel(santa,santaX,santaY)
                setColor(px,getColor(santaPixel))
                santaY = santaY + 1
                santaX = santaX + 1
                writePictureTo(frame,folder+"s"+file)

                # make Santa sink one line lower each frame
                startXPos = startXPos + 1
