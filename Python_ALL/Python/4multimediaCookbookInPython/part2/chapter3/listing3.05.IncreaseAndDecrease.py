def increaseAndDecrease(sound):
    for sampleIndex in range(1,getLength(sound)/2):
        value = getSampleValueAt(sound,sampleIndex)
        setSampleValueAt(sound,sampleIndex,value * 2)
    for sampleIndex in range(getLength(sound)/2,getLength(sound)+1):
        value = getSampleValueAt(sound,sampleIndex)
        setSampleValueAt(sound,sampleIndex,value * 0.2)
