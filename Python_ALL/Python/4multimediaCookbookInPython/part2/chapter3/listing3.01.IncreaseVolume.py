def increaseVolume(sound):
    for sample in getSample(sound):
        value = getSample(sample)
        setSample(sample,value * 2)
