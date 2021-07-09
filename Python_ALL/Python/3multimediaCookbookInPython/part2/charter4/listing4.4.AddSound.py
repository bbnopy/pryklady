def addSounds(sound1,sound2):
    for index in range(1,getLength(sound1)+1):
        s1Sample = getSampleValueAt(sound1,index)
        s2Sample = getSampleValueAt(sound2,index)
        setSampleValueAt(sound2,index,s1Sample+s2Sample)
