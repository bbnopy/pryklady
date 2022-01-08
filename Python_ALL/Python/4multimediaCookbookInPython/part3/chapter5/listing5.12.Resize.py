def resize(source,increment):
    newWidth = int(getWidth(source)* (1/increment))
    newHeight = int(getWidth(source)* (1/increment))
    target = makePicture( getMediaPath("7inx95in.jpg"))
    sourceX = 1

    for targetX in range(1,newWidth):
        sourceY = 1

        for targetY in range(1,newHeight):
            targetPixel = getPixel(target,targetX,targetY)
            sourcePixel = getPixel(source,int(sourceX),int(sourceY))
            setColor(targetPixel,getColor(sourcePixel))
            sourceY = sourceY + increment

            if sourceY > getHeight(source):
                sourceY = sourceY- getHeight(source)
                sourceX = sourceX + increment

                if sourceX > getWidth(source):
                    sourceX = sourceX - getWidth(source)

        return target
