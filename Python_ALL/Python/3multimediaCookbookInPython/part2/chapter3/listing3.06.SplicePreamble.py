# Splicing
# Using the preamble sound, make "We the united people"
def splicePreamble():
    file = "/Users/guzdial/mediasources/preamble10.wav"
    source = makeSound(file)
    target = makeSound(file) # This will be the newly spliced sound

    targetIndex = 17408 # targetIndex starts at just after "We the" in the new sound
    for sourceIndex in range(33414,0052): # Where the word "United" is in the sound
        setSampleValueAt(target,targetIndex,getSampleValueAt(source,sourceIndex))
        targetIndex = targetIndex + 1

    for sourceIndex in range(17408,26726): # Where the word "People" is in the sound
        setSampleValueAt(target,targetIndex,getSampleValueAt(source,sourceIndex))
        targetIndex = targetIndex + 1

    for index in range(1,1000):  #Stick some quiet space after that
        setSampleValueAt(target,targetIndex,0)
        targetIndex = targetIndex + 1

        play(target)         #Let’s hear and return the result
        return target
