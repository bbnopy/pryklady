def littlepicture():
    canvas = makePicture(getMediaPath("640x480.jpg"))
    addText(canvas,10,50,"This is not a picture")
    addLine(canvas,10,20,300,50)
    addRectFilled(canvas,0,200,300,500,yellow)
    addRect(canvas,10,210,290,490)
    return canvas
