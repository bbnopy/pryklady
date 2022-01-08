def increaseVolumeByRange(sound):
    for sampleIndex in range(1,getLength(sound)+1):
        value = getSampleValueAt(sound,sampleIndex)
        setSampleValueAt(sound,sampleIndex,value * 2)
