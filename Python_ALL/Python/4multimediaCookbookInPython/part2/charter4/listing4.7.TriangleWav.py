def triangleWav(freq):
    # Get a blank sound
    myFolder = setMediaFolder()
    mySound =  getMediaPath("sec1silence.wav")
    triangle = makeSound(mySound)

    # Set music constants
    amplitude = 6000 # Loudness at 6000: could be any from 1 to 32768
    samplingRate = 22050 # sampling rate
    seconds = 1 # play for 1 second

    # Build tools for this wave
    # seconds per cycle: make sure floating point
    interval = 1.0 * seconds / freq
    # creates floating point since interval is fl point
    samplesPerCycle = interval * samplingRate
    # weneed to switch every half-cycle
    samplesPerHalfCycle = int(samplesPerCycle / 2)
    # value to add for each subsequent sample; must be integer
    increment = int(amplitude / samplesPerHalfCycle)
    # start at bottom and increment or decrement as needed
    sampleVal = -amplitude
    i=1

    for s in range (1, samplingRate + 1): # create 1 second sound
        # ifend of a half-cycle
        if (i > samplesPerHalfCycle):
            # reverse the increment every half-cycle
            increment = increment * -1
            # and reinit the half-cycle counter
            i = 0

        sampleVal = sampleVal + increment
        setSampleValueAt(triangle,s,sampleVal)
        i = i+1

    play(triangle)
