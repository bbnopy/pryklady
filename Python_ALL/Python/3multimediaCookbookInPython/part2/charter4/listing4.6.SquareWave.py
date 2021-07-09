def squareWave(freq,amplitude):
    # Get a blank sound
    mySound =  getMediaPath("sec1silence.wav")
    square = makeSound(mySound)

    # Set music constants
    samplingRate = getSamplingRate(square) # sampling rate
    seconds = 1   # play for 1 second

    # Build tools for this wave
    # seconds per cycle: make sure floating point
    interval = 1.0 * seconds / freq
    # creates floating point since interval is fl point
    samplesPerCycle = interval * samplingRate
    # we need to switch every half-cycle
    samplesPerHalfCycle = int(samplesPerCycle / 2)
    sampleVal = amplitude
    s=1
    i=1

    for s in range (1, getLength(square)+1):
        # if end of a half-cycle
        if (i > samplesPerHalfCycle):
            # reverse the amplitude every half-cycle
            sampleVal = sampleVal * -1
            # and reinitialize the half-cycle counter
            i=0
        setSampleValueAt(square,s,sampleVal)
        i=i+1

    return(square)
