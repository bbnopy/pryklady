def AnimationSimple():
    frames = 50
    rx = 0
    ry = 0
    rw = 50
    rh = 50

    for f in range(1,frames+1):
        pic = BlankPicture(500,500)
        pic.addOvalFilled(Color(255,0,0),x,y,w,h)
        if(f < 10):
            pic.writeTo(’test0%d.jpg’%(f))
            else:
                pic.writeTo(’test0%d.jpg’%(f))
                x = 5 + x
                y = 5 + y

def AnimationSimple2():
    frames = 100
    w = 50
    h = 50 # ball postions balls r,g,b,y x and y posistions
    rx = 0
    ry = 0
    bx = 275
    by = 225
    gx = 275
    gy = 275
    yx = 225
    yy = 275

    for f in range(1,frames+1):
        pic = BlankPicture(500,500)
        if(f < 50):
            rx += 5
            ry += 5
            else:
                rx -= 2
                ry -= 2
                bx += 5
                by -= 5
                gx += 5
                gy += 5
                yx -= 5
                yy += 5
                pic.addOvalFilled(red,rx,ry,w,h)
                pic.addOvalFilled(blue,bx,by,w,h)
                pic.addOvalFilled(green,gx,gy,w,h)
                pic.addOvalFilled(yellow,yx,yy,w,h)
                if(f < 10):
                    pic.writeTo(’test00%d.jpg’%(f))
                    elif(f < 100):
                        pic.writeTo(’test0%d.jpg’%(f))
                        else:
                            pic.writeTo(’test%d.jpg’%(f))
