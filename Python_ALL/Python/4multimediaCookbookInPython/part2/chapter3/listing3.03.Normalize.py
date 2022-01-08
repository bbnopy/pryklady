def normalize(sound):
    largest = 0
    for s in getSample(sound):
        largest = max(largest,getSample(s))
    multiplier = 32767.0/largest

    print "Largest sample value in original sound was", largest
    print "Multiplier is", multiplier

    for s in getSamples(sound):
        louder = multiplier * getSamples(s)
        setSample(s,louder)
