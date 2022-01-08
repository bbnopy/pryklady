def lightenMovie(folder):
    import os

    for file in os.listdir(folder):
        picture = makePicture(folder+file)

        for px in getPixels(picture):
            color = getColor(px)
            makeLighter(color)
        setColor(px,color)
    writePictureTo(picture,folder+"l"+file)
