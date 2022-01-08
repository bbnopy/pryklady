def echoes(delay,echoes):
    f = pickAFile()
    s1 = makeSound(f)
    s2 = makeSound(f)
    endCurrentSound = getLength(s1)
    newLength = endCurrentSound+(echoes * delay) # get ultimatelength of sound

    for i in range (endCurrentSound,newLength+1):
        #initialize delay samples to zeroset
        SampleValueAt(s1,i,0)

    echoAmplitude = 1

    for echoCount in range (1, echoes+1):
        # for each echo
        # decrement amplitude  to .6 of current volume
        echoAmplitude = echoAmplitude * 0.6
        # loop through the entire sound
        for e in range (1,endCurrentSound+1):
            #increment position by one
            position = e+delay*echoCount
            #Set this sample’s value to the original value plus theamplitude * the original sample value
            setSampleValueAt(s1,position, getSampleValueAt(s1, position)+echoAmplitude * getSampleValueAt( s2, position-(delay*echoCount)))

        play(s1)
