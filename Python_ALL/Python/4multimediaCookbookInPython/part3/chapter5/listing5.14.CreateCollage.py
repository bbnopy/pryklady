def createCollage():
    flower1 = makePicture(getMediaPath("flower1.jpg"))
    print flower1
    flower2 = makePicture(getMediaPath("flower2.jpg"))
    print flower2
    canvas = makePicture(getMediaPath("640x480.jpg"))
    print canvas
    # First picture, at left edge
    targetX = 1

    for sourceX in range(1,getWidth(flower1)):
        targetY = getHeight(canvas)-getHeight(flower1)-5

        for sourceY in range(1,getHeight(flower1)):
            px = getPixel(flower1,sourceX,sourceY)
            cx = getPixel(canvas,targetX,targetY)
            setColor(cx,getColor(px))
            targetY = targetY + 1
        targetX = targetX + 1

        # Second picture, 100 pixels over
        targetX = 100

        for sourceX in range(1,getWidth(flower2)):
            targetY = getHeight(canvas)-getHeight(flower2)-5

            for sourceY in range(1,getHeight(flower2)):
                px = getPixel(flower2,sourceX,sourceY)
                cx = getPixel(canvas,targetX,targetY)
                setColor(cx,getColor(px))
                targetY = targetY + 1
            targetX=targetX + 1

            # Third picture, flower1 negated
            negative(flower1)
            targetX = 200

            for sourceX in range(1,getWidth(flower1)):
                targetY = getHeight(canvas)-getHeight(flower1)-5

                for sourceY in range(1,getHeight(flower1)):
                    px = getPixel(flower1,sourceX,sourceY)
                    cx = getPixel(canvas,targetX,targetY)
                    setColor(cx,getColor(px))
                    targetY = targetY + 1
                targetX = targetX + 1

                # Fourth picture, flower2 with no blue
                clearBlue(flower2)
                targetX = 300

                for sourceX in range(1,getWidth(flower2)):
                    targetY = getHeight(canvas)-getHeight(flower2)-5

                    for sourceY in range(1,getHeight(flower2)):
                        px = getPixel(flower2,sourceX,sourceY)
                        cx = getPixel(canvas,targetX,targetY)
                        setColor(cx,getColor(px))
                        targetY = targetY + 1
                    targetX = targetX + 1

                    # Fifth picture, flower1, negated with decreased red
                    decreaseRed(flower1)
                    targetX = 400

                    for sourceX in range(1,getWidth(flower1)):
                        targetY = getHeight(canvas)-getHeight(flower1)-5

                        for sourceY in range(1,getHeight(flower1)):
                            px = getPixel(flower1,sourceX,sourceY)
                            cx = getPixel(canvas,targetX,targetY)
                            setColor(cx,getColor(px))
                            targetY = targetY + 1
                        targetX = targetX + 1
                    show(canvas)

                return(canvas)
