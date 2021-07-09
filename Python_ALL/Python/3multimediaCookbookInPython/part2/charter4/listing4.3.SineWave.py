def sineWave(freq,amplitude):
    #Get a blank sound
    mySound =  getMediaPath(’sec1silence.wav’)
    buildSin = makeSound(mySound)
    #Set sound constant
    sr = getSamplingRate(buildSin)        # sampling rate
    interval = 1.0/freq      # Make sure it’s floating point
    samplesPerCycle =  interval * sr    # samples per cycle
    maxCycle = 2 * pi

    for pos in range (1,getLength(buildSin)+1):
        rawSample = sin( (pos / samplesPerCycle) * maxCycle)
        sampleVal = int( amplitude*rawSample)
        setSampleValueAt(buildSin,pos,sampleVal)

    return (buildSin)
