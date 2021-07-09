def shift(filename,factor):
    source = makeSound(filename)
    target = makeSound(filename)
    sourceIndex = 1

    for targetIndex in range(1, getLength( target)+1):
        setSampleValueAt( target, targetIndex, getSampleValueAt(source, int(sourceIndex)))
        sourceIndex = sourceIndex + factorif sourceIndex > getLength(source):
            sourceIndex = 1

            play(target)
            return target
