def echo(delay):
    f = pickAFile()
    s1 = makeSound(f)
    s2 = makeSound(f)

    for p in range(delay+1, getLength(s1)):
        #set delay to original value + delayed value * .6
        setSampleValueAt(s1, p, getSampleValueAt( s1,p) + .6*getSampleValueAt(s2, p-delay) )

        play(s1)
