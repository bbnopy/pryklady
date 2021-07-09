def double(filename):
    source = makeSound(filename)
    target = makeSound(filename)

    targetIndex = 1

    for sourceIndex in range(1, getLength(source)+1, 2):
        setSampleValueAt( target, targetIndex, getSampleValueAt(source, sourceIndex))
        targetIndex = targetIndex + 1

    #Clear out the rest of the target sound -- it’s only half full!
    for secondHalf in range( getLength( target)/2, getLength( target)):
        setSampleValueAt(target,targetIndex,0)
        targetIndex = targetIndex + 1

        play(target)
        return target
