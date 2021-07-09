def sineWave(freq,amplitude):
    #Get a blank soundmy
    Sound =  getMediaPath(’sec1silence.wav’)
    buildSin = makeSound(mySound)

    #Set sound constant
    sr = getSamplingRate(buildSin) # sampling rate

    interval = 1.0/freq
    samplesPerCycle =  interval * sr # samples per cycle: make sure floating point
    maxCycle = 2 * pi

    for pos in range (1,getLength(buildSin)+1):
        rawSample = sin( (pos / samplesPerCycle) * maxCycle)
        sampleVal = int( amplitude*rawSample)
        setSampleValueAt(buildSin,pos,sampleVal)

    return (buildSin)

def addSounds(sound1,sound2):
    for index in range(1,getLength(sound1)+1):
        s1Sample = getSampleValueAt(sound1,index)
        s2Sample = getSampleValueAt(sound2,index)
        setSampleValueAt(sound2,index,s1Sample+s2Sample)
